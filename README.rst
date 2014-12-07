PYTHON STACKFULL
================

This small utility package provides functions to be used
inside Pythob expressions that provide functionality
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
     
     result = pop().upper() if not push(get_my+expensive_value()).isdigit() else pop()

For conveninece, most functions return the valued passed
to them in the first place (like the push above).

Possibly in the future a decorator could be provided
to modify the bytecode of calling the functions defined
in here to make use of the actual value stack running
inside the Python VM. **Then this will be fun**
