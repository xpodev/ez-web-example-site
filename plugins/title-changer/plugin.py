import ez
import ez.plugins
# from ez.events import TreeRenderer
# from ez.jsx import Page


# class TitleChanger:
#     def change_title(self, page: Page):
#         page.title = "EZ Web - Blah"


# @ez.on(TreeRenderer.WillRender)
# def update_title(page: ...):
#     page.title = "EZ Web - Blah"


@ez.site.get("/title")
def index():
    print("Hello, World!")
    return "<h1>Hello, World!</h1>"


@ez.site.get("/api/plugins/{plugin_id}/enable")
def enable_plugin(plugin_id: str):
    print(f"Enabling plugin {plugin_id}...")
    ez.plugins.enable_plugin(plugin_id)
    return "Plugin enabled!"


@ez.site.get("/api/plugins/{plugin_id}/disable")
def disable_plugin(plugin_id: str):
    print(f"Disabling plugin {plugin_id}...")
    ez.plugins.disable_plugin(plugin_id)
    return "Plugin disabled!"


@ez.site.get("/api/plugins")
def get_plugins():
    print("Getting plugins...")
    return [
        plugin.info.model_dump() for plugin in ez.plugins.get_plugins()
    ]


@ez.site.get("/exc/{exc_type}")
def raise_exc(exc_type: str):
    raise {
        "ValueError": ValueError,
        "TypeError": TypeError,
        "KeyError": KeyError,
        "ZeroDivisionError": ZeroDivisionError,
        "AttributeError": AttributeError,
        "NameError": NameError,
        "SyntaxError": SyntaxError,
        "ImportError": ImportError,
        "ModuleNotFoundError": ModuleNotFoundError,
        "FileNotFoundError": FileNotFoundError,
        "PermissionError": PermissionError,
        "FileExistsError": FileExistsError,
        "NotADirectoryError": NotADirectoryError,
        "IsADirectoryError": IsADirectoryError,
        "InterruptedError": InterruptedError,
        "PermissionError": PermissionError,
        "ProcessLookupError": ProcessLookupError,
        "TimeoutError": TimeoutError,
        "OSError": OSError,
        "BlockingIOError": BlockingIOError,
        "ChildProcessError": ChildProcessError,
        "ConnectionError": ConnectionError,
        "BrokenPipeError": BrokenPipeError,
        "ConnectionAbortedError": ConnectionAbortedError,
        "ConnectionRefusedError": ConnectionRefusedError,
        "ConnectionResetError": ConnectionResetError,
        "FileExistsError": FileExistsError,
        "FileNotFoundError": FileNotFoundError,
        "InterruptedError": InterruptedError,
        "IsADirectoryError": IsADirectoryError,
        "NotADirectoryError": NotADirectoryError,
        "PermissionError": PermissionError,
        "ProcessLookupError": ProcessLookupError,
        "TimeoutError": TimeoutError,
        "TypeError": TypeError,
        "ValueError": ValueError,
        "ZeroDivisionError": ZeroDivisionError,
        "KeyError": KeyError,
        "AttributeError": AttributeError,
        "NameError": NameError,
        "SyntaxError": SyntaxError,
        "ImportError": ImportError,
        "ModuleNotFoundError": ModuleNotFoundError,
        "FileNotFoundError": FileNotFoundError,
        "PermissionError": PermissionError,
        "FileExistsError": FileExistsError,
        "NotADirectoryError": NotADirectoryError,
        "IsADirectoryError": IsADirectoryError,
        "InterruptedError": InterruptedError,
        "PermissionError": PermissionError,
        "ProcessLookupError": ProcessLookupError,
        "TimeoutError": TimeoutError,
        "OSError": OSError,
        "BlockingIOError": BlockingIOError,
        "ChildProcessError": ChildProcessError,
        "ConnectionError": ConnectionError,
    }[exc_type]("This is a test exception!")


@ez.events.on("test")
def test_event(data):
    print(f"Test event: {data}")
    print(ez.lowlevel.APP_HOST.current_application.oid)


def main():
    from . import test

    test.run()


# try:
#     ez.install_plugin("D:\\xpodev\\ez-web-src\\tests\\plugins\\test-plugin.zip")
# except FileExistsError:
#     ...
