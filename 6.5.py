def group_by(func, iterable) -> dict:
    """
    Function to create a dictionary. The key is the result of the function on the iterable,
    and the value is list of the items that give this result.
    :param func:
    :param iterable:
    :return:dictionary of keys and list of  iterable objects.
    """
    return {func(i): list(filter(lambda word: func(word) == func(i), iterable)) for i in iterable}


if __name__ == "__main__":
    lst = ["hi", "bye", "yo", "try"]
    print(group_by(len, lst))
