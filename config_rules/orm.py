from sqlalchemy import (
    Column,
    ForeignKey,
    String,
    Table,
)
from sqlalchemy.orm import relationship
from sqlalchemy.sql.sqltypes import UUID

from common import metadata
from config_rules.domain.model import ConfigurationRule, DependencyRule, IncompatibilityRule

configuration_rule = Table(
    "configuration_rules",
    metadata,
    Column("rule_id", UUID, primary_key=True),
    Column("product_id", UUID, ForeignKey("products.id")),
    Column("error_message", String(511)),
    Column("type", String(50)),  # Discriminator column
    Column("if_option", UUID, nullable=True),  # Used by both rule types
)

# m2m
rule_then_options = Table(
    "rule_then_options",
    metadata,
    Column("rule_id", UUID, ForeignKey("configuration_rules.rule_id"), primary_key=True),
    Column("option_id", UUID, primary_key=True)
)

def start_mappers(mapper_registry):
    class RuleOption:
        def __init__(self, option_id):
            self.option_id = option_id

    mapper_registry.map_imperatively(
        RuleOption,
        rule_then_options,
        properties={
            "option_id": rule_then_options.c.option_id,
        }
    )

    rule_mapper = mapper_registry.map_imperatively(
        ConfigurationRule,
        configuration_rule,
        polymorphic_on=configuration_rule.c.type,
        polymorphic_identity="configuration_rule",
        properties={
            "rule_id": configuration_rule.c.rule_id,
            "product_id": configuration_rule.c.product_id,
            "error_message": configuration_rule.c.error_message,
        }
    )

    then_options_relation = relationship(
        RuleOption,
        secondary=rule_then_options,
        collection_class=list,
    )

    mapper_registry.map_imperatively(
        DependencyRule,
        inherits=rule_mapper,
        polymorphic_identity="dependency_rule",
        properties={
            "if_option": configuration_rule.c.if_option,
            "then_options": then_options_relation,
        }
    )

    mapper_registry.map_imperatively(
        IncompatibilityRule,
        inherits=rule_mapper,
        polymorphic_identity="incompatibility_rule",
        properties={
            "if_option": configuration_rule.c.if_option,
            "then_options": then_options_relation,
        }
    )
