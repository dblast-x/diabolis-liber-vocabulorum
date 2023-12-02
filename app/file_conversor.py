import re

patterns = "|".join(
    [
        r"\d+\n",
    ]
)

compiled = re.compile(
    patterns,
    re.MULTILINE,
)

with open("src/Diabolous.txt", "r") as text:
    with open("src/edited_diabolous.txt", "w") as new:
        new_text = re.sub(
            compiled,
            "",
            text.read(),
        )
        new.write(new_text)
        print("DONE..!")
