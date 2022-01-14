import re


def validate_name(name):

    if not len(name) > 0 or not len(name) <= 7:
        print(f"Maximum 7 Characters! Please try again.")
    elif re.match(r"^[0-9a-zA-Z,.!?\/\"']-", name):
        print(f"Contains a non-supported character!")
    else:

        return True


def validate_gender(gender):

    if gender.casefold() in {"boy", "girl"}:

        return True
    else:
        print("Please enter a valid response! 'boy' or 'girl'")


def validate_stater(response):

    if response.casefold() in {"custom", "optimal"}:

        return True
    else:
        print("Please enter a valid response! 'custom' or 'optimal'")


def validate_starter_selection(starter):

    if starter.casefold() in {"1", "2", "3"}:

        return True
    else:
        print("Please enter a valid response! '1', '2', '3' ")


def starter_number_to_name(selection):
    if selection == '1':
        selection = 'Treecko'
        return selection
    elif selection == '2':
        selection = "Torchic"
        return selection
    elif selection == '3':
        selection = "Mudkip"
        return selection


def validate_real_time_clock(response):

    if response.casefold() in {"y", "n"}:

        return True
    else:
        print("Please enter a valid response! (Y/N) ")
