from typing import Any, Self, Tuple as tTuple
from sympy.concrete.expr_with_limits import AddWithLimits
from sympy.core.basic import Basic
from sympy.core.containers import Tuple
from sympy.core.expr import Expr
from sympy.core.relational import Equality, Ne, Relational
from sympy.tensor.functions import shape

class Integral(AddWithLimits):
    __slots__ = ...
    args: tTuple[Expr, Tuple]
    def __new__(cls, function, *symbols, **assumptions) -> Equality | Relational | Ne | Self:
        ...
    
    def __getnewargs__(self) -> tuple[Basic, *tuple[tuple[Any], ...]]:
        ...
    
    @property
    def free_symbols(self) -> set[Any]:
        ...
    
    def transform(self, x, u) -> Self:
        ...
    
    def doit(self, **hints):
        ...
    
    def as_sum(self, n=..., method=..., evaluate=...):
        ...
    
    def principal_value(self, **kwargs) -> Self:
        ...
    


def integrate(*args, meijerg=..., conds=..., risch=..., heurisch=..., manual=..., **kwargs) -> Equality | Relational | Ne:
    ...

def line_integrate(field, curve, vars) -> Equality | Relational | Ne:
    ...

@shape.register(Integral)
def _(expr):
    ...

