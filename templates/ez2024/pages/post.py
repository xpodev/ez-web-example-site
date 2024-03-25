from jsx.html import *
from jsx.styling import *
from ez.jsx import *

import ez

def render(page):
    return PostPage(page).render()


class PostPage:
    def __init__(self, page):
        self.page = page

    def render(self):
        return Div(
            H1(
                f"Post - {self.page.title}",
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
