import ez

from sandbox.host import AppHost
from sandbox.applications import Application
# from ezplugins import test_plugin

# test_plugin.my_api(1, "2")

class MyApp(Application):
    def __init__(self, host):
        ...


@ez.site.get("/test")
def test():
    ez.events.emit("test", "test")
    return "This is a test plugin"


@ez.site.get("/app")
def app():
    return {
        "current_app": AppHost.current_host.current_application.oid,
    }


class MyAPI:
    def my_api(self, x: int, y: int) -> bool:
        return x > y


__api__ = MyAPI()
