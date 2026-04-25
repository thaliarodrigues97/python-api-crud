from typing import List, Optional
from src.domain.models.product import Product # type: ignore

class InMemoryProductRepository:
    def __init__(self):
        self.products = []
        self.counter = 1

    def get_all(self) -> List[Product]:
        return self.products

    def add(self, product: Product) -> Product:
        product.id = self.counter
        self.counter += 1
        self.products.append(product)
        return product
    
    def update(self, product_id: int, new_product: Product) -> Optional[Product]:
        for idx, product in enumerate(self.products):
            if product.id == product_id:
                new_product.id = product_id
                self.products[idx] = new_product
                return new_product
        return None
    

    def delete(self, product_id: int) -> bool:
        for idx, product in enumerate(self.products):
            if product.id == product_id:
                del self.products[idx]
                return True
        return False
