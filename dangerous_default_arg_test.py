"""Module Docstring."""
import os


def some_func(arg1, arg2, arg3=None, arg4=None, arg5=None):
    """
    Some docstring to ensure docstring stay at its position
    """
    if arg3 is None:
        arg3 = [1, 2, 3]
    if arg5 is None:
        arg5 = {1,2}
    print("I am a function!")

    def some_other_func(arg=None):
        """Nested function to ensure indentation doesn't get messed up"""
        if arg is None:
            arg = [1,2,3]

        x = [1,2,3]; y={1, 2, 3}; z={'a': 1, 'b': 2}; t=(1, 2, 3)
        def another_nested_function(danger_one=None, danger_two=None, danger_three=None, xyz=None, safe_four=t):
            """Another deeply nested function."""
            if danger_one is None:
                danger_one = x
            if danger_two is None:
                danger_two = y
            if danger_three is None:
                danger_three = z
            return

        return arg

    # Returning
    return (arg1, arg2, arg3, arg4)
