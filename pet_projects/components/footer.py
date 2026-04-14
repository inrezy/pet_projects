import reflex as rx


def footer() -> rx.Component:
    return rx.flex(
        rx.text(
            "yeah, you're on the best website which contains unique pet projects haha",
            as_='span',
            color_scheme='gray'
        ),
        justify='center'
    )