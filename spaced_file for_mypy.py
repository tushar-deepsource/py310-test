import functools


class C:
    @functools.cached_property
    def addr(self):
        return "asdf"

    @property
    def another(self):
        return "ddpjd"
    
    def not_a_property(self):
        return "dnvpmPkmv"


# These are fine.
C().addr == "asdf"
C().another == "dhoj"

# This is not
C().not_a_property == "something"
