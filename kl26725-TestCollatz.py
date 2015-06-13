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

# ------------
# TestCollatz
# ------------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read_1 (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

    def test_read_2 (self):
        s    = "987 420\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  987)
        self.assertEqual(j, 420)

    def test_read_3 (self):
        s    = "100000 999999\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100000)
        self.assertEqual(j, 999999)

    def test_read_4 (self):
        s    = "987654 3210\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  987654)
        self.assertEqual(j, 3210)

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
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20)

    def test_eval_6 (self) :
        v = collatz_eval(25, 30)
        self.assertEqual(v, 112)

    def test_eval_7 (self) :
        v = collatz_eval(222, 222222)
        self.assertEqual(v, 386)

    def test_eval_8 (self) :
        v = collatz_eval(321321, 12)
        self.assertEqual(v, 443)

    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 10, 1, 20)
        self.assertEqual(w.getvalue(), "10 1 20\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 222, 222222, 386)
        self.assertEqual(w.getvalue(), "222 222222 386\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 321321, 12, 443)
        self.assertEqual(w.getvalue(), "321321 12 443\n")

    # -----
    # solve
    # -----

    # Fix solving 

    def test_solve_1 (self) :        
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)        
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")        

    def test_solve_2 (self) :        
        r = StringIO("10 1\n25 30\n1000 1\n837790 837800\n")
        w = StringIO()
        collatz_solve(r, w)        
        self.assertEqual(w.getvalue(), "10 1 20\n25 30 112\n1000 1 179\n837790 837800 525\n")        

    def test_solve_3 (self) :        
        r = StringIO("222 222222\n200 100\n654 123\n444 222\n")
        w = StringIO()
        collatz_solve(r, w)        
        self.assertEqual(w.getvalue(), "222 222222 386\n200 100 125\n654 123 145\n444 222 144\n")        

    def test_solve_4 (self) :        
        r = StringIO("321321 12\n1020 1080\n420 69\n1440 4000\n")
        w = StringIO()
        collatz_solve(r, w)        
        self.assertEqual(w.getvalue(), "321321 12 443\n1020 1080 169\n420 69 144\n1440 4000 238\n")        
        

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
