from sys import argv

from pydantic import BaseModel
from tpt import two_plus_two


class Greeting(BaseModel):
    audience: str


def pop_argv_with_default(default: str) -> str:
    return argv[-1] if len(argv) > 1 else default


def greet() -> str:
    greeting = Greeting(audience=pop_argv_with_default(default="world"))
    return f"Hello {greeting.audience} from workspaces!"


def add_two_plus_two() -> str:
    return f"Two plus two is {two_plus_two()}"
