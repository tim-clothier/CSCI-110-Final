import string
text = '''Chapter One

All this happened, more or less. The war parts, anyway, are pretty much true. One guy I knew really was shot in Dresden for taking a teapot that wasn't his. Another guy I knew really did threaten to have his personal enemies killed by hired gunmen after the war. And so on. I've changed all the names.

I really did go back to Dresden with Guggenheim money (God love it) in 1967. It looked a lot like Dayton, Ohio, more open spaces than Dayton has. There must be tons of human bone meal in the ground.

I went back there with an old war buddy, Bernard V. O'Hare, and we made friends with a cab driver, who took us to the slaughterhouse where we had been locked up at night as prisoners of war. His name was Gerhard Müller. He told us that he was a prisoner of the Americans for a while. We asked him how it was to live under Communism, and he said that it was terrible at first, because everybody had to work so hard, and because there wasn't much shelter or food or clothing. But things were much better now. He had a pleasant little apartment, and his daughter was getting an excellent education. His mother was incinerated in the Dresden fire-storm. So it goes.'''


def analyze_text(s) :
    s_no_punct = ""
    for letter in s :
        if letter not in string.punctuation :
            s_no_punct += letter

    s_split = s_no_punct.split()

    total_words = len(s_split)
    words_with_e = 0
    for word in s_split :
        if "e" in word :
            words_with_e += 1

    word_ratio = words_with_e / total_words

    #print(f"Total words: {total_words}")
    #print(f"Words with an 'E': {words_with_e}")
    #print(f"E ratio: {word_ratio:.1%}")

    print(f'Your text contains {total_words} words, of which {words_with_e} ({word_ratio:.1%}) contain an "e"')

analyze_text(text)
