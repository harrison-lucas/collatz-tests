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

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

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
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self) :
        s    = "17 151\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  17)
        self.assertEqual(j, 151)

    def test_read_3 (self) :
        s    = "999000 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 999000)
        self.assertEqual(j, 999999)

    def test_read_4 (self) :
        s    = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    def test_read_5 (self) :
        s    = "4838 182\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 4838)
        self.assertEqual(j, 182)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(999000, 999999)
        self.assertEqual(v, 396)

    def test_eval_3 (self) :
        v = collatz_eval(1, 1001)
        self.assertEqual(v, 179)

    def test_eval_4 (self) :
        v = collatz_eval(4999, 6051)
        self.assertEqual(v, 236)

    def test_eval_5 (self) :
        v = collatz_eval(4838, 182)
        self.assertEqual(v, 238)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 999000, 999999, 396)
        self.assertEqual(w.getvalue(), "999000 999999 396\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 17, 151, 122)
        self.assertEqual(w.getvalue(), "17 151 122\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 4999, 6051, 236)
        self.assertEqual(w.getvalue(), "4999 6051 236\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 4838, 182, 238)
        self.assertEqual(w.getvalue(), "4838 182 238\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("17 151\n999000 999999\n1 1001\n4999 6051\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "17 151 122\n999000 999999 396\n1 1001 179\n4999 6051 236\n")

    def test_solve_3 (self) :
        r = StringIO("93939 1003\n4838 182\n123 456\n10 11\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "93939 1003 351\n4838 182 238\n123 456 144\n10 11 15\n")
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
