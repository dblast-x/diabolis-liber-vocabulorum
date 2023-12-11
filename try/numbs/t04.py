import re


def set_db():
    import sqlite3 as s3

    conn = s3.connect("dict.sqlite")
    cur = conn.cursor()

    cur.execute("DROP TABLE IF EXISTS Letters")
    cur.execute("DROP TABLE IF EXISTS Definitions")

    cur.execute(
        """
        CREATE TABLE Letters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            letter VARCHAR(1) NOT NULL UNIQUE
        )
        """
    )
    cur.execute(
        """
        CREATE TABLE Definitions (
            letter_id INTEGER NOT NULL,
            words TEXT NOT NULL,
            meaning TEXT NOT NULL UNIQUE
        )
        """
    )


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

    print(dictionary)


definitions = define(words)
make_dict(letters, definitions)
