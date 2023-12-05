"""
    The right algo it's got to be a search from one
    definition-word to the other definition-word
    patterns = r"|".join(
        [
            "^[A-Z][\w]+, s. y adj.",
            "^[A-Z][\w]+, adj. y s.",
            "^[A-Z][\w]+, adj.",
            "^[A-Z][\w]+, adv.",
            "^[A-Z][\w]+, s.",
            "^[A-Z][\w]+, v.t.",
            "^[A-Z][\w]+, v.i.",
        ]
    )
"""
import re


def meaning_01(f: str):
    if len(f) < 1:
        with open("src/edited_diabolous.txt", "r") as file:
            print("Find the meaning.")
            file = file.read()
            pattern = re.compile(
                r"\n^[A-Z][\w]+, [svtiadj.]+ ([A-Z][\w]+.+)\n+^[A-Z][\w]+, [svtiadj.]+ ",
                re.MULTILINE | re.DOTALL,
            )
            matches = pattern.finditer(file)
            for match in matches:
                print(match.group())


def letter_picker():
    with open("src/edited_diabolous.txt", "r") as f:
        print("Find the Letter.")
        for line in f:
            match = re.search(r"^A\n+", line)
            if match:
                print("found!", match.group())
            elif match is None:
                continue
            else:
                print("Not found")


def create_file(name: str):
    with open(f"try/abc/{name}.txt", "w") as afile:
        with open("src/edited_diabolous.txt", "r") as f:
            print("Find the Letter.")
            for line in f:
                match = re.search(r"^A\n+", line)
                if match:
                    print("found!", match.group())
                elif match is None:
                    continue
                else:
                    print("Not found")

    print("Done")


if __name__ == "__main__":
    # meaning_01(_ := input(" <- + -> "))
    letter_picker()
    create_file("A")
