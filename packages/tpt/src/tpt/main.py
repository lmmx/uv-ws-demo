from bolded import make_text_bold
from word2number.w2n import word_to_num


def two_plus_two() -> str:
    """Doing two plus two in a dumb way."""
    two = word_to_num("two")
    four = two + two
    return make_text_bold(four)
