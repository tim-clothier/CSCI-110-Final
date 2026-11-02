# Write a program called alice_words.py that creates a text file named alice_words.txt containing an alphabetical listing of all the words, 
# and the number of times each occurs, in the text version of ALice's Adventures in Wonderland.
#Import string library for text processing/string clean-up i.e. punctuation
import string
#Import re for re.split, allowing for multiple delimiters
import re

#Define dictionary to keep track of all unique words and occurence counts
unique_words = {}

#Import .txt file and split into list of words
alice_txt = open('alice.txt', 'r').read()
alice_words = re.split(r'[-—\s]+', alice_txt)


#Iterate over txt list
for word in alice_words:
    #Format to lowercase
    lword = word.lower()
    #Strip punctuation
    sword = lword.translate(str.maketrans('', '', string.punctuation))
    #Check if word is in the dictionary already
    if sword not in unique_words:
        #Add word to dictionary, start count at one
        unique_words[sword] = 1
    else :
        #Increment occurence count
        unique_words[sword] += 1

#Sort into alphabetical list
sorted_unique_words = list(unique_words.items())
sorted_unique_words.sort()

#Create output text document, header, and seperator.
output_txt = open("alice_words.txt", "w")
header = "{0:<16}{1:>16}".format("Words", "Count""\n")
seperator = "================================\n"
output_txt.write(header)
output_txt.write(seperator)

for word in sorted_unique_words:
    #Create output line for each unique word in our dictionary
    output = "{0:<16}{1:>16}\n".format(word[0], word[1])
    #Write to output file
    output_txt.write(output)