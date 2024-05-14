from _typeshed import Incomplete

def compact(text, *args, **kw): ...
def compact_empty_lines(text): ...
def concatenate(items, conjunction: str = "and", serial_comma: bool = False): ...
def dedent(text, *args, **kw): ...
def format(text, *args, **kw): ...
def generate_slug(text, delimiter: str = "-"): ...
def is_empty_line(text): ...
def join_lines(text): ...
def pluralize(count, singular, plural: Incomplete | None = None): ...
def pluralize_raw(count, singular, plural: Incomplete | None = None): ...
def random_string(length=(25, 100), characters=...): ...
def split(text, delimiter: str = ","): ...
def split_paragraphs(text): ...
def tokenize(text): ...
def trim_empty_lines(text): ...
