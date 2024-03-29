from jsx.html import *
from jsx.styling import *
from ez.jsx import *

from ez.templates import template
from ez.jsx import Card
import ez

def render(page):
    return SinglePage(page).render()


class SinglePage:
    def __init__(self, page):
        self.page = page

    def render(self):
        return Div(
            H1(
                self.page.title,
                class_name="bg-primary text-white p-3 mb-3 text-center",
            ),
            Div(
                self.page.content,
                class_name="p-3",
                style=Style(
                    {
                        "background-color": Color.CORNFLOWER_BLUE,
<<<<<<< HEAD
                        "color": "white",
=======
>>>>>>> 9eba15f (Add ez2024 template)
                        "padding": "10px",
                        "font-family": "sans-serif",
                    }
                ),
            ),
<<<<<<< HEAD
=======
            Div(
                "Your Query: " + ez.request.query_params.get("query", ""),
            )
>>>>>>> 9eba15f (Add ez2024 template)
        )
