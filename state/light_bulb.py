# from "Arjan codes" youtube channel: https://www.youtube.com/watch?v=5OzLrbk82zY

from typing import Protocol


class LightState(Protocol):
    def switch(self, bulb) -> None: ...


class OnState:
    def switch(self, bulb) -> None:
        bulb.state = OffState()
        print("Light is off")


class OffState:
    def switch(self, bulb) -> None:
        bulb.state = OnState()
        print("Light is on")


class Bulb:
    def __init__(self) -> None:
        self.state = OnState()

    def switch(
        self,
    ) -> None:
        self.state.switch(self)
        pass


def main() -> None:
    bulb = Bulb()
    bulb.switch()
    bulb.switch()


if __name__ == "__main__":
    main()
