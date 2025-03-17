from abc import abstractmethod, ABC
from product.domain.model import PartOption, Product
from sqlalchemy import text

class AbstractProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        raise NotImplementedError

    @abstractmethod
    def get(self, reference) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Product]: 
        raise NotImplementedError

    @abstractmethod
    def get_part_options(self, ids) -> list[PartOption]: 
        raise NotImplementedError


class SQLAlchemyProductRepository(AbstractProductRepository):
    def __init__(self, session):
        self.session = session
    # TODO: review rollbacks

    def add(self, product: Product): #-> Product:
        self.session.add(product)
        self.session.commit()


    def get(self, reference) -> Product | None:
        return self.session.query(Product).filter_by(reference=reference).one_or_none()

    def get_all(self):
        return self.session.query(Product).all() or []

    def get_part_options(self, ids) -> list[PartOption]:
        table_name = "part_options"
        query = text(f"SELECT * FROM {table_name} WHERE id IN :ids")

        return self.session.execute(query, {"ids": ids}).fetchall()
    
    # def get_product_part_by_id(self, product_part_id: UUID, product_id: UUID) -> ProductPart | None:
    #     # FIXME: db_models
    #     part_model = self.session.query(db_models.ProductPart).filter_by(id=product_part_id, product_id=product_id).first()
    #     return part_model
