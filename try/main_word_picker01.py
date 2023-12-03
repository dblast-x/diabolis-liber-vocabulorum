"""
Steps >>
1. Find the uppercase letter.
2. Separate the *pattern from the meaning
3. Insert it into the DB.

Pattern >>
  * | startswith_capitalized_letter + one_or_more_linebreaks >>
  ( A \n)
  * | startswith_capitalized_word + coma + space + [letters + dot]s + space >>
  (Abstemio, s.  ) || (Abstemio, v. t.  )
"""

import re

# import sqlite3


def letter_picker(file: str):
    if len(file) < 1:
        with open("src/edited_diabolous.txt", "r") as f:
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
    count = 0
    if len(file) < 1:
        with open("src/edited_diabolous.txt", "r") as f:
            print("Find the Pattern.")
            pattern = re.compile(r"(^[\w]+,\s[svtiadj.]+)\s")
            for line in f:
                line = line.rstrip()
                print(line)
                match = re.findall(pattern, line)
                if match:
                    # print(line)  # D
                    count += 1
                    print(match, "found!")
                else:
                    continue
        print(count)


def meaning_picker(file: str):
    count = 0
    if len(file) < 1:
        with open("src/edited_diabolous.txt", "r") as f:
            print("Find the Pattern.")
            pattern = re.compile(r"^[\w]+,\s[svtiadj.]+\s(.+$)")
            for line in f:
                line = line.rstrip()
                match = re.findall(pattern, line)
                if match:
                    count += 1
                    print(match, "found!")
                else:
                    continue
        print(count)


def parser_on():
    inp = input("Type in the file or no >> ")
    # letter_picker(inp)
    # word_picker(inp)
    meaning_picker(inp)


if __name__ == "__main__":
    parser_on()
