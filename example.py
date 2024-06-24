from __future__ import annotations

from implements import Implements

class C:
    def __init__(self, x: int) -> None:
        self.x = x
    # def __eq__(self, other: object) -> bool: ...
    def __eq__(self, other: object) -> Implements[C]: # type: ignore[override]
        if not isinstance(other, C):
            return NotImplemented
        return self.x == other.x # type: ignore

class D:
    def __init__(self, y: int) -> None:
        self.y = y
    def __eq__(self, other: object) -> Implements[C]: # type: ignore[override]
        if isinstance(other, C):
            return self.y == other.x # type: ignore
        return NotImplemented

class E:
    def __eq__(self, other: object) -> Implements[E]: # type: ignore[override]
        return NotImplemented

def main() -> int:
    print(C(1) == C(1)) # C Implements __eq__
    print(C(1) == D(1)) # C does not implements __eq__ with D but D implements __eq__ with C
    print(C(1) == E()) # type: ignore  # (need to be ignore since nor left nor right implements this __eq__)
    return 0

