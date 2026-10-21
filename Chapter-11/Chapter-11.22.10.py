#Write a function replace(s, old, new) that replaces all occurences of old with new in a string s
import sys

    # Define [s_list] as a list of characters/words delimited by the [old] string we want to replace (split function omits delimiter from result)
    # Join s_list (which now has instances of [old] ommitted) into output, using [new] as the glue, functionally replacing all instances of [old] with [new]
    # Return output

def replace(s, old, new) :
    s_list = s.split(old)
    output = new.join(s_list)
    return output


def test(did_pass):
    linenum = sys._getframe(1).f_lineno
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else :
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

test(replace("Mississippi", "i", "I") == "MIssIssIppI")

string1 = "I love spom! Spom is my favorite food. Spom, spom, yum!"

test(replace(string1, "om", "am") == "I love spam! Spam is my favorite food. Spam, spam, yum!")

test(replace(string1, "o", "a") == "I lave spam! Spam is my favarite faad. Spam, spam, yum!")