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


    Loop inside file and word_list( ->> words
    re.search( <<- words ) in file
    extract meaning from
    boundaries( ->> word_to_word
    .
"""

import re


def letter_picker():
    letters = list()
    """
    #  25 letters
      'A', 'B', 'C', 'D', 'E', 'F',
      'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'Y',
      'Z'.
    """
    with open("src/edit.txt", "r") as f:
        # print("Find the Letter.")
        pattern = re.compile(r"^[A-Z]\n")
        for line in f:
            match = re.search(pattern, line)
            if match:
                letters.append(line.strip())
            elif match is None:
                continue
            else:
                print("Not found")

    return letters


def word_picker():
    """
    The actual count is 804.
    """
    with open("src/edit.txt", "r") as f:
        # print("Find the Pattern.")
        patterns = r"|".join(
            [
                "(^[A-Z][\w]+), s[.] y adj[.]",
                "(^[A-Z][\w]+), adj[.] y s[.]",
                "(^[A-Z][\w]+), adj[.]",
                "(^[A-Z][\w]+), adv[.]",
                "(^[A-Z][\w]+), s[.]",
                "(^[A-Z][\w]+), v[.]t[.]",
                "(^[A-Z][\w]+), v[.]i[.]",
                "(^[A-Z][\w]+), v[.]r[.]",
            ]
        )
        compiled = re.compile(patterns)
        words = list()
        for line in f:
            line = line.rstrip()
            match = re.findall(patterns, line)
            if match:
                print(match, "found!")
                words.append(match)
            else:
                continue

        return words


def meaning_picker(file: str):
    pass


def search_words(letters):
    with open("src/edit.txt", "r") as f:
        start, end = 0, 1
        for letter in range(0, len(letters)):
            text = ""
            with open(f"try/{letters[letter]}.txt", "w") as target:
                for line in f:
                    a = re.search(rf"^{letters[start]}\n", line)
                    if a is not None:
                        print(a)
                        text += line
                    try:
                        b = re.search(rf"^{letters[end]}\n", line)
                        if b is None:
                            text += line
                        else:
                            print(b)
                            break
                    except IndexError:
                        text += line
                    target.write(text)
                    text = ""
            start += 1
            end += 1


def parser_on():
    _ = input("!!Start!!Start!!")
    letters = letter_picker()
    words = word_picker()
    print(len(letters), "\t\t->> .letters.")
    print(len(words), "\t\t->> .words.")


if __name__ == "__main__":
    parser_on()
