import reflex as rx

from ...templates import template

from ...states import CounterState


@template(route="/fun/counter", title="Counter")
def counter() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.card(
                rx.text(
                    CounterState.count,
                    size='9',
                    weight='medium',
                    align='center'
                ),
                width='100%'
            ),
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.input(
                            on_change=CounterState.set_first_value,
                            value=CounterState.first_value
                        ),
                        rx.button(
                            "Decrement",
                            color_scheme='red',
                            on_click=lambda: CounterState.decrement(CounterState.first_value),
                            disabled=CounterState.count <= CounterState.min_limit,
                            width='100%'
                        )
                    )
                ),
                rx.card(
                    rx.vstack(
                        rx.input(
                            on_change=CounterState.set_second_value,
                            value=CounterState.second_value
                        ),
                        rx.button(
                            "Increment",
                            color_scheme='grass',
                            on_click=lambda: CounterState.increment(CounterState.second_value),
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
                        color_scheme='blue',
                        on_click=lambda: CounterState.set_count(0),
                        flex_grow='1'
                    ),
                    rx.icon_button(
                        rx.icon("repeat"),
                        color_scheme='blue',
                        on_click=CounterState.swap_values
                    )
                ),
                width='100%'
            ),
            align='center'
        ),
        rx.vstack(
            rx.hstack(
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
                            rx.text("Cooldown:", width='5.5rem'),
                            rx.input(
                                value=CounterState.negative_autoclick_cooldown,
                                on_change=CounterState.set_negative_autoclick_cooldown
                            ),
                            align='center'
                        ),
                        rx.hstack(
                            rx.text("Min. Value:", width='5.5rem'),
                            rx.input(
                                value=CounterState.negative_autoclick_min_value,
                                on_change=CounterState.set_negative_autoclick_min_value
                            ),
                            align='center'
                        ),
                        rx.hstack(
                            rx.text("Value:", width='5.5rem'),
                            rx.input(
                                value=CounterState.negative_autoclick_value,
                                on_change=CounterState.set_negative_autoclick_value
                            ),
                            align='center'
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
                            rx.text("Cooldown:", width='5.5rem'),
                            rx.input(
                                value=CounterState.positive_autoclick_cooldown,
                                on_change=CounterState.set_positive_autoclick_cooldown
                            ),
                            align='center'
                        ),
                        rx.hstack(
                            rx.text("Max. Value:", width='5.5rem'),
                            rx.input(
                                value=CounterState.positive_autoclick_max_value,
                                on_change=CounterState.set_positive_autoclick_max_value
                            ),
                            align='center'
                        ),
                        rx.hstack(
                            rx.text("Value:", width='5.5rem'),
                            rx.input(
                                value=CounterState.positive_autoclick_value,
                                on_change=CounterState.set_positive_autoclick_value
                            ),
                            align='center'
                        )
                    )
                )
            ),
            rx.hstack(
                rx.card(
                    rx.vstack(
                        rx.text("Randomizator", weight='medium'),
                        rx.divider(),
                        rx.vstack(
                            rx.hstack(
                                rx.text("Min. Value:", width='5.5rem'),
                                rx.input(
                                    value=CounterState.random_min_value,
                                    on_change=CounterState.set_random_min_value
                                ),
                                align='center'
                            ),
                            rx.hstack(
                                rx.text("Max. Value:", width='5.5rem'),
                                rx.input(
                                    value=CounterState.random_max_value,
                                    on_change=CounterState.set_random_max_value
                                ),
                                align='center'
                            ),
                            rx.button(
                                "Randomize",
                                color_scheme='blue',
                                on_click=lambda: CounterState.randomize_values(CounterState.random_min_value, CounterState.random_max_value),
                                width='100%'
                            )
                        ),
                        align='center'
                    )
                ),
                rx.card(
                    rx.vstack(
                        rx.text("Other", weight='medium'),
                        rx.divider(),
                        rx.vstack(
                            rx.hstack(
                                rx.text("Min. Limit:", width='5.5rem'),
                                rx.input(
                                    value=CounterState.min_limit,
                                    on_change=CounterState.set_min_limit
                                ),
                                align='center'
                            ),
                            rx.hstack(
                                rx.text("Max. Limit:", width='5.5rem'),
                                rx.input(
                                    value=CounterState.max_limit,
                                    on_change=CounterState.set_max_limit
                                ),
                                align='center'
                            )
                        ),
                        align='center'
                    )
                )
            )
        ),
        justify='center'
    )
