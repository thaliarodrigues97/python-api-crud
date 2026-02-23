from typing import List, Optional
from src.domain.models.product import Product

class ProductService:
    def __init__(self, repository):
        self.repository = repository

    def get_products(self) -> List[Product]:
        return self.repository.get_all()

    def add_product(self, product: Product) -> Product:
        return self.repository.add(product)
    
    def update_product(self, product_id: str, updated_data: dict) -> Optional[Product]:
        return self.repository.update(product_id, updated_data)

    def delete_product(self, product_id: str) -> bool:
        return self.repository.delete(product_id)