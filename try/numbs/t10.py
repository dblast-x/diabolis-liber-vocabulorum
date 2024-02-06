import re


def pick_letters():
    """
    Selects each letter from the book.
    25 letters >>
    A, B, C, D, E, F,
    G, H, I, J, K, L,
    M, N, O, P, Q, R,
    S, T, U, V, W, Y,
    Z.
    """
    letters = list()
    with open("src/Diabolous.txt", "r") as f:
        pattern = re.compile("^[A-Z]\n")
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
    Creates a list with the extracted words.
    """
    with open("src/edit.txt", "r") as f:
        patterns = "|".join(
            [
                "(\n*^[A-Z][\w]+), s[.] y adj[.]",
                "(\n*^[A-Z][\w]+), adj[.] y s[.]",
                "(\n*^[A-Z][\w]+), adj[.]",
                "(\n*^[A-Z][\w]+), adv[.]",
                "(\n*^[A-Z][\w]+), s[.]",
                "(\n*^[A-Z][\w]+), v[.]t[.]",
                "(\n*^[A-Z][\w]+), v[.]i[.]",
                "(\n*^[A-Z][\w]+), v[.]r[.]",
            ]
        )
        pattern = re.compile(patterns)
        words = list()
        for line in f:
            line = line.rstrip()
            match = re.findall(pattern, line)
            if match:
                words.append(match)
            else:
                continue

        definitions_list = [
            alpha for sublist in words for word in sublist for alpha in word if alpha
        ]

        return definitions_list


def define(picked):
    """
    Structures the definitions.
    """
    end, start = 1, 0
    with open("src/edit.txt", "r") as f:
        # ->> preps
        file = f.read()
        lenght = range(len(picked))
        definitions = list()
        # ->> preps
        x = 0
        for s in lenght:
            start = s
            definition = dict()
            try:
                pattern = rf"\n*{picked[start]}(.+)[\n.]{picked[end]}"
                match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            except IndexError:
                match = re.findall(
                    rf"\n*{picked[start]}(.+)", file, re.MULTILINE | re.DOTALL
                )

            if len(match) > 0:
                definition[picked[start]] = match[0]
                definitions.append(definition)
                print("." * x)
                x += 1
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

    conn = s3.connect("diabolous.db")
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
    definitions = define(pick_words())
    dictionary = make_dictionary(letters, definitions)
    set_db(dictionary)
    print("Database created")


if __name__ == "__main__":
    game_on()
