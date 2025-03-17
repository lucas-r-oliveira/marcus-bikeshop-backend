from abc import abstractmethod, ABC
from product.domain.model import PartOption, Product, ProductPart
from sqlalchemy import text

class AbstractProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        raise NotImplementedError

    @abstractmethod
    def get(self, product_id) -> Product | None:
        raise NotImplementedError

    @abstractmethod
    def get_all(self) -> list[Product]: 
        raise NotImplementedError

    @abstractmethod
    def get_part_options(self, ids) -> list[PartOption]: 
        raise NotImplementedError

    @abstractmethod
    def create_part(self, part: ProductPart): 
        raise NotImplementedError

    @abstractmethod
    def get_part(self, part_id) -> ProductPart | None:
        raise NotImplementedError


class SQLAlchemyProductRepository(AbstractProductRepository):
    def __init__(self, session):
        self.session = session
    # TODO: review rollbacks

    def add(self, product: Product): #-> Product:
        self.session.add(product)
        self.session.commit()


    def get(self, product_id) -> Product | None:
        return self.session.query(Product).filter_by(id=product_id).one_or_none()

    def get_all(self):
        return self.session.query(Product).all() or []

    def create_part(self, part):
        self.session.add(part)
        self.session.commit()

    def get_part(self, part_id) -> ProductPart | None:
        self.session.query(ProductPart).filter_by(id=part_id).one_or_none()
         


    # TODO abstract method
    def get_part_options(self, ids) -> list[PartOption]:
        table_name = "part_options"
        query = text(f"SELECT * FROM {table_name} WHERE id IN :ids")

        return self.session.execute(query, {"ids": ids}).fetchall()
    
    # def get_product_part_by_id(self, product_part_id: UUID, product_id: UUID) -> ProductPart | None:
    #     # FIXME: db_models
    #     part_model = self.session.query(db_models.ProductPart).filter_by(id=product_part_id, product_id=product_id).first()
    #     return part_model
