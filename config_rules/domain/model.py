from abc import ABC, abstractmethod
from uuid import UUID, uuid4


class ConfigurationRule(ABC):
    def __init__(self, product_id: UUID, error_message: str):
        self.rule_id = uuid4() 
        self.product_id = product_id
        self.error_message = error_message

        @abstractmethod
        def validate(self, configuration: dict) -> bool:
            raise NotImplementedError

class DependencyRule(ConfigurationRule):
    def __init__(self, product_id: UUID, 
                 if_part: str, if_option: str, 
                 then_part: str, then_options: list[str], 
                 error_message: str):
        super().__init__(product_id, error_message)
        self.if_part = if_part
        self.if_option = if_option
        self.then_part = then_part
        self.then_options = then_options
    
    def validate(self, configuration: dict) -> bool:
        if configuration.get(self.if_part) == self.if_option:
            if self.then_part in configuration:
                return configuration[self.then_part] in self.then_options
            return False
        return True

class IncompatibilityRule(ConfigurationRule):
    def __init__(self, product_id: UUID,
                 part1: str, option1: str, 
                 part2: str, option2: str, 
                 error_message: str):
        super().__init__(product_id, error_message)
        self.part1 = part1
        self.option1 = option1
        self.part2 = part2
        self.option2 = option2
    
    def validate(self, configuration: dict) -> bool:
        if self.part1 in configuration and self.part2 in configuration:
            if configuration[self.part1] == self.option1 and configuration[self.part2] == self.option2:
                return False
        return True
