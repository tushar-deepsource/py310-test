import os
import sys

def something(x):
    print(x)

def something_else(y):
    print(y)
    print(os)

__all__ = [
    something,
    something_else,
    "bleh",
]

print("x")
from __future__ import print_function
