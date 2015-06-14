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
        s    = "100 200\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  100)
        self.assertEqual(j, 200)

    def test_read_3 (self) :
        s    = "201 210\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 201)
        self.assertEqual(j, 210)

    def test_read_4 (self) :
        s    = "900 1000\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  900)
        self.assertEqual(j, 1000)

    def test_read_5 (self) :
        s    = "1 1\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 1)

    def test_read_6 (self) :
        s    = "7 27\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  7)
        self.assertEqual(j, 27)

    def test_read_7 (self) :
        s    = "54 97\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 54)
        self.assertEqual(j, 97)

    def test_read_8 (self) :
        s    = "10971 13255 255\n"
        i, j = collatz_read(s)
        self.assertEqual(i, 0)
        self.assertEqual(j, 0)

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
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)

    def test_eval_6 (self) :
        v = collatz_eval(7, 27)
        self.assertEqual(v, 112)

    def test_eval_7 (self) :
        v = collatz_eval(54, 97)
        self.assertEqual(v, 119)

    def test_eval_8 (self) :
        v = collatz_eval(-27, 7)
        self.assertEqual(v, 0)

    def test_eval_9 (self) :
        v = collatz_eval(0, 1)
        self.assertEqual(v, 0)

    def test_eval_10 (self) :
        v = collatz_eval("abcd", "ABCD")
        self.assertEqual(v, 0)
  
    # -----
    # print
    # -----

    def test_print_1 (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")

    def test_print_2 (self) :
        w = StringIO()
        collatz_print(w, 100, 200, 125)
        self.assertEqual(w.getvalue(), "100 200 125\n")

    def test_print_3 (self) :
        w = StringIO()
        collatz_print(w, 201, 210, 89)
        self.assertEqual(w.getvalue(), "201 210 89\n")

    def test_print_4 (self) :
        w = StringIO()
        collatz_print(w, 900, 1000, 174)
        self.assertEqual(w.getvalue(), "900 1000 174\n")

    def test_print_5 (self) :
        w = StringIO()
        collatz_print(w, 1, 1, 1)
        self.assertEqual(w.getvalue(), "1 1 1\n")

    def test_print_6 (self) :
        w = StringIO()
        collatz_print(w, "abcd", "ABCD", 4)
        self.assertEqual(w.getvalue(), "")

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

# ----
# main
# ----

if __name__ == "__main__" :
    main()
