from config_rules.repository import AbstractConfigRulesRepository
from config_rules.domain.model import ConfigurationRule, DependencyRule, IncompatibilityRule
from uuid import UUID

class ConfigurationRuleService:
    def __init__(self, rule_repository: AbstractConfigRulesRepository):
        self.rule_repository = rule_repository
    
    def create_dependency_rule(self, product_id: UUID, 
                              if_part: str, if_option: str,
                              then_part: str, then_options: list[str],
                              error_message: str) -> ConfigurationRule:

        rule = DependencyRule(
            product_id=product_id,
            if_part=if_part,
            if_option=if_option,
            then_part=then_part,
            then_options=then_options,
            error_message=error_message
        )
        return self.rule_repository.add(rule)
    
    def create_incompatibility_rule(self, product_id: UUID,
                                  part1: str, option1: str,
                                  part2: str, option2: str,
                                  error_message: str) -> ConfigurationRule:
        rule = IncompatibilityRule(
            product_id=product_id,
            part1=part1,
            option1=option1,
            part2=part2,
            option2=option2,
            error_message=error_message
        )
        return self.rule_repository.add(rule)
    
    def delete_rule(self, rule_id: UUID) -> bool:
        return self.rule_repository.delete(rule_id)
    
    def validate_configurations(self, product_id: UUID, configurations: list[dict]) -> tuple[bool, str | None]:
        rules = self.rule_repository.get_rules_for_product(product_id)
        
        for rule in rules:
            for config in configurations:
                if not rule.validate(config):
                    return False, rule.error_message
        
        return True, None
