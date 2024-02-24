from jsx.html import *
from ez.jsx import *
from ez.database.models.page import PageModel


def render(**props):
    return Page(
        SinglePage(
            **props,
        ),
    )


class SinglePage(Page):
    def __init__(self, page: PageModel):
        self.page = page

    def body(self):
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
                        "color": "white",
                        "padding": "10px",
                        "font-family": "sans-serif",
                    }
                ),
            ),
        )
