__all__ = ("make_text_bold",)


def make_text_bold(text) -> str:
    """Coerce input `text` to string and wrap in asterisks."""
    return f"**{text}**"
