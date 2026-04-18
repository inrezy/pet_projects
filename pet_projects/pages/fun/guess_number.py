import reflex as rx

from ...templates import general_template

from ...states import GuessNumberState


@general_template(route="/fun/guess_number", title="Guess Number")
def guess_number() -> rx.Component:
    return rx.hstack(
        rx.vstack(
            rx.card(
                rx.text(
                    rx.cond(
                        GuessNumberState.secret_guessed,
                        GuessNumberState.secret,
                        "?"
                    ),
                    size='9',
                    weight='medium',
                    align='center'
                ),
                width='100%'
            ),
            rx.card(
                rx.center(
                    rx.text(f"Attempts: {GuessNumberState.attempts}"),
                ),
                width='100%',
            ),
            rx.card(
                rx.vstack(
                    rx.input(
                        value=GuessNumberState.answer,
                        type='number',
                        on_change=GuessNumberState.set_answer,
                        width='100%'
                    ),
                    rx.button(
                        "Check",
                        on_click=GuessNumberState.check_answer,
                        disabled=GuessNumberState.secret_guessed,
                        width='100%'
                    )
                ),
                width='100%'
            ),
            align='center'
        ),
        rx.vstack(
            rx.card(
                rx.vstack(
                    rx.text("Range", weight='medium'),
                    rx.divider(),
                    rx.hstack(
                        rx.input(
                            value=GuessNumberState.min_limit,
                            type='number',
                            on_change=GuessNumberState.set_min_limit,
                            flex_grow='1'
                        ),
                        rx.text("and"),
                        rx.input(
                            value=GuessNumberState.max_limit,
                            type='number',
                            on_change=GuessNumberState.set_max_limit,
                            flex_grow='1'
                        ),
                        align='center'
                    ),
                    align='center'
                )
            ),
            rx.card(
                rx.center(
                    rx.text(
                        GuessNumberState.message,
                        size='8',
                        weight='medium'
                    ),
                    height='100%'
                ),
                width='100%',
                flex_grow='1'
            ),
            rx.card(
                rx.button(
                    "Start",
                    on_click=GuessNumberState.start_game,
                    width='inherit'
                ),
                width='100%'
            ),
            height='inherit',
            align='center'
        ),
        justify='center',
        height='100%'
    )