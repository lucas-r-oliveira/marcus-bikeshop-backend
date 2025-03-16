from abc import ABC, abstractmethod
from config_rules.domain.model import ConfigurationRule
from uuid import UUID

class AbstractConfigRulesRepository(ABC):
    @abstractmethod
    def add(self, rule: ConfigurationRule) -> ConfigurationRule:
        raise NotImplementedError

    @abstractmethod
    def get_rules_for_product(self, product_id: UUID) -> list[ConfigurationRule]:
        raise NotImplementedError

    @abstractmethod
    def delete(self, rule_id: UUID) -> bool:
        raise NotImplementedError

class SQLAlchemyConfigRulesRepository(AbstractConfigRulesRepository):
    def __init__(self, session):
        self.session = session

    def add(self, rule: ConfigurationRule) -> ConfigurationRule:
        return self.session.add(rule)
    
    #TODO: 
    def get_rules_for_product(self, product_id: UUID) -> list[ConfigurationRule]:
        # return session.query. ... 
        return []
    
    
    #TODO:
    def delete(self, rule_id: UUID) -> bool:
        return True
