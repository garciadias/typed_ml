from dataclasses import dataclass
from typing import List


def wrong_type(number: int, text: str) -> List[str]:
    print("Got here!")
    return number * [text]


@dataclass
class InputDataclass:
    number: int
    text: str


if __name__ == "__main__":
    number: int = "3"
    text: str = 100

    dataclass_input = InputDataclass(number=number, text=text)
    print(f"Trying with {dataclass_input.number} and {dataclass_input.text}")
    print(wrong_type(dataclass_input.number, dataclass_input.text))
