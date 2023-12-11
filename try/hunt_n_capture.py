import re


def pick_letters():
    letters = list()
    """
    #  25 letters
      'A', 'B', 'C', 'D', 'E', 'F',
      'G', 'H', 'I', 'J', 'K', 'L',
      'M', 'N', 'O', 'P', 'Q', 'R',
      'S', 'T', 'U', 'V', 'W', 'Y',
      'Z'.
    """
    with open("src/Diabolous.txt", "r") as f:
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


def pick_words():
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

        definition = [word for sublist in words for word in sublist]

        return definition


def pick_definitions(words):
    end, start = 1, 0
    with open("src/edit.txt", "r") as f:
        # ->> preps
        file = f.read()
        lenght = range(len(words))
        definitions = list()
        # ->> preps
        for s in lenght:
            start = s
            definition = dict()
            try:
                pattern = rf"\n*{words[start]}(.+)\n*{words[end]}"
                match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            except IndexError:
                match = re.findall(
                    rf"\n*{words[start]}(.+)", file, re.MULTILINE | re.DOTALL
                )

            if len(match) > 0:
                definition[words[start]] = match[0]
                definitions.append(definition)
            else:
                continue
            start += 1
            end += 1

        return definitions


def make_dictionary(letters, definitions):
    dictionary = {letter: {} for letter in letters}
    for definition in definitions:
        for key, value in definition.items():
            key_letter = key[0]
            if key_letter in dictionary:
                dictionary[key_letter].update({key: value})
            else:
                print(f"'{key_letter}' Not found")

    return dictionary


def set_db(dictionary):
    import sqlite3 as s3

    conn = s3.connect("dict.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Letters")
    cur.execute("DROP TABLE IF EXISTS Words")

    cur.execute(
        """
        CREATE TABLE Letters(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            letter VARCHAR(1) NOT NULL)
        """
    )
    cur.execute(
        """
        CREATE TABLE Words(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
            word TEXT NOT NULL,
            meaning TEXT NOT NULL,
            letter_id INTEGER)
        """
    )
    key_list = list(dictionary.keys())
    letter_id = 1
    for x in key_list:
        actual = dictionary[x]
        cur.execute("INSERT INTO Letters(letter) VALUES(?)", (x,))
        for key, value in actual.items():
            cur.execute(
                """
            INSERT INTO Words(word, meaning, letter_id) VALUES(
                ?, ?, ?)""",
                (
                    key,
                    value,
                    letter_id,
                ),
            )
        letter_id += 1

    conn.commit()


def game_on():
    _ = input("!!Start!!Start!!")
    letters = pick_letters()
    words = pick_words()
    definitions = pick_definitions(words)
    dictionary = make_dictionary(letters, definitions)
    # set_db(dictionary)
    print("Database created")


if __name__ == "__main__":
    game_on()
