from jsx.html import Div, H1, P
from jsx.styling import Style

from ez.templates import PageData, template


# @template("product_page")
# class ProductPage:
def render(product_id, color: str = "black"):
    return Div(
        H1(
            f"Product {product_id}", 
            style=Style().color(color)
        ),
        Div(
            P("Copyright 2021"),
            P("All rights reserved"),
            style=Style().position("absolute").bottom(0).width("100%").textAlign("center"),
        )
    )
