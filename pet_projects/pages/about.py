import reflex as rx

from ..templates import general_template


@general_template(route="/about", title="About")
def about() -> rx.Component:
    return rx.flex(
        rx.vstack(
            rx.hstack(
                rx.avatar(
                    src=rx.asset("author_avatar.png"),
                    size='7',
                    radius='full'
                ),
                rx.text(
                    "inrezy",
                    size='9',
                    weight='medium'
                ),
                align='center'
            ),
            rx.card(
                rx.text(
                    "This website is my creative workshop where I create and share pet projects. ",
                    "The site has open source code on GitHub, which might be useful to you. ",
                    "You can suggest ideas to me by writing to me on Telegram — perhaps I will implement them. ",
                    "I also have other projects, which are on GitHub. "
                ),
            ),
            rx.card(
                rx.hstack(
                    rx.button(
                        "GitHub",
                        variant='outline',
                        on_click=rx.redirect("https://github.com/inrezy/pet_projects")
                    ),
                    rx.button(
                        "Telegram",
                        variant='outline',
                        on_click=rx.redirect("https://t.me/inrezy")
                    )
                ),
            ),
            width='50%'
        ),
        justify='center'
    )