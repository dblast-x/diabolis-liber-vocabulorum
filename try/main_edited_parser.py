import re

patterns = "|".join(
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
    with open("src/edited_diabolous.txt", "w") as new:
        new_blob = re.sub(
            compiled,
            "\n",
            blob.read(),
        )
        new.write(new_blob)
        print("DONE..!")
