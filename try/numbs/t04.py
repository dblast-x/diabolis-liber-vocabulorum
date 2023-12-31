import re

"""
CREATE TABLE Letters(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
letter VARCHAR(1) NOT NULL,
word_id INTEGER);

CREATE TABLE Words(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL UNIQUE,
word VARCHAR(10) NOT NULL,
meaning VARCHAR(50) NOT NULL,
letter_id INTEGER);
"""


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
            meaning  NOT NULL,
            letter_id INTEGER)
        """
    )
    key_list = list(dictionary.keys())
    letter_id = 1
    for x in key_list:
        cur.execute("INSERT INTO Letters(letter) VALUES(?)", (x,))
        for key, value in dictionary[x].items():
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


letters = ["A", "B", "C"]

words = [
    "Abandonado, s. y adj.",
    "Abdicación, s.",
    "Abdomen, s.",
    "Aborígenes, s.",
    "Baal, s.",
    "Baco, s.",
    "Bailar, v.i.",
    "Baño, s.",
    "Basilisco, s.",
    "Caaba, s.",
    "Cabo, s.",
    "Cagatintas, s.",
]


def define(words):
    end, start = 1, 0
    _ = input("!!Start!!")
    with open("try/abc/tst.txt", "r") as f:
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


def make_dict(letters, definitions):
    dictionary = {letter: {} for letter in letters}
    for definition in definitions:
        for key, value in definition.items():
            key_letter = key[0]
            if key_letter in dictionary:
                dictionary[key_letter].update({key: value})
            else:
                print(f"'{key_letter}' Not found")

    return dictionary


definitions = define(words)
dictionary = make_dict(letters, definitions)

set_db(dictionary)
print("Done!!")
