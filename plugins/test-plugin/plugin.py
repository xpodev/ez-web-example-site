import ez

# from ez.jsx import Page, Card
from jsx.html import *
from jsx.components.component import Component
# from ezplugins import test_plugin

# test_plugin.my_api(1, "2")

__version__ = "0.0.1"


class Page(Component):
    def render(self):
        return Html(
            Head(
                Title("Sample Page"),
                Link(rel="stylesheet", href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css"),
                Script(src="https://code.jquery.com/jquery-3.5.1.slim.min.js"),
                Script(src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.5.4/dist/umd/popper.min.js"),
                Script(src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"),
            ),
            Body(
                self.body()
            )
        )
    
    def body(self):
        return Fragment(*self.children)
    

class Card(Component):
    def render(self):
        classes = set(["card"])
        if "class_name" in self.props:
            classes.add(self.props["class_name"])
        
        return Div(
            *self.children,
            class_name=" ".join(classes)
        )
    

class SamplePage(Page):
    def body(self):
        return Card(
            H1("Hello, World!"),
            P("This is a sample page."),
            class_name="bg-light p-5 rounded w-50 mx-auto mt-5"
        )


@ez.get("/test")
def test():
    return SamplePage()


class MyAPI:
    def my_api(self, x: int, y: str) -> bool:
        return x > y


__api__ = MyAPI()
