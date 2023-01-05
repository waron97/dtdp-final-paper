from typing import Any, Iterable, Callable, TypeVar, Generic

X = TypeVar("X")


def find_index(fn: Callable[[X], bool], iterable: Iterable[X]) -> int:
    for i, x in enumerate(iterable):
        if fn(x):
            return i
    return -1


def find(fn: Callable[[X], bool], iterable: Iterable[X]) -> X | None:
    for i, x in enumerate(iterable):
        if fn(x):
            return x
    return None
