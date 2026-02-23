from http.client import HTTPException
from fastapi import APIRouter
from typing import List
from src.domain.models.product import Product
from src.application.product_usecase import ProductUseCase
from src.domain.services.product_service import ProductService
from src.infrastructure.repositories.in_memory_product_repository import InMemoryProductRepository
from src.domain.services.ia_service import IAService

router = APIRouter()

repository = InMemoryProductRepository()
service = ProductService(repository)
usecase = ProductUseCase(service)

@router.get("/products", response_model=List[Product])
def list_products():
    return usecase.list_products()

@router.post("/products", response_model=Product)
def create_product(product: Product):
    try:
        return usecase.create_product(product)
    except Exception as e:
        return {"message": IAService(e, e.with_traceback).ia_error_handler()}
    
@router.put("/products/{id}", response_model=Product)
def update_product(id: int, product: Product):
    updated = service.update_product(id, product)
    if not updated:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return updated

@router.delete("/products/{id}")
def delete_product(id: int):
    deleted = service.delete_product(id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return {"message": "Produto removido com sucesso"}