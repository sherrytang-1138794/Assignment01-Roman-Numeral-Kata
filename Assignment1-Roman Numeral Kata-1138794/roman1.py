import pytest

# convert arabic numbers to roman numerals
# convert roman numerals to arabic

roman_numeral = (("M", 1000),
                 ("CM", 900),
                 ("D", 500),
                 ("CD", 400),
                 ("C", 100),
                 ("XC", 90),
                 ("L", 50),
                 ("XL", 40),
                 ("X", 10),
                 ("V", 5),
                 ("IV", 4),
                 ("I", 1))

# Convert arabic numbers to roman numerals
# test

# test to_roman function


def test_to_roman():
    arabic = 1
    roman = "I"
    result = to_roman(arabic)
    assert roman == result

# test invalid numbers


def test_over_maximum():
    """
    the maximum of roman numeral is 3999
    to_roman should raise an ValueError when the arabic number
    entered is over 3999
    """
    with pytest.raises(ValueError):
        to_roman(4000)


def test_zero():
    """
    there's no zero in roman numeral
    to_roman should also raise an ValueError when the arabic number
    entered is 0
    """
    with pytest.raises(ValueError):
        to_roman(0)


def test_negative():
    """
    roman numeral cannot apply to negative numbers
    to_roman should also raise an ValueError when the arabic number
    entered is negtaive
    """
    with pytest.raises(ValueError):
        to_roman(-1)


def test_non_integer():
    """
    roman numeral could only apply to integers
    to_roman should raise an ValueError when the arabic number
    entered is non-integer
    """
    with pytest.raises(ValueError):
        to_roman(0.5)


def test_integer_with_floating_point():
    """
    although roman numerals only apply to integers
    1.0 should pass the test
    """
    assert to_roman(1.0) == "I"

# function that could convert arabic numbers to roman numerals


def to_roman(n):
    if not (0 < n < 4000):
        raise ValueError("Number entered should between 1 and 3999")

    if int(n) != n:
        raise ValueError("Number entered should be integer")

    result = ""
    for roman, arabic in roman_numeral:
        while n >= arabic:
            result += roman
            n -= arabic
    return result


# convert roman numerals to arabic numbers
# test

def test_to_arabic():
    roman = "M"
    arabic = 1000
    result = to_arabic(roman)
    assert arabic == result


# def test_inversible():
#     for arabic in range(1, 4000):
#         roman = to_roman(arabic)
#         result = to_arabic(roman)
#         assert result == arabic


def test_invalid_roman():
    for s in ["A", "QC", "XBI"]:
        with pytest.raises(ValueError):
            print(f"trying: {s}")
            to_arabic(s)


def test_repeat_over_three_times():
    for s in ("MMMM", "DDDD", "CCCC", "LLLL", "XXXX", "VVVV", "IIII"):
        with pytest.raises(ValueError):
            print(f"trying: {s}")
            to_arabic(s)


def test_invalid_order():
    for s in ("CMC", "DM", "VX"):
        with pytest.raises(ValueError):
            print(f"trying: {s}")
            to_arabic(s)


def test_repeat_pair():
    for s in ("CMCM", "CDCD", "XCXC", "XLXL", "IXIX", "IVIV"):
        with pytest.raises(ValueError):
            print(f"trying: {s}")
            to_arabic(s)


def valid_roman(s):

    # thousands
    for i in range(3):
        if s[:1] == "M":
            s = s[1:]

    # hundreds
    if s[:2] == "CM":  # 900
        s = s[2:]
    elif s[:2] == "CD":  # 400
        s = s[2:]
    else:
        if s[:1] == "D":  # 500
            s = s[1:]

        for i in range(3):
            if s[:1] == "C":  # 100
                s = s[1:]

    # tens
    if s[:2] == "XC":  # 90
        s = s[2:]
    elif s[:2] == "XL":  # 40
        s = s[2:]
    else:
        if s[:1] == "L":  # 50
            s = s[1:]
        for i in range(3):
            if s[:1] == "X":  # 10
                s = s[1:]

    # ones
    if s[:2] == "IX":  # 9
        s = s[2:]
    elif s[:2] == "IV":  # 4
        s = s[2:]
    else:
        if s[:1] == "V":  # 5
            s = s[1:]
        for i in range(3):
            if s[:1] == "I":  # 1
                s = s[1:]

    if s:
        return False
    else:
        return True


def to_arabic(s):
    if not valid_roman(s):
        raise ValueError(f"{s} is not a valid roman numeral.")
    result = 0
    index = 0
    for roman, arabic in roman_numeral:
        while s[index:index+len(roman)] == roman:
            result += arabic
            index += len(roman)
    return result
