#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve, findCycle

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "50 100\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 50)
        self.assertEqual(j, 100)

    def test_read_3 (self) :
        s    = "999 50\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 999)
        self.assertEqual(j, 50)

    def test_read_4 (self) :
        s    = "10000 20000\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 10000)
        self.assertEqual(j, 20000)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_5 (self) :
        v = collatz_eval(10840, 9961)
        self.assertEqual(v, 255)

    def test_eval_6 (self) :
        v = collatz_eval(18774, 19142)
        self.assertEqual(v, 261)

    def test_eval_7 (self) :
        v = collatz_eval(17204, 18275)
        self.assertEqual(v, 279)

    def test_eval_8 (self) :
        v = collatz_eval(7636, 5905)
        self.assertEqual(v, 262)

    # -----
    # cycles
    # -----
    def test_cycles_1 (self) :
        v = findCycle(4)
        self.assertTrue(v == 3)

    def test_cycles_2 (self) :
        v = findCycle(10)
        self.assertTrue(v == 7)

    def test_cycles_3 (self) :
        v = findCycle(100)
        self.assertTrue(v == 26)

    def test_cycles_4 (self) :
        v = findCycle(4249)
        self.assertTrue(v == 127)

    def test_cycles_5 (self) :
        v = findCycle(22)
        self.assertTrue(v == 16)

    def test_cycles_6 (self) :
        v = findCycle(59)
        self.assertTrue(v == 33)

    def test_cycles_7 (self) :
        v = findCycle(5353)
        self.assertTrue(v == 47)

    def test_cycles_8 (self) :
        v = findCycle(999999)
        self.assertTrue(v == 259)


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 18774, 19142, 261)
        self.assertEqual(w.getvalue(), "18774 19142 261\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 17204, 18275, 279)
        self.assertEqual(w.getvalue(), "17204 18275 279\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 7636, 5905, 262)
        self.assertEqual(w.getvalue(), "7636 5905 262\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("12 12\n34 34\n55 55\n66 66\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "12 12 10\n34 34 14\n55 55 113\n66 66 28\n")

    def test_solve_3 (self) :
        r = StringIO("11 20\n20 55\n500 900\n9000 10\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "11 20 21\n20 55 113\n500 900 179\n9000 10 262\n")

    def test_solve_4 (self) :
        r = StringIO("90 50000\n45 46\n69 79\n50000 1\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "90 50000 324\n45 46 17\n69 79 116\n50000 1 324\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1



% coverage3 report -m                   >> TestCollatz.out



% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""
