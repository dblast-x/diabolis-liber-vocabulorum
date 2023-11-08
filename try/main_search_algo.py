import re

"""
TODO: Found the algorithm, improve it later on
"""


def main():
    clean_text()


def clean_text(text=""):
    if len(text) < 1:
        with open("src/Diabolous.txt") as f:
            pattern = re.compile(
                r"Espacio Disponible\n    Diccionario del Diablo\n    www.elaleph.com\n    donde los libros son gratis\n?",
                re.MULTILINE,
            )
            file = f.read()
            # print(file)
            cleaned = re.sub(pattern, "\n", file)

            print(cleaned)


if __name__ == "__main__":
    main()
