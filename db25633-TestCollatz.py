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

from Collatz import collatz_read, collatz_cycle_length, collatz_eval, collatz_print, collatz_solve

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
        s    = "2 20\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  2)
        self.assertEqual(j, 20)

    def test_read_3 (self) :
        s    = "45 457\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  45)
        self.assertEqual(j, 457)

    # ----
    # cycle_length
    # ----

    def test_cycle_length_1 (self) :
        v = collatz_cycle_length(1, 0)
        self.assertEqual(v, 1)

    def test_cycle_length_2 (self) :
        v = collatz_cycle_length(2, 0)
        self.assertEqual(v, 2)

    def test_cycle_length_3 (self) :
        v = collatz_cycle_length(5, 0)
        self.assertEqual(v, 6)

    def test_cycle_length_4 (self) :
        v = collatz_cycle_length(10, 0)
        self.assertEqual(v, 7)
        
    def test_cycle_length_5 (self) :
        v = collatz_cycle_length(100, 0)
        self.assertEqual(v, 26)

    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_2 (self) :
        v = collatz_eval(1, 2)
        self.assertEqual(v, 2)

    def test_eval_3 (self) :
        v = collatz_eval(2, 1)
        self.assertEqual(v, 2)        
    
    def test_eval_4 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_5 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_6 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_7 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_8 (self) :
        v = collatz_eval(37, 67)
        self.assertEqual(v, 113)

    def test_eval_9 (self) :
        v = collatz_eval(5000, 70006)
        self.assertEqual(v, 340)

    
    def test_eval_10 (self) :
        v = collatz_eval(1, 1000000)
        self.assertEqual(v, 525)
	
    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_2 (self) :
        r = StringIO("900 1000\n37 67\n5000 70006\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "900 1000 174\n37 67 113\n5000 70006 340\n")
    
    def test_solve_3 (self) :
        r = StringIO("900 1000\n37 67\n5000 70006\n1 1000000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "900 1000 174\n37 67 113\n5000 70006 340\n1 1000000 525\n")

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


