# coding: utf-8
# author: João S. O. Bueno
"""
Stack expression utilities

These functions use a "hidden" variable in the calling
code frame context to hold a stack (a Python list)
with values - the simple functionality here allow one
have much of the functionality of stack
based languages, like Postscript and Forth conveninently
available to be used in any Python expression.


(MAYBE) TODO: create a decorator which transform the operations here
in real operations in the Python VM stack,
by modifying the bytecode of calls to these utility functions into
actual Python VM stack operations.
"""

from inspect import currentframe
from collections import deque

SN = ".stackfull"
MARK = object()


def push(value):
    """
    Pushes a value into the stack, and returns the value itself
    Along with 'pop' and 'popclear' this is the heart of
    stackfull - as it allows an expensive function to be used
    in a 'if' or 'while' test, and still have its value
    available to use inside the defined block - without
    the need of an explicit auxiliar variable
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    stack.append(value)
    return value


def pop():
    """
    Pops the last value from the stack
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    return stack.pop()


def popclear():
    """
    Pops the last value from the stack, and clears the stack.
    This allows stackfull to be used inside generator expressions
    and comprehensions, using a 'push' in the filtering expression,
    and 'popclear' on the result expression.
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    result = stack.pop()
    stack[:] = []
    return result


def retr():
    """
    Peeks the last value on the stack without consuming it
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    return stack[-1]


def dup():
    """
    Dplicates the last value on the stack
    It also returns the value duplicated in a non-destructive way
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    value = stack[-1]
    stack.append(value)
    return value


def stack():
    """
    Retrieves the stack as an ordinary Python list
    (which it actually is), allowing one to perform
    extra desired operations, such as 'len' or 'insert'
    """
    return currentframe().f_back.f_locals.setdefault(SN, [])


def roll(items, amount):
    """
    Rolls the last 'items' values on the stack by
    'amount' positions, changing their order.
    Returns the value on the top of the stack after
    the changes in a non destructive way.
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    top = deque(stack[-items:])
    top.rotate(amount)
    stack[-items:] = top
    return stack[-1]


def clear():
    """
    Clears the stack
    """
    currentframe().f_back.f_locals[SN][:] = []


def cleartomark():
    """
    Clears the stack up to the special sentinel value
    MARK - this allows for clean-up of the stack after
    a block of code, preserving the older values.
    If the stack is not empty, returns the last value on the
    stack non destructively, else, MARK itself is returned.
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    obj = object()
    while obj is not MARK:
        try:
            obj = stack.pop()
        except IndexError:
            pass
    if stack:
        return stack[-1]
    return MARK


def push_if_true(value):
    """
    Returns the value itself, and Pushes a value into the stack, if it
    is truthy. Otherwise does not touch the stack.
    Nice to use inside  comprehensions
    in the "if" part: if the expession is not True, it is never pushed, and
    extraneous values don't pile up on the stack.

    Ex.:
    [pop().name for image in values if push_if_true(image)]

    """
    if value:
        stack = currentframe().f_back.f_locals.setdefault(SN, [])
        stack.append(value)
    return value


def discard_if_false(value):
    """
    Removes the last value in the stack if the expression is false.
    Made to be used in comprehensions, in the if part:

    Ex.:
    [pop().name for image in values if pop_if_false(push(image) is not None)]

    """
    if not value:
        stack = currentframe().f_back.f_locals.setdefault(SN, [])
        stack.pop()
    return value


def window(iterable, *seeds):
    """Pre-populates a frame stack with the seed values,
    and then iterates over the iterable -

        This allows one to use the stack with initial values in a simple way
        in a generator-expression context - like

        `fib = [push(stack()[-2] + stack()[-1]) for i in window(range(2, 10), 1,1)]`
    """
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    for seed in seeds:
        stack.append(seed)

    yield from iterable
