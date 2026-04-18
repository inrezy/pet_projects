import reflex as rx
import random
import asyncio


class CounterState(rx.State):
    count: int = 0

    first_value: int = 0
    second_value: int = 0

    positive_autoclick_switched: bool = False
    negative_autoclick_switched: bool = False

    positive_autoclick_cooldown: int = 1
    negative_autoclick_cooldown: int = 1

    positive_autoclick_max_value: int = 0
    negative_autoclick_min_value: int = 0

    positive_autoclick_value: int = 0
    negative_autoclick_value: int = 0

    random_min_value: int = 0
    random_max_value: int = 0

    min_limit: int = -100
    max_limit: int = 100
 
    @rx.event
    def set_first_value(self, value: str):
        self.first_value = int(value)

    @rx.event
    def set_second_value(self, value: str):
        self.second_value = int(value)

    @rx.event
    def swap_values(self):
        self.first_value, self.second_value = self.second_value, self.first_value

    @rx.event
    def set_count(self, value: int):
        self.count = max(self.min_limit, min(int(value), self.max_limit))

    @rx.event(background=True)
    async def switch_positive_autoclick(self):
        async with self:
            self.positive_autoclick_switched = not (self.positive_autoclick_switched)

        while True:
            async with self:
                if self.count >= self.positive_autoclick_max_value or self.positive_autoclick_cooldown <= 0:
                    self.positive_autoclick_switched = False

                    break

            await asyncio.sleep(self.positive_autoclick_cooldown)

            async with self:
                if not self.positive_autoclick_switched:
                    break

                self.count = max(self.min_limit, min(self.count + self.positive_autoclick_value, self.max_limit))

    @rx.event(background=True)
    async def switch_negative_autoclick(self):
        async with self:
            self.negative_autoclick_switched = not (self.negative_autoclick_switched)

        while True:
            async with self:
                if self.count <= self.negative_autoclick_min_value or self.negative_autoclick_cooldown <= 0:
                    self.negative_autoclick_switched = False

                    break

            await asyncio.sleep(self.negative_autoclick_cooldown)

            async with self:
                if not self.negative_autoclick_switched:
                    break

                self.count = max(self.min_limit, min(self.count - self.negative_autoclick_value, self.max_limit))

    @rx.event
    def set_positive_autoclick_cooldown(self, value: str):
        self.positive_autoclick_cooldown = int(value)

    @rx.event
    def set_negative_autoclick_cooldown(self, value: str):
        self.negative_autoclick_cooldown = int(value)

    @rx.event
    def set_positive_autoclick_max_value(self, value: str):
        self.positive_autoclick_max_value = int(value)

    @rx.event
    def set_negative_autoclick_min_value(self, value: str):
        self.negative_autoclick_min_value = int(value)

    @rx.event
    def set_positive_autoclick_value(self, value: str):
        self.positive_autoclick_value = int(value)

    @rx.event
    def set_negative_autoclick_value(self, value: str):
        self.negative_autoclick_value = int(value)

    @rx.event
    def randomize_values(self, min_value: int, max_value: int):
        try:
            self.first_value = random.randint(min_value, max_value)
            self.second_value = random.randint(min_value, max_value)
        except ValueError:
            yield rx.toast.error("Minimum value shouldn't be greater than maximum value.")

    @rx.event
    def set_random_min_value(self, value: str):
        self.random_min_value = int(value)

    @rx.event
    def set_random_max_value(self, value: str):
        self.random_max_value = int(value)

    @rx.event
    def set_min_limit(self, value: str):
        self.min_limit = int(value)

    @rx.event
    def set_max_limit(self, value: str):
        self.max_limit = int(value)