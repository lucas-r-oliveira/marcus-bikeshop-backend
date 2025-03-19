from abc import ABC, abstractmethod
from config_rules.domain.model import ConfigurationRule
from uuid import UUID

class AbstractConfigRulesRepository(ABC):
    # @abstractmethod
    # def add(self, rule: ConfigurationRule) -> ConfigurationRule:
    #     raise NotImplementedError

    # @abstractmethod
    # def getrules_for_product(self, product_id: UUID) -> list[ConfigurationRule]:
    #     raise NotImplementedError
    
    @abstractmethod
    def get(self, rule_id: UUID) -> ConfigurationRule | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[ConfigurationRule]:
        raise NotImplementedError

    # @abstractmethod
    # def delete(self, rule_id: UUID) -> bool:
    #     raise NotImplementedError

# FIXME:
class SQLAlchemyConfigRulesRepository(AbstractConfigRulesRepository):
    def __init__(self, session):
        self.session = session

    # not in scope
    # def add(self, rule: ConfigurationRule) -> ConfigurationRule:
    #     return self.session.add(rule)
    
    def get_rules_for_product(self, product_id: UUID) -> list[ConfigurationRule]:
        rules = self.session.query(ConfigurationRule).filter_by(product_id=product_id).all()
        return rules

    # not in scope
    # def delete(self, rule_id: UUID) -> bool:
    #     return True

class InMemoryConfigRulesRepository(AbstractConfigRulesRepository):
    def __init__(self, config_rules = set()):
        self.config_rules = config_rules

    def get(self, rule_id):
        for rule in self.config_rules:
            if rule.id == rule_id:
                return rule
        return None

    def get_all(self):
        return self.config_rules
