# Clean data for extraction.
import re


with open("src/Diabolous.txt", "r") as text:
    with open("src/edit", "w") as new:
        pattern = re.compile("^\n*[A-Z]\n+|\d+\n", re.MULTILINE)
        new_text = re.sub(
            pattern,
            "",
            text.read(),
        )
        new.write(new_text)
        print("DONE..!")
