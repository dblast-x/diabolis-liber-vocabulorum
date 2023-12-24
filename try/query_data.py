import sqlite3 as s3

"""
  word = "Abandonado"
  The single word value is not valid.. for they go
  with their type as well.
  e.g >> Abandonado, s. y adj.
"""

# word = input("What are you looking for?\n")


# TODO: search for a way to search an special element with sql.
conn = s3.connect("try/dict.db")
cur = conn.cursor()

words = cur.execute("SELECT * FROM Words")
for word in words:
    print(word)
    _ = input("continue\n")

# cur.execute("SELECT * FROM Words WHERE word = ?", (word,))

print(cur.fetchone())
