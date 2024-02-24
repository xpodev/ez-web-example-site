from sqlalchemy import Column, String, Integer, Float

import ez

from jsx.html import *
from ez.jsx import *
from jsx.styling import Style
from jsx import Component

from ez.database.model import Model

from fastapi.staticfiles import StaticFiles

resources_path = ez.SITE_DIR / "resources" / "images"
ez._app.mount("/res/i", StaticFiles(directory=f"{resources_path}"), name="res")

class ProductImage(Model):
    __table_name__ = "eco_product_images"

    id = Column(Integer, primary_key=True)
    product_id = Column(String)
    image_resource = Column(String)
    image_index = Column(Integer)


class ProductModel(Model):
    __table_name__ = "eco_products"

    id = Column(String, primary_key=True)
    name = Column(String)
    price = Column(Float)

class ProductRepository:
    def all(self):
        return ProductModel.all()

    def get(self, id):
        return ProductModel.get(id)
    

class ProductImageRepository:
    def get_by_product_id(self, product_id):
        return ProductImage.filter_by(product_id=product_id).order_by(ProductImage.image_index).all()


PRODUCT_REPOSITORY = ProductRepository()
PRODUCT_IMAGE_REPOSITORY = ProductImageRepository()

class ImageCarousel(Component):
    def __init__(self, images: list[str]):
        self.images = images
        print("Images:", images)

    def render(self):
        return Div(
            *[Div(
                Img(
                    src=f"/res/i/{image}",
                    class_name="d-block",
                    style=Style().height("300px"),
                ),
            )
            for i, image in enumerate(self.images)]
        )


def render(product_id: int, title_color):
    print("Product ID:", product_id)
    product = PRODUCT_REPOSITORY.get(product_id)

    if product is None:
        return "404"
    
    product_images = PRODUCT_IMAGE_REPOSITORY.get_by_product_id(product_id)

    return Div(
        H1(
            product.name,
            class_name="bg-primary p-3 mb-3 text-center",
            style=Style().color(title_color),
        ),
        Div(
            ImageCarousel([image.image_resource for image in product_images]),
            class_name="carousel slide",
            data_ride="carousel",
        ),
    )

