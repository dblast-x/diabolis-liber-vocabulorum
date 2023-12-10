"""
# A none initial value is valid.

letters = ["a", "b", "c", "d"]

definition = dict()
for letter in letters:
    definition[letter] = None
    for x in range(4):
        definition[letter] = x
"""
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


def new_logic(letters, words):
    end, start = 1, 0
    _ = input("!!Start!!")
    with open("try/abc/tst.txt", "r") as f:
        file = f.read()
        lenght = range(len(words))
        dictionary = dict()
        for letter in letters:
            dictionary[letter] = None

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
                # for l in dictionary:
                print(definition)
            else:
                continue
            start += 1
            end += 1
        print(start, end)


new_logic(letters, words)
