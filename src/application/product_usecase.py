from typing import Optional
from src.domain.models.product import Product
from src.domain.services.product_service import ProductService

class ProductUseCase:
    def __init__(self, service: ProductService):
        self.service = service

    def list_products(self):
        return self.service.get_products()

    def create_product(self, product: Product):
        return self.service.add_product(product)

    def update_product(self, id: int, product: Product) -> Optional[Product]:
        return self.service.update_product(id, product)

    def delete_product(self, id: int) -> Optional[Product]:
        return self.service.delete_product(id)