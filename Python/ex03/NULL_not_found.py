from typing import Any


def NULL_not_found(object: Any) -> int:
    """Identifies and prints different Python null-like values along with
    their corresponding type, returning 0 if recognized and 1 otherwise.
    """
    obj_type = type(object)

    if object is None:
        print(f"Nothing: {object} {obj_type}")
    # NaN check: In IEEE 754 float standard, NaN is the ONLY value where x != x
    elif obj_type is float and object != object:
        print(f"Cheese: {object} {obj_type}")
    elif obj_type is bool and object is False:
        print(f"Fake: {object} {obj_type}")
    elif obj_type is int and object == 0:
        print(f"Zero: {object} {obj_type}")
    elif obj_type is str and object == "":
        print(f"Empty: {object} {obj_type}")
    else:
        print("Type not Found")
        return 1

    return 0
