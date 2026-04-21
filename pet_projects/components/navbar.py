import reflex as rx
from reflex.style import set_color_mode, color_mode

from ..config import CATEGORIES, TOTAL_PAGES


def _menu_content() -> rx.Component:
    return [
        rx.menu.sub(
            rx.menu.sub_trigger(category['category'].upper()),
            rx.menu.sub_content(
                [
                    rx.menu.item(
                        page['name'],
                        shortcut=page['description'],
                        on_click=rx.redirect(page['href'])
                    ) for page in category['pages']
                ]
            )
        ) for category in CATEGORIES
    ]
 
def navbar() -> rx.Component:
    return rx.flex(
        rx.tooltip(
            rx.text(
                "PPC",
                size='8',
                weight='medium',
                color_scheme='iris'
            ),
            content="2026. Made by inrezy."
        ),
        rx.hstack(
            rx.button(
                "Index",
                variant='soft',
                on_click=rx.redirect("/")
            ),
            rx.button(
                "About",
                variant='soft',
                on_click=rx.redirect("/about")
            ),
            rx.menu.root(
                rx.menu.trigger(
                    rx.button("Projects", variant='soft')
                ),
                rx.menu.content(
                    _menu_content(),
                    rx.divider(
                        margin_y="var(--space-2)"
                    ),
                    rx.menu.item(
                        f"Projects: {TOTAL_PAGES}",
                        disabled=True
                    ),
                    spacing='5'
                )
            ),
            align='center'
        ),
        rx.flex(
            rx.segmented_control.root(
                rx.segmented_control.item(
                    rx.icon(tag='sun', size=20),
                    value='light',
                ),
                rx.segmented_control.item(
                    rx.icon(tag='moon', size=20),
                    value='dark',
                ),
                on_change=set_color_mode,
                variant='classic',
                radius='medium',
                value=color_mode
            ),
            align='center'
        ),
        justify='between'
    )