import stackfull
from stackfull import push, pop, dup, clear, roll, retr, stack
import unittest

class StackTest(unittest.TestCase):
    def test_push_resturns_value(self):
        self.assertEqual(42, push(42))
    
    def test_push_pop_works(self):
        push(42)
        self.assertEqual(42, pop())
    
    def test_push_pop_works_for_multiple_values(self):
        for i in range(0, 1000):
            push(i)
        for i in range(999,-1,-1):
            self.assertEqual(i, pop())
    
    def test_double_pop_raises_stackunderflow(self):
        push(42)
        pop()
        # TODO: specialize the exception
        self.assertRaises(IndexError, pop)
        
    def test_push_pop_works_in_if_expression(self):
        self.assertEqual(42, pop() if push(47 - 5) == 42 else 0)
        
    def test_dup_works(self):
        push(42)
        # Dup returns top of stak value:
        self.assertEqual(42, dup())
        pop()
        self.assertEqual(42, pop())
        self.assertRaises(IndexError, pop)
        
    def test_clear_Works(self):
        push(42)
        clear()
        self.assertRaises(IndexError, pop)
        
    def test_roll_works(self):
        push(42)
        push(40)
        push(38)
        roll(2,1)
        self.assertEqual(40, pop())
        self.assertEqual(38, pop())
        self.assertEqual(42, pop())
        self.assertRaises(IndexError, pop)
    
    def test_roll_works_for_larger_stacks(self):
        for i in range(10):
            push(i)
        roll(5, 3)
        self.assertEqual(6, pop())
        
    def test_retr_works(self):
        push(42)
        self.assertEqual(42, retr())
        self.assertEqual(42, pop())
        self.assertRaises(IndexError, retr)
    
    def test_stack_works(self):
        push(42)
        dup()
        dup()
        self.assertEqual([42, 42, 42] , stack())
        
    def test_stack_is_isolated_in_function_contexts(self):
        push(42)
        def helper():
            push(20)
            self.assertEqual(20, pop())
            self.assertRaises(IndexError, pop)
        helper()
        self.assertEqual(42, pop())
        
    def test_stack_is_isolated_in_generator_contexts(self):
        push(42)
        def helper():
            for i in range(50, 60):
                push(i)
                yield i
                self.assertEqual(i, pop())
        push(-1)
        for j, i in enumerate(helper()):
            self.assertEqual(j - 1, pop())
            push(j)
        self.assertEqual([42, 9], stack())
        

if __name__ == "__main__":
    unittest.main()