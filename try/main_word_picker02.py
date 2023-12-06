"""
 Steps >>
   1. Find the uppercase letter.
   2. Separate the words from the meanings.
   3. Insert it into the DB.

 Patterns >>
   * | startswith_capitalized_letter + one_or_more_linebreaks >>
   ( A \n)
   * | startswith_capitalized_word + coma + space + [letters + dot]s + space >>
   (Abstemio, s.  ) || (Abstemio, v. t.  )

TODO: 
    try exporting the letters in a list >>
    then use them to search in the files >>
    then extract the words and export them in a list >>
    then use them to mark the boundaries of the meanings
    and extract them.
    Pass everything to a DB.sqlite
"""

import re

# import sqlite3


def letter_picker(file: str):
    if len(file) < 1:
        with open("src/edit.txt", "r") as f:
            print("Find the Letter.")
            for line in f:
                match = re.search(r"^[A-Z]\n+", line)
                if match:
                    print("found!", match.group())
                elif match is None:
                    continue
                else:
                    print("Not found")


def word_picker(file: str):
    """
    The actual count is 806. Still missing the
    definition-words that include spaces and numbers.

    Another algorithm that half-worked >>
     [svtiadj.]+
    """
    if len(file) < 1:
        with open("src/edit.txt", "r") as f:
            print("Find the Pattern.")
            patterns = r"|".join(
                [
                    "^[A-Z][\w]+, s. y adj.",
                    "^[A-Z][\w]+, adj. y s.",
                    "^[A-Z][\w]+, adj.",
                    "^[A-Z][\w]+, adv.",
                    "^[A-Z][\w]+, s.",
                    "^[A-Z][\w]+, v.t.",
                    "^[A-Z][\w]+, v.i.",
                ]  # add the 'numbered' ones
            )
            compiled = re.compile(patterns)
            for line in f:
                line = line.rstrip()
                match = re.findall(patterns, line)
                if match:
                    print(match, "found!")
                else:
                    continue


def meaning_picker(file: str):
    pass


def parser_on():
    inp = input("Type in the file, or no >> ")
    letter_picker(inp)
    word_picker(inp)
    # meaning_picker(inp)


if __name__ == "__main__":
    parser_on()
