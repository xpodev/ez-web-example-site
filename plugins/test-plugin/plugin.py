import ez

# from ezplugins import test_plugin

# test_plugin.my_api(1, "2")


@ez.get("/test")
def test():
    return "This is a test plugin"


class MyAPI:
    def my_api(self, x: int, y: str) -> bool:
        return x > y


__api__ = MyAPI()
