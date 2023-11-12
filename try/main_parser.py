import re

patterns = "|".join(
    # HACK: in case it isn't used very often, change it
    # to a simple string and separate each pattern with the | pipe
    [
        r"\d+\n",
        r"Espacio Disponible\n",
        r"Ambrose Gwinet Bierce?",
        r"Diccionario del Diablo\n",
        r"www.elaleph.com\n",
        r"donde los libros son gratis\n",
    ]
)

compiled = re.compile(
    patterns,
    re.MULTILINE,
)

with open("src/Diabolous.txt", "r") as blob:
    # TODO: Use the original file and write a copy with the parser aplied
    with open("src/edited_diabolous.txt", "w") as new:
        new_blob = re.sub(
            compiled,
            "\n",
            blob.read(),
        )
        print(new_blob)
        new.write(new_blob)

    print("DONE..!")
