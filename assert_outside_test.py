# inside a func def
def some_function(args):
    """Docstring."""
    assert 1  > 2, (
        "Some message"
    )

    if args != []:
        raise AssertionError

some_function('123')


#Comment
assert {} is not []
