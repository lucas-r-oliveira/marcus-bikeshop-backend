from dataclasses import dataclass
from sqlalchemy import DECIMAL, TypeDecorator

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str = "EUR"

    def __add__(self, other):
        if (self.currency != other.currency):
            raise ValueError("Cannot add different currencies together")
        return Money(self.amount + other.amount, self.currency)

    def __mul__(self, other):
        if isinstance(other, int):
            return Money(self.amount * other, self.currency)
        elif isinstance(other, Money):
            return Money(self.amount * other.amount, self.currency)
        
        raise TypeError("Multiplication is not supported for this type") 

    def __rmul__(self, other):
        return self.__mul__(other)


    
# conversion between the database and domain
class MoneyType(TypeDecorator):
    
    # the type to store in the database
    impl = DECIMAL

    def process_bind_param(self, value, dialect):
        # convert to db format
        if value is None:
            return None
        return value.amount

    def process_result_value(self, value, dialect):
        # convert to domain
        if value is None:
            return None
        # FIXME: EUR hardcode
        return Money(amount=value, currency="EUR")
