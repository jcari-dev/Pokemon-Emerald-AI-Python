import re


def validate_name(name):
    valid = False
    if not len(name) > 0 or not len(name) <= 7:
        print(f"Maximum 7 Characters! Please try again.")
    elif re.match(r"^[0-9a-zA-Z,.!?\/\"']-*$", name):
        print(f"Contains a non-supported character!")
    else:
        valid = True
        return True


def validate_gender(gender):
    valid = False
    if gender.casefold() in {"boy", "girl"}:
        valid = True
        return True
    else:
        print("Please enter a valid response! 'boy' or 'girl'")


def validate_stater(response):
    valid = False
    if response.casefold() in {"custom", "optimal"}:
        valid = True
        return True
    else:
        print("Please enter a valid response! 'custom' or 'optimal'")


def validate_starter_selection(starter):
    valid = False
    if starter.casefold() in {"1", "2", "3"}:
        valid = True
        return True
    else:
        print("Please enter a valid response! '1', '2', '3' ")
