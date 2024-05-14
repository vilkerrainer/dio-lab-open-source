from typing import Callable

class Substitution:
    def __init__(self, *args, **kwargs) -> None: ...
    def __call__(self, func: Callable) -> Callable: ...
    def update(self, *args, **kwargs) -> None: ...

class _ArtistKwdocLoader(dict):
    def __missing__(self, key: str) -> str: ...

class _ArtistPropertiesSubstitution(Substitution):
    def __init__(self) -> None: ...
    def __call__(self, obj: Callable) -> Callable: ...

def copy(source: Callable) -> Callable: ...

dedent_interpd: _ArtistPropertiesSubstitution = ...
interpd: _ArtistPropertiesSubstitution = ...
