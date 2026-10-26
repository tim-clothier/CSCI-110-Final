#Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the first line in the old file becomes the last one in the new file)

# Open dummy text file, store it in a list, then reverse the list order
txt = open("dummy.txt", "r")
xs = txt.readlines()
xs.reverse()

#Write new file with reversed list order, giving a file with the lines reversed
txt_s = open("sorted_dummy.txt", "w")
for l in xs:
    txt_s.write(l)
txt_s.close()