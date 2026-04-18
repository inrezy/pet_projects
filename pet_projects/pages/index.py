import reflex as rx

from ..templates import general_template


@general_template(route="/", title="Index Page")
def index() -> rx.Component:
    return rx.vstack(
        rx.text(
            "Hi! Welcome to Pet Projects Collection website.",
            size='8',
            weight='medium'
        ),
        rx.text(
            "This website contains some interesting pet projects (I think), so enjoy lol.",
            size='6',
            weight='light'
        ),
        align='center'
    )