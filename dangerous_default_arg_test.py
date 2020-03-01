"""Module Docstring."""
import os


def some_func(arg1, arg2, arg3=[1, 2, 3], arg4=None, arg5={1,2}):
    """
    Some docstring to ensure docstring stay at its position
    """
    print("I am a function!")

    def some_other_func(arg=[1,2,3]):
        """Nested function to ensure indentation doesn't get messed up"""

        def another_nested_function(danger=[]):
            """Another deeply nested function."""
            return danger

        return arg

    # Returning
    return (arg1, arg2, arg3, arg4)
