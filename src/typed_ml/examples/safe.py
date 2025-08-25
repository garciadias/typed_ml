from typing import List

from pydantic import BaseModel


def wrong_type(number: int, text: str) -> List[str]:
    print("Got here!")
    return number * [text]


class InputPydantic(BaseModel):
    number: int
    text: str


if __name__ == "__main__":
    number: int = "3"
    text: str = 100

    pydantic_input = InputPydantic(number=number, text=text)
    print(f"Trying with {pydantic_input.number} and {pydantic_input.text}")
    print(wrong_type(pydantic_input.number, pydantic_input.text))
