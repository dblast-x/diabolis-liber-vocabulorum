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
    with open("t_src/Diabolous.txt", "r") as f:
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


def pick_definitions():
    """
    Creates a list with the extracted words
    and their meanings.
    """
    with open("t_src/edit.txt", "r") as f:
        patterns = "|".join(
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
                words.append(match)
            else:
                continue

        definitions_list = [
            alpha for sublist in words for word in sublist for alpha in word if alpha
        ]

        return definitions_list


def pick_types():
    """
    Creates a list of types
    """
    with open("t_src/edit.txt", "r") as f:
        patterns = "|".join(
            [
                "^[A-Z][\w]+, (s[.])",
                "^[A-Z][\w]+, (adj[.] y s[.])",
                "^[A-Z][\w]+, (adj[.])",
                "^[A-Z][\w]+, (adv[.])",
                "^[A-Z][\w]+, (v[.]t[.])",
                "^[A-Z][\w]+, (v[.]i[.])",
                "^[A-Z][\w]+, (v[.]r[.])",
            ]
        )
        compiled = re.compile(patterns)
        types = list()
        for line in f:
            line = line.rstrip()
            match = re.findall(patterns, line)
            if match:
                types.append(match)
            else:
                continue
        print(types)

        type_list = set(
            [alpha for sublist in types for typ in sublist for alpha in typ if alpha]
        )

        return type_list


def define(picked):
    """
    Structures the definitions.
    """
    end, start = 1, 0
    with open("t_src/edit.txt", "r") as f:
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
                pattern = f"\n*{picked[start]}(.+)[\n.]{picked[end]}"
                match = re.findall(pattern, file, re.MULTILINE | re.DOTALL)
            except IndexError:
                match = re.findall(
                    f"\n*{picked[start]}(.+)", file, re.MULTILINE | re.DOTALL
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

    conn = s3.connect("dict.db")
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
    key_list = list(dictionary.keys())  # select the letters.
    letter_id = 1
    for x in key_list:
        actual = dictionary[x]  # <- collects the word&def dict for each letter ->
        cur.execute("INSERT INTO Letters(letter) VALUES(?)", (x,))
        for key, value in actual.items():  # <- key => word && value => meaning ->
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
    # letters = pick_letters()
    # # print(letters)
    definitions = define(pick_definitions())
    print(definitions)
    # types = pick_types()
    # print(types)
    # dictionary = make_dictionary(letters, definitions)
    # # print(dictionary)
    # set_db(dictionary)
    # print("Database created")


if __name__ == "__main__":
    game_on()
