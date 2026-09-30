#Write a function that converts hours, minutes, and seconds into a total number of seconds
import sys

def convert_to_seconds (h, m, s):
    total_seconds = 0
    total_seconds += h * 3600
    total_seconds += m * 60
    total_seconds += s

    return total_seconds

def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def test_suite():
    test(convert_to_seconds(2, 30, 10) == 9010)
    test(convert_to_seconds(2, 0, 0) == 7200)
    test(convert_to_seconds(0, 2, 0) == 120)
    test(convert_to_seconds(0, 0, 42) == 42)
    test(convert_to_seconds(0, -10, 10) == -590)

test_suite();