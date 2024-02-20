from ez.jsx import Page
from jsx.html import Div

class SinglePage(Page):
    def body():
        return Div(
            Div(
                "Hello, World!",
                class_name="card mx-auto w-50 p-3 mt-5 text-center"
            ),
        )