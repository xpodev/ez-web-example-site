import ez
import ez.plugins
# from ez.events import TreeRenderer
from . import test
from jsx.html import H1


# class TitleChanger:
#     def change_title(self, page: Page):
#         page.title = "EZ Web - Blah"


# @ez.on(TreeRenderer.WillRender)
# def update_title(page: ...):
#     page.title = "EZ Web - Blah"


@ez.get("/title")
def index():
    return H1("Hello, World!")


def main():
    test.run()


# try:
#     ez.install_plugin("D:\\xpodev\\ez-web-src\\tests\\plugins\\test-plugin.zip")
# except FileExistsError:
#     ...
