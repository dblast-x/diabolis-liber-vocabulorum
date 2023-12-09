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
        # print("Find the Pattern.")
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
                # print(match, "found!")
                words.append(match)
            else:
                continue

        # HACK: the findall is returning a list of lists of tuples
        #       had to extract them first
        # words = [word for sublist in words for tpl in sublist for word in tpl if word]
        definition = [word for sublist in words for word in sublist]

        return definition


def meaning_picker():
    pass


def search_words(words):
    start, end = 0, 1
    with open(f"src/edit.txt", "r") as f:
        for _ in range(len(words)):
            text = ""
            t = 0
            for line in f:
                a = re.search(r"^" + words[start] + ",\s", line)
                if a is not None:
                    if t == 0:
                        span = a.span[1]
                        text += line[span:]
                        t += 1
                    print(a)
                    text += line
                try:
                    b = re.search(r"^" + words[end] + ",\s", line)
                    if b is None:
                        text += line
                    else:
                        print(b)
                        break
                except IndexError:
                    print(1)
                    text += line
                print(text)
                text = ""
            start += 1
            end += 1


def parser_on():
    _ = input("!!Start!!Start!!")
    letters = letter_picker()
    words = word_picker()
    print(words)
    # search_words(words)


if __name__ == "__main__":
    parser_on()
