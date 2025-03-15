from dataclasses import dataclass

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


    
