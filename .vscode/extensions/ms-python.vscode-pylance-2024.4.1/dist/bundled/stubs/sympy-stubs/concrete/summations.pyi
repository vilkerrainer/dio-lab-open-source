from typing import Any, Self, Tuple as tTuple
from sympy.concrete.expr_with_intlimits import ExprWithIntLimits
from sympy.concrete.expr_with_limits import AddWithLimits
from sympy.core.basic import Basic
from sympy.core.expr import Expr
from sympy.core.relational import Equality, Ne, Relational
from sympy.core.symbol import Symbol
from sympy.functions.elementary.piecewise import Piecewise
from sympy.series.order import Order

class Sum(AddWithLimits, ExprWithIntLimits):
    __slots__ = ...
    limits: tTuple[tTuple[Symbol, Expr, Expr]]
    def __new__(cls, function, *symbols, **assumptions) -> Equality | Relational | Ne | Self:
        ...
    
    def doit(self, **hints) -> tuple[Any, ...] | Self | Order | Any | Piecewise | Basic | Equality | Relational | Ne | Sum | None:
        ...
    
    def eval_zeta_function(self, f, limits) -> Piecewise | None:
        ...
    
    def is_convergent(self):
        ...
    
    def is_absolutely_convergent(self):
        ...
    
    def euler_maclaurin(self, m=..., n=..., eps=..., eval_integral=...) -> tuple[Any, Any] | tuple[Any | Basic, Any] | tuple[Any | Order | Basic, Any] | tuple[Any, int]:
        ...
    
    def reverse_order(self, *indices) -> Sum:
        ...
    


def summation(f, *symbols, **kwargs) -> Equality | Relational | Ne:
    ...

def telescopic_direct(L, R, n, limits) -> Order:
    ...

def telescopic(L, R, limits) -> Order | None:
    ...

def eval_sum(f, limits) -> Piecewise | Equality | Relational | Ne | Basic | Sum | Order | None:
    ...

def eval_sum_direct(expr, limits) -> Order:
    ...

def eval_sum_symbolic(f, limits):
    ...

def eval_sum_hyper(f, i_a_b) -> Piecewise | None:
    ...

def eval_sum_residue(f, i_a_b):
    ...

