from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, Generic, List, NamedTuple, TypedDict, TypeVar, Union


def hi(x: str) -> str:
    return 1
    print("hi")


y: list = hi()


class Point(NamedTuple):
    x: int
    y: int


class Animal:
    ...


TFriend = TypeVar("TFriend", Animal, "Student")


@dataclass
class Student(Generic[TFriend]):
    name: str
    age: int
    position: Point
    friends: List[TFriend]


student_that_only_likes_animals: Student[int] = Student(
    name="Neville",
    age=16,
    position=Point(1, 2),
    friends=[1],
)


student = Student(
    **{  # type: ignore
        "name": "Marcy",
        "age": 25,
        "position": Point(1, 2),
        "friends": [
            Student(
                **{  # type: ignore
                    "name": "Jared",
                    "age": 25,
                    "position": Point(1, 2),
                    "friends": [],
                }
            )
        ],
    }
)

TStudentArgsDictKeys = Union[str, int, Point, List[Student]]
TStudentArgsDict = Dict[str, TStudentArgsDictKeys]

TAddableEntity = TypeVar("TAddableEntity", int, float, str, list, tuple)


def raise_exception(err: Exception):
    raise err


def make_list_of_addable_entity(
    a: TAddableEntity,
    b: TAddableEntity,
) -> List[TAddableEntity]:
    return [a, b]


def add(a: TAddableEntity, b: TAddableEntity) -> TAddableEntity:
    return a + b


add(a=1, b=1)
make_list_of_addable_entity(a=1, b=2)[0]
