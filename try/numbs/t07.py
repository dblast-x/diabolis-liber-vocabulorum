d = {
    "A": {"worda": 0, "word1": 1, "word2": 2},
    "B": {"wordb": 0, "word1": 1, "word2": 2},
    "C": {"wordc": 0, "word1": 1, "word2": 2},
}


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


set_db(d)
