import re

"""
Here are the ones that the main parser 
missed
"""


def sNy():
    with open("src/edited_diabolous.txt", "r") as f:
        print("Find the Pattern.")
        pattern = re.compile(r"(^[\w]+,\ss\.\sy\sadj\.)\s")
        for line in f:
            line = line.rstrip()
            match = re.findall(pattern, line)
            if match:
                print(match, "found!")
            else:
                continue


def yNs():
    with open("src/edited_diabolous.txt", "r") as f:
        print("Find the Pattern.")

        patterns = "|".join(
            [
                r"\d+\n",
            ]
        )
        compiled = re.compile(r"(^[A-Z][a-z]+,\sadj\.\sy\ss.)\s")
        for line in f:
            line = line.rstrip()
            match = re.findall(pattern, line)
            if match:
                print(match, "found!")
            else:
                continue


def parser_on():
    _ = input("Start..!")
    sNy()
    yNs()


if __name__ == "__main__":
    parser_on()
