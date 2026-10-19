#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s
import sys

def replace(s, old, new) :
    output = list(s)
    for (i, val) in enumerate(output) :
        print(val)
        if val == old :
            #print("i is equal to old")
            output[i] = new
    output = "".join(output)
    print(output)
    return output


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else :
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(replace("Mississippi", "i", "I") == "MIssIssIppI")
s = "I love spom! Spom is my favorite food. Spom, spom, yum!"
test(replace(s, "om", "am") == "I love spam! Spam is my favorite food. SPam, spam, yum!")