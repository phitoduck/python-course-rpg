from .type_hints import Duck

duck = Duck()
duck.quack()


def add(
    a,  # type: int
    b,  # type: int
):      # type: (...) -> int
    return a + b


