import pytest

ZERO = "零"
DIGITS = [""] + list("一二三四五六七八九")
DIGITS_WITHOUT_ONE = ["", ""] + list("二三四五六七八九")
TEN = "十"
HUNDRED = "百"


def number_to_text(number: int) -> str:
    assert number >= 0, "Negative numbers are not supported"
    assert number <= 999, "Numbers greater than 999 are not supported (yet)"
    if number == 0:
        return ZERO

    result = ""

    hundreds, remainder = divmod(number, 100)

    if hundreds:
        result += DIGITS[hundreds] + HUNDRED

    if remainder < 10:
        result += DIGITS[remainder]
    else:
        tens, units = divmod(remainder, 10)
        result += DIGITS_WITHOUT_ONE[tens] + TEN + DIGITS[units]

    return result


@pytest.mark.parametrize(
    "number, expected",
    [
        (0, "零"),
        (1, "一"),
        (10, "十"),
        (11, "十一"),
        (12, "十二"),
        (20, "二十"),
        (21, "二十一"),
        (99, "九十九"),
        (100, "一百"),
        (123, "一百二十三"),
        (999, "九百九十九"),
    ],
)
def test_number_to_text(number: int, expected: str) -> None:
    assert number_to_text(number) == expected
