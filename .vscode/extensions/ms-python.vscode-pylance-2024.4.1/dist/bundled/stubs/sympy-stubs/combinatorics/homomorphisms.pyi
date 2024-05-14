from typing import Any, Literal
from sympy.combinatorics.fp_groups import FpSubgroup
from sympy.combinatorics.perm_groups import PermutationGroup
class GroupHomomorphism:
    def __init__(self, domain, codomain, images) -> None:
        ...
    
    def invert(self, g) -> list[Any] | None:
        ...
    
    def kernel(self) -> PermutationGroup | FpSubgroup:
        ...
    
    def image(self) -> PermutationGroup | FpSubgroup:
        ...
    
    def __call__(self, elem) -> list[Any]:
        ...
    
    def is_injective(self) -> bool:
        ...
    
    def is_surjective(self) -> None:
        ...
    
    def is_isomorphism(self) -> Literal[False] | None:
        ...
    
    def is_trivial(self) -> bool:
        ...
    
    def compose(self, other) -> GroupHomomorphism:
        ...
    
    def restrict_to(self, H) -> GroupHomomorphism:
        ...
    
    def invert_subgroup(self, H) -> PermutationGroup:
        ...
    


def homomorphism(domain, codomain, gens, images=..., check=...) -> GroupHomomorphism:
    ...

def orbit_homomorphism(group, omega) -> GroupHomomorphism:
    ...

def block_homomorphism(group, blocks) -> GroupHomomorphism:
    ...

def group_isomorphism(G, H, isomorphism=...) -> tuple[Literal[True], GroupHomomorphism] | tuple[Literal[False], None] | bool:
    ...

def is_isomorphic(G, H) -> tuple[Literal[True], GroupHomomorphism] | tuple[Literal[False], None] | bool:
    ...

