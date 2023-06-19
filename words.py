import argparse
import string
import random


def word_input():

    parser = argparse.ArgumentParser()

    parser.add_argument("--words", type=str, default="hangman.txt", help="Pdf with over 24k words")

    return parser.parse_args()

def get_words(vocabulary):

    words_dict = dict()

    with open(vocabulary, "r", encoding="UTF-8") as phrases:

        in_file = phrases.readline()


        while in_file != "":

            in_file = in_file.split()

            labels = ""

            for word in in_file:
                word = word.strip()
                if (len(word) >= 4):
                    if (word[0] not in string.punctuation and word[len(word) - 1] not in
                            string.punctuation and (word[0] in string.ascii_lowercase and
                            word[len(word) - 1] in string.ascii_lowercase)
                    ):
                        words_dict[word.lower()] = 1

                else:
                    labels += word + " "

            in_file = phrases.readline()

    return words_dict

def word_list(words_dict):
    words = []

    for key in words_dict:
        if key.translate(str.maketrans("", "", string.punctuation)):
            words.append(key)

    return words

in_args = word_input()

words_dict = get_words(in_args.words)

words = word_list(words_dict)





