import reflex as rx

from ...templates import general_template

from ...states import CounterState


@general_template(route="/fun/counter", title="Counter")
def counter() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.card(
                rx.center(
                    rx.text(
                        CounterState.count,
                        size='9',
                        weight='medium'
                    ),
                    height='100%'
                ),
                width='100%',
                flex_grow='1'
            ),
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.input(
                            value=CounterState.first_value,
                            type='number',
                            on_change=CounterState.set_first_value
                        ),
                        rx.button(
                            "Decrement",
                            color_scheme='red',
                            on_click=lambda: CounterState.set_count(CounterState.count - CounterState.first_value),
                            disabled=CounterState.count <= CounterState.min_limit,
                            width='100%'
                        )
                    )
                ),
                rx.card(
                    rx.vstack(
                        rx.input(
                            value=CounterState.second_value,
                            type='number',
                            on_change=CounterState.set_second_value
                        ),
                        rx.button(
                            "Increment",
                            color_scheme='grass',
                            on_click=lambda: CounterState.set_count(CounterState.count + CounterState.second_value),
                            disabled=CounterState.count >= CounterState.max_limit,
                            width='100%'
                        )
                    )
                )
            ),
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.button(
                            "Double",
                            color_scheme='bronze',
                            on_click=lambda: CounterState.set_count(CounterState.count * 2),
                            flex_grow='1'
                        ),
                        rx.button(
                            "Triple",
                            color_scheme='bronze',
                            on_click=lambda: CounterState.set_count(CounterState.count * 3),
                            flex_grow='1'
                        ),
                        rx.button(
                            "Halve",
                            color_scheme='bronze',
                            on_click=lambda: CounterState.set_count(CounterState.count / 2),
                            flex_grow='1'
                        ),
                        width='100%'
                    ),
                    rx.hstack(
                        rx.button(
                            "Square",
                            color_scheme='bronze',
                            on_click=lambda: CounterState.set_count(CounterState.count * CounterState.count),
                            flex_grow='1'
                        ),
                        rx.button(
                            "Sqrt",
                            color_scheme='bronze',
                            on_click=lambda: CounterState.set_count(CounterState.count ** (1/2)),
                            flex_grow='1'
                        ),
                        width='100%'
                    )
                ),
                width='100%'
            ),
            rx.card(
                rx.hstack(
                    rx.button(
                        "Clear",
                        on_click=lambda: CounterState.set_count(0),
                        flex_grow='1'
                    ),
                    rx.tooltip(
                        rx.icon_button(
                            rx.icon("repeat"),
                            on_click=CounterState.swap_values
                        ),
                        content="Swap Values"
                    )
                ),
                width='100%'
            ),
            align='center',
            height='inherit'
        ),
        rx.grid(
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.switch(
                            checked=CounterState.negative_autoclick_switched,
                            on_change=CounterState.switch_negative_autoclick
                        ),
                        rx.text("Negative Auto-Click", weight='medium'),
                        width='100%',
                        justify='center',
                        align='center'
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Cooldown (s):"),
                        rx.input(
                            value=CounterState.negative_autoclick_cooldown,
                            type='number',
                            on_change=CounterState.set_negative_autoclick_cooldown
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.hstack(
                        rx.text("Min. Value:"),
                        rx.input(
                            value=CounterState.negative_autoclick_min_value,
                            type='number',
                            on_change=CounterState.set_negative_autoclick_min_value
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.hstack(
                        rx.text("Value:"),
                        rx.input(
                            value=CounterState.negative_autoclick_value,
                            type='number',
                            on_change=CounterState.set_negative_autoclick_value
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    )
                )
            ),
            rx.card(
                rx.vstack(
                    rx.hstack(
                        rx.switch(
                            checked=CounterState.positive_autoclick_switched,
                            on_change=CounterState.switch_positive_autoclick
                        ),
                        rx.text("Positive Auto-Click", weight='medium'),
                        width='100%',
                        justify='center',
                        align='center'
                    ),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Cooldown (s):"),
                        rx.input(
                            value=CounterState.positive_autoclick_cooldown,
                            type='number',
                            on_change=CounterState.set_positive_autoclick_cooldown
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.hstack(
                        rx.text("Max. Value:"),
                        rx.input(
                            value=CounterState.positive_autoclick_max_value,
                            type='number',
                            on_change=CounterState.set_positive_autoclick_max_value
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.hstack(
                        rx.text("Value:"),
                        rx.input(
                            value=CounterState.positive_autoclick_value,
                            type='number',
                            on_change=CounterState.set_positive_autoclick_value
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    )
                )
            ),
            rx.card(
                rx.vstack(
                    rx.text("Randomizator", weight='medium'),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Min. Value:"),
                        rx.input(
                            value=CounterState.random_min_value,
                            type='number',
                            on_change=CounterState.set_random_min_value
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.hstack(
                        rx.text("Max. Value:"),
                        rx.input(
                            value=CounterState.random_max_value,
                            type='number',
                            on_change=CounterState.set_random_max_value
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.button(
                        "Randomize",
                        on_click=lambda: CounterState.randomize_values(CounterState.random_min_value, CounterState.random_max_value),
                        width='100%'
                    ),
                    align='center'
                )
            ),
            rx.card(
                rx.vstack(
                    rx.text("Other", weight='medium'),
                    rx.divider(),
                    rx.hstack(
                        rx.text("Min. Limit:"),
                        rx.input(
                            value=CounterState.min_limit,
                            type='number',
                            on_change=CounterState.set_min_limit
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    rx.hstack(
                        rx.text("Max. Limit:"),
                        rx.input(
                            value=CounterState.max_limit,
                            type='number',
                            on_change=CounterState.set_max_limit
                        ),
                        width='100%',
                        align='center',
                        justify='between'
                    ),
                    align='center'
                )
            ),
            columns='2',
            spacing='3'
        ),
        justify='center',
        height='100%'
    )
