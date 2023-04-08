class Duck:
    def __init__(self):
        ...

    def __getattr__(self, attr: str):
        if attr == "quack":
            return lambda: print("quack")
        elif attr == "swim":
            return lambda: print("splash")
        else:
            raise AttributeError


e = 1

duck = Duck()
duck.quack()
duck.fly()


class Pikachu:
    def __init__(self, tail_length_cm: int):
        self.tail_length_cm = tail_length_cm

    @classmethod
    def from_tail_length_meters(
        cls: Type["Pikachu"],
        tail_length_meters: int,
    ) -> "Pikachu":
        tail_length_cm = tail_length_meters * 100
        return cls(tail_length_cm=tail_length_cm)


def consume_many_types(
    num: int,
    decimal: float,
    boolean: bool,
    string: str,
    binary: bytes,
    obj: object,
) -> None:
    ...


from typing import (
    Dict,
    List,
    Optional,
    Set,
    Tuple,
    Union,
)

nums: List[int] = []
three_dimensional_vector: Tuple[int, float, str] = (1, 2.0, "hi")
n_dimensional_vector: Tuple[float, ...] = 1, 2, 3, 4, 5
students_to_ages: Dict[str, int] = {
    "bobby": 25,
    "murph": 27,
    "alice": 21,
}
fruits: Set[str] = {"apple", "kiwi", "banana"}


class Animal:
    ...


miscellaneous_values: List[Union[int, float, str, Type]] = [
    1,
    1.0,
    "hi",
    object,
    "hi",
    2.0,
    1,
]
x: Optional[int] = None


def greet(name: Optional[str]):
    if not name:
        print("Hello!")
        return
    print(f"Hello, {name}!")
