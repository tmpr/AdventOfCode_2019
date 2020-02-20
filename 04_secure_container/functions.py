def possible_elve_passwords(your_range: range, strict=False) -> list:
    """
    Finds all possible passwords in given range that meet
    the elves criteria.

    If `strict == True`, double digits cannot also
    be tripple digits or more.
    """
    return [number for number in your_range
            if _is_valid_password(number, strict=strict)]


def _is_valid_password(number, strict=False):
    """Checks if given number could be a password."""
    number_string = str(number)

    if len(number_string) != 6:
        return False
    if sorted(number_string) != list(number_string):
        return False
    # No double digit if there are only unique digits.
    elif len(set(number_string)) == len(number_string):
        return False

    if strict:
        for digit in set(number_string):
            triple = digit * 3
            double = digit * 2
            if double in number_string and triple not in number_string:
                # Found a strict double digit!
                return True
        return False
    else:
        return True
