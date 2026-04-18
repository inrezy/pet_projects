import reflex as rx
import random


class GuessNumberState(rx.State):
    secret: int = 0
    secret_guessed: bool = False

    min_limit: int = 1
    max_limit: int = 20

    answer: int = 0

    attempts: int = 0

    message: str = "Start guessing..."

    @rx.event
    def set_min_limit(self, value: str):
        self.min_limit = int(value)

    @rx.event
    def set_max_limit(self, value: str):
        self.max_limit = int(value)

    @rx.event
    def set_answer(self, value: str):
        self.answer = int(value)

    @rx.event
    def check_answer(self):
        match self.answer:
            case answer if answer > self.secret and (self.min_limit <= answer <= self.max_limit):
                self.message = "Too high!"

                self.attempts += 1
            case answer if answer < self.secret and (self.min_limit <= answer <= self.max_limit):
                self.message = "Too low!"

                self.attempts += 1
            case answer if not (self.min_limit <= answer <= self.max_limit):
                self.message = "Is out of bounds."
            case answer if answer == self.secret:
                self.message = "You win!"

                self.attempts += 1
                self.secret_guessed = True

    @rx.event
    def start_game(self):
        try:
            self.secret = random.randint(self.min_limit, self.max_limit)

            self.message = "Start guessing..."

            self.attempts = 0
            self.secret_guessed = False

            yield rx.toast.success("Game started!")
        except ValueError:
            yield rx.toast.error("Minimum limit shouldn't be greater than maximum limit.")