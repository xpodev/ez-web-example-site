from pyx.html import Head, Link, Title,Script
from pyx.components import Component


class Header(Component):
    def __init__(self, title="") -> None:
        self.title = title

    def render(self):
        return Head(
            Link(
                rel="stylesheet",
                href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css",
            ),
            Link(
                rel="icon",
                href="/static/icon-bg.svg",
                type="image/svg+xml",
            ),
            Script(
                src="https://unpkg.com/react@18/umd/react.production.min.js",
                crossorigin=True
            ),
            Script(
                src="https://unpkg.com/react-dom@18/umd/react-dom.production.min.js",
                crossorigin=True
            ),
            Script(
                src="https://cdn.socket.io/4.7.4/socket.io.min.js",
                crossorigin=True
            ),
            Script(
                src="/static/js/ez.js",
                defer=True
            ),
            Title(self.title),
        )
