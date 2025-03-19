from abc import ABC, abstractmethod
from config_rules.domain.model import ConfigurationRule
from uuid import UUID

class AbstractConfigRulesRepository(ABC):
    # @abstractmethod
    # def add(self, rule: ConfigurationRule) -> ConfigurationRule:
    #     raise NotImplementedError

    @abstractmethod
    def get_rules_for_product(self, product_id: UUID) -> list[ConfigurationRule]:
        raise NotImplementedError

    # @abstractmethod
    # def delete(self, rule_id: UUID) -> bool:
    #     raise NotImplementedError

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
