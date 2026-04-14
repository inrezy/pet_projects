import reflex as rx

from ..templates import template


@template(route="/", title="Index Page")
def index() -> rx.Component:
    return rx.flex(
        rx.text("sex porno"),
        justify='center'
    )