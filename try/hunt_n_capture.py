import re

# import sqlite3


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
        patterns = r"|".join(
            [
                "^[A-Z][\w]+, s[.] y adj[.]",
                "^[A-Z][\w]+, adj[.] y s[.]",
                "^[A-Z][\w]+, adj[.]",
                "^[A-Z][\w]+, adv[.]",
                "^[A-Z][\w]+, s[.]",
                "^[A-Z][\w]+, v[.]t[.]",
                "^[A-Z][\w]+, v[.]i[.]",
                "^[A-Z][\w]+, v[.]r[.]",
            ]
        )
        compiled = re.compile(patterns)
        words = list()
        for line in f:
            line = line.rstrip()
            match = re.findall(patterns, line)
            if match:
                words.append(match)
            else:
                continue
        # HACK: Just in case is needed only the word
        # words = [word for sublist in words for tpl in sublist for word in tpl if word]
        definition = [word for sublist in words for word in sublist]

        return definition


def meaning_picker(words):
    end, start = 1, 0
    _ = input("!!Start!!")
    # print(f"start, end \t\t ->> {start}|{end}")
    with open("src/edit.txt", "r") as f:
        file = f.read()
        lenght = range(len(words))
        for s in lenght:
            start = s
            text = dict()
            try:
                pattern = rf"\n*{words[start]}(.+)\n*{words[end]}"
                match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            except IndexError:
                match = re.findall(
                    rf"\n*{words[start]}(.+)", file, re.MULTILINE | re.DOTALL
                )

            if len(match) > 0:
                text[words[start]] = match[0]
                print(text)
            else:
                continue
            start += 1
            end += 1
        print(start, end)


def parser_on():
    _ = input("!!Start!!Start!!")
    letters = letter_picker()
    words = word_picker()
    meaning_picker(words)
    # print(words)


if __name__ == "__main__":
    parser_on()
