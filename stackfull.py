# coding: utf-8
# author: João S. O. Bueno
"""
Stack expression utilities


TODO: create a decorator which trasnform the operations here
in real operations in the VM stack,
by modifying the bytecode in calls to these utility functions
"""
from inspect import currentframe
from collections import deque

SN = ".stackfull"

#
# All functions return the last value on the stack
#
def push(value):
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    stack.append(value)
    return value

def pop():
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    return stack.pop()

def retr():
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    return stack[-1]

def dup():
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    value = stack[-1]
    stack.append(value)
    return value

def stack():
    return currentframe().f_back.f_locals.setdefault(SN, [])

def roll(items, ammount):
    stack = currentframe().f_back.f_locals.setdefault(SN, [])
    top = stack[-items:]
    top.rotate(ammount)
    stack[-items:] = top
    return stack[-1]

    
    
def clear():
    currentframe().f_back.f_locals[SN] = []
