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
        s    = "1001 2001\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1001)
        self.assertEqual(j, 2001)

    def test_read_3 (self) :
        s    = "2 0\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  2)
        self.assertEqual(j, 0)

    def test_read_4 (self) :
        s    = "12 136\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  12)
        self.assertEqual(j, 136)
  
    # ----
    # eval
    # ----


    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20) #ok....
 
    def test_eval_2 (self) :
        v = collatz_eval(100, 100)
        self.assertEqual(v, 26) #ok

    def test_eval_3 (self) :
        v = collatz_eval(101, 101)
        self.assertEqual(v, 26) #ok

    def test_eval_4 (self) :
        v = collatz_eval(102, 102)
        self.assertEqual(v, 26) #ok

    def test_eval_5 (self) :
        v = collatz_eval(103, 103)
        self.assertEqual(v, 88) #ok

    def test_eval_6 (self) :
        v = collatz_eval(104, 104)
        self.assertEqual(v, 13) #ok

    def test_eval_7 (self) :
        v = collatz_eval(105, 105)
        self.assertEqual(v, 39) #ok

    def test_eval_8 (self) :
        v = collatz_eval(106, 106)
        self.assertEqual(v, 13) #ok

    def test_eval_9 (self) :
        v = collatz_eval(107, 107)
        self.assertEqual(v, 101) #ok

    def test_eval_10 (self) :
        v = collatz_eval(108, 108)
        self.assertEqual(v, 114) #ok

    def test_eval_11 (self) :
        v = collatz_eval(109, 109)
        self.assertEqual(v, 114) #ok
 
    def test_eval_12 (self) :
        v = collatz_eval(100, 109)
        self.assertEqual(v, 114) #ok

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125) #ok

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89) #ok

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174) #ok

    def test_eval_5 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20) #ok

    def test_eval_6 (self) :
        v = collatz_eval(210, 201)
        self.assertEqual(v, 89) #ok

    def test_eval_7 (self) :
        v = collatz_eval(842, 842)
        self.assertEqual(v, 42) #ok
    def test_eval_8 (self) :
        v = collatz_eval(462, 462)
        self.assertEqual(v, 129)#ok
    def test_eval_9 (self) :
        v = collatz_eval(868, 868)
        self.assertEqual(v, 29)#ok
    def test_eval_10 (self) :
        v = collatz_eval(571, 571)
        self.assertEqual(v,31 ) #ERROR
    def test_eval_11 (self) :
        v = collatz_eval(3, 3)
        self.assertEqual(v, 8) #ERROR
    def test_eval_12 (self) :
        v = collatz_eval(42, 42)
        self.assertEqual(v, 9) #ERROR
    def test_eval_13 (self) :
        v = collatz_eval(533, 533)
        self.assertEqual(v, 31)  #ERROR
 
    def test_eval_14 (self) :
        v = collatz_eval(10, 1)
        self.assertEqual(v, 20) #ok....
    def test_eval_15 (self) :
        v = collatz_eval(200, 100)
        self.assertEqual(v, 125) #ok
    def test_eval_16 (self) :
        v = collatz_eval(210, 201)
        self.assertEqual(v, 89) #ok
    def test_eval_17 (self) :
        v = collatz_eval(1000, 900)
        self.assertEqual(v, 174) #ok
    def test_eval_18 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20) #ok
    def test_eval_19 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89) #ok  
    def test_eval_20 (self) :
        v = collatz_eval(99999, 99999)
        self.assertEqual(v, 227) #ok  
    def test_eval_21 (self) :
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1) #ok  
 
    def test_eval_22 (self) :
        v = collatz_eval(1, 99999)
        self.assertEqual(v, 351) #ok  

    def test_eval_23 (self) :
        v = collatz_eval(99998, 99999)
        self.assertEqual(v, 227) #ok  
  


    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 10, 10, 7)
        self.assertEqual(w.getvalue(), "10 10 7\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 99998, 99999, 227)
        self.assertEqual(w.getvalue(), "99998 99999 227\n")
 
    # -----
    # solve
    # -----

    def test_solve_1 (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")


    def test_solve_2 (self) :
        r = StringIO("1 99999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 99999 351\n")


    def test_solve_3 (self) :
        r = StringIO("99998 99999\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "99998 99999 227\n")

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
