import stackfull
from stackfull import (push, pop, dup,
                       clear, roll, retr,
                       stack, popclear, cleartomark,
                       MARK, push_if_true, discard_if_false,
                       window)
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
        for i in range(999, -1, -1):
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
        roll(2, 1)
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
        self.assertEqual([42, 42, 42], stack())

    def test_popclear_works(self):
        push(42)
        push(23)
        self.assertEqual(23, popclear())
        try:
            pop()
        except IndexError:
            pass
        else:
            assert False, "Stack should be empty, popped a value instead."

    def test_cleartomark_works(self):
        push(23)
        push(MARK)
        push(42)
        push(42)
        self.assertEqual(23, cleartomark())

    def test_stack_is_isolated_in_function_contexts(self):
        push(42)

        def helper():
            push(20)
            self.assertEqual(20, pop())
            try:
                pop()
            except IndexError:
                pass
            else:
                assert False, "Stack should be empty - pop returned a value instead"

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

    def test_push_if_true(self):
        results = [(pop(), len(stack())) for i in range(10) if push_if_true(i % 2)]
        assert all(result[1] == 0 for result in results)
        assert len(results) == 5

    def test_discard_if_false(self):
        results = [(pop(), len(stack())) for i in range(10) if discard_if_false(push(i) % 2)]
        assert all(result[1] == 0 for result in results)
        assert len(results) == 5
        assert [result[0] for result in results] == list(range(1, 10, 2))

    def test_window_function(self):
        assert [push(stack()[-2] +  stack()[-1]) for i in window(range(2,12), 0,1)] == [1, 2, 3, 5, 8, 13, 21, 34, 55, 89]


if __name__ == "__main__":
    unittest.main()
