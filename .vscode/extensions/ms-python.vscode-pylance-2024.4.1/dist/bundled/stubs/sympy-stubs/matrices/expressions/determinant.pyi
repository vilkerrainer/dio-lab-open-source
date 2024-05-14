from typing import Self
from sympy.core.basic import Basic
from sympy.core.expr import Expr

class Determinant(Expr):
    is_commutative = ...
    def __new__(cls, mat) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    @property
    def kind(self):
        ...
    
    def doit(self, expand=..., **hints) -> Self:
        ...
    


def det(matexpr) -> Determinant:
    ...

class Permanent(Expr):
    def __new__(cls, mat) -> Self:
        ...
    
    @property
    def arg(self) -> Basic:
        ...
    
    def doit(self, expand=..., **hints) -> Self:
        ...
    


def per(matexpr) -> Permanent:
    ...

def refine_Determinant(expr, assumptions):
    ...

