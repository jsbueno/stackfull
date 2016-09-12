PYTHON STACKFULL
================

This small utility package provides functions to be used
inside Python expressions that provide functionality
like that available in stack-based languages
(such as forth and postscript).

It registers a hidden variable in the current
running frame, which is a plain Python list -
calls to plain "push, pop, dup, retr", etc...
will just push/recover elements from that list.

The intent is that whenever in an expression
a value is complicated to retrieve - (or 
computationally extensive) - instead of
having to retrieve it in a previous line
and storing said value in a variable,
one gets the ability to "push" the value
in this implicit stack - and retrieve it
in another part of the same expression::
     
     `result = pop().upper() if not push(get_my+expensive_value()).isdigit() else pop()`

For convenience, most functions return the valued passed
to them in the first place (like the push above).

Avalilable functions:

clear
_____

    Clears the stack


cleartomark
___________

    Clears the stack up to the special sentinel value
    MARK - this allows for clean-up of the stack after
    a block of code, preserving the older values.
    If the stack is not empty, returns the last value on the
    stack non destructively, else, MARK itself is returned.


discard_if_false
________________

    Removes the last value in the stack if the expression is false.
    Made to be used in comprehensions, in the if part:

    Ex.:
    [pop().name for image in values if pop_if_false(push(image) is not None)]



dup
___

    Dplicates the last value on the stack
    It also returns the value duplicated in a non-destructive way


pop
___

    Pops the last value from the stack


popclear
________

    Pops the last value from the stack, and clears the stack.
    This allows stackfull to be used inside generator expressions
    and comprehensions, using a 'push' in the filtering expression,
    and 'popclear' on the result expression.


push
____

    Pushes a value into the stack, and returns the value itself
    Along with 'pop' and 'popclear' this is the heart of
    stackfull - as it allows an expensive function to be used
    in a 'if' or 'while' test, and still have its value
    available to use inside the defined block - without
    the need of an explicit auxiliar variable


push_if_true
____________

    Returns the value itself, and Pushes a value into the stack, if it
    is truthy. Otherwise does not touch the stack.
    Nice to use inside  comprehensions
    in the "if" part: if the expession is not True, it is never pushed, and
    extraneous values don't pile up on the stack.

    Ex.:
    [pop().name for image in values if push_if_true(image)]



retr
____

    Peeks the last value on the stack without consuming it


roll
____

    Rolls the last 'items' values on the stack by
    'amount' positions, changing their order.
    Returns the value on the top of the stack after
    the changes in a non destructive way.


stack
_____

    Retrieves the stack as an ordinary Python list
    (which it actually is), allowing one to perform
    extra desired operations, such as 'len' or 'insert'

