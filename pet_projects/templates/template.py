from typing import Callable

import reflex as rx

from ..components import navbar, footer


default_meta = [
    {
        "name": "viewport",
        "content": "width=device-width, shrink-to-fit=no, initial-scale=1"
    }
]

def template(
    route: str | None = None,
    title: str | None = None,
    description: str | None = None,
    meta: str | None = None,
    script_tags: list[rx.Component] | None = None,
    on_load: rx.event.EventType[()] | None = None
) -> Callable[[Callable[[], rx.Component]], rx.Component]:
    def decorator(page_content: Callable[[], rx.Component]) -> rx.Component:
        all_meta = [*default_meta, *(meta or [])]

        def templated_page():
            return rx.box(
                rx.flex(
                    rx.container(
                        navbar(),
                        size='4',
                        flex_grow='0',
                        padding='20px'
                    ),
                    rx.container(
                        page_content(),
                        size='4',
                        flex_grow='1',
                        padding='20px',
                        style={
                            "justify-content": 'center'
                        }
                    ),
                    rx.container(
                        footer(),
                        size='4',
                        flex_grow='0',
                        padding='20px'
                    ),
                    flex_direction='column',
                    height='inherit'
                ),
                height='100vh'
            )
        
        @rx.page(
            route=route,
            title=f"PPC | {title}",
            description=description,
            meta=all_meta,
            script_tags=script_tags,
            on_load=on_load
        )
        def theme_wrap():
            return rx.theme(
                templated_page(),
                has_background=True,
                accent_color='iris',
                gray_color='gray',
                radius='medium',
                scaling='100%'
            )
        
        return theme_wrap
    
    return decorator