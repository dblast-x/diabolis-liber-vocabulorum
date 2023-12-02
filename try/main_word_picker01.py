"""
Steps >>
1. Find the uppercase letter.
2. Separate the *pattern from the meaning
3. Insert it into the DB.

Pattern >>
  * | startswith_capitalized_letter + one_or_more_linebreaks >>
  ( A \n)
  * | startswith_capitalized_word + coma + space + [letters + dot]s + space >>
  (Abstemio, s.  ) || (Abstemio, v. t.  )
"""

import re

with open("src/edited_diabolous.txt", "r") as file:
    print("Find the Letter.")
    for line in file:
        match = re.search(r"^[A-Z]\n+", line)
        if match:
            print("found!", match.group())
        elif match is None:
            continue
        else:
            print("Not found")
    print()
    print("Find the Pattern.")
    for line in file:
        line = line.rstrip()
        match = re.findall(r"(^[A-Z][a-z]+,\s.*)\s[A-Z][a-z]+", line)
        if match:
            # print(line) # D
            print(match, "found!")
        else:
            continue
