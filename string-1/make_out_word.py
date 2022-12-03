# Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".

def make_out_word(out, word):
    print(out[:2] + word + out[2:])

# test cases

make_out_word('<<>>', 'Yay')
make_out_word('<<>>', 'WooHoo')
make_out_word('[[]]', 'word')