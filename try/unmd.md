`
patterns = "|".join([
    r"^[A-Z][\w]+,\ss.\sy\sadj.",
    r"^[A-Z][\w]+,\ss.",
    r"^[A-Z][\w]+,\sv.t.",
    r"^[A-Z][\w]+,\sv.i.",
    r"^[A-Z][\w]+,\sadj.\sy\ss.",
])
\
\
def word_picker(file: str):
    if len(file) < 1:
        with open("src/edited_diabolous.txt", "r") as f:
            print("Find the Pattern.")
            pattern = re.compile(
                r"^[A-Z][\w]+,\ss.|^[A-Z][\w]+,\sv.t.|^[A-Z][\w]+,\sv.i.|^[A-Z][\w]+,\sadj.\sy\ss."
            )  # [svtiadj.]+
            for line in f:
                line = line.rstrip()
                match = re.findall(pattern, line)
                # print(line)
                if match:
                    print(match, "found!")
                else:
                    continue
`
