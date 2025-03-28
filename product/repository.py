from uuid import UUID
from abc import abstractmethod, ABC

from sqlalchemy.orm import joinedload
from product.domain.model import CharacteristicOption, PartConfiguration, PartOption, Product, ProductPart
from sqlalchemy import text

class AbstractProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product):
        raise NotImplementedError

    @abstractmethod
    def remove(self, product_id) -> None:
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

    def remove(self, product_id: UUID):
        try:
            # product = self.session.query(Product).filter_by(id=product_id).first()
            product = self.session.execute(
                text("SELECT * FROM products WHERE id = :product_id"), 
                {"product_id": product_id}
            ).first()

            # print(product)
            
            if product:
                self.session.delete(product)
                self.session.commit()
                print(f"Successfully deleted product {product_id}")  
            else:
                print(f"No product found with id {product_id}")  
                raise ValueError("No product found with id {product_id}")
        
        except Exception as e:
            self.session.rollback()
            print(f"Error deleting product: {e}")
            raise


    def get(self, product_id) -> Product | None:
        return self.session.query(Product)\
            .options(
                #joinedload(Product.parts).joinedload(ProductPart.options),  #type: ignore
                # joinedload(Product.part_configs).joinedload(PartConfiguration.available_options) #type: ignore
            ).filter_by(id=product_id).one_or_none()

    def get_all(self):
        # return self.session.query(Product).all() or []
        return self.session.query(Product)\
        .options(
            joinedload(Product.default_characteristics), #type: ignore
            joinedload(Product.available_characteristics)#type: ignore
            # joinedload(Product.parts).joinedload(ProductPart.options), #type: ignore
            # joinedload(Product.part_configs).joinedload(PartConfiguration.available_options) #type: ignore
        )\
        .all() or []

    def create_part(self, part):
        self.session.add(part)
        self.session.commit()

    def get_part(self, part_id) -> ProductPart | None:
        self.session.query(ProductPart).filter_by(id=part_id).one_or_none()
         
    def get_part_options(self, ids) -> list[PartOption]:
        table_name = "part_options"
        query = text(f"SELECT * FROM {table_name} WHERE id IN :ids")

        return self.session.execute(query, {"ids": ids}).fetchall()
    
    # def get_product_part_by_id(self, product_part_id: UUID, product_id: UUID) -> ProductPart | None:
    #     # FIXME: db_models
    #     part_model = self.session.query(db_models.ProductPart).filter_by(id=product_part_id, product_id=product_id).first()
    #     return part_model


class InMemoryProductRepository(AbstractProductRepository):
    def __init__(self, part_options, product_parts, products):
        # TODO: review - do we actually need to pass in part options here? I feel like 
        # we 're doing redundant work

        # we can just extend from product_parts
        self._part_options = set(part_options)
        self._products_parts = set(product_parts)
        self._products = set(products)

    def add(self, product):
        self._products.add(product)
   
    def remove(self, product_id):
        self._products = set([product for product in self._products if product.id != product_id])

    def get(self, product_id):
        return next(p for p in self._products if p.id == product_id)

    def get_all(self): 
        return list(self._products)

    def get_part_options(self, ids): 
        return list(filter(lambda opt: opt.id in ids, self._part_options))

    def create_part(self, part: ProductPart):
        self._products_parts.add(part)
        self._part_options.update(part.options)

    def get_part(self, part_id):
        for p in self._products_parts:
            if p.id == part_id:
                return p
        
