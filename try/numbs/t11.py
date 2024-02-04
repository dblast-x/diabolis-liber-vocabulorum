import re


def pick_types():
    """
    Creates a list of types
    """
    with open("t_src/edit.txt", "r") as f:
        patterns = "|".join(
            [
                "^[A-Z][\w]+, (s[.])",
                "^[A-Z][\w]+, (adj[.])",
                "^[A-Z][\w]+, (v[.]i[.])",
            ]
        )
        compiled = re.compile(patterns)
        types = list()
        for line in f:
            line = line.rstrip()
            match = re.findall(patterns, line)
            if match:
                types.append(match)
            else:
                continue
        print(types)

        type_list = set(
            [alpha for sublist in types for typ in sublist for alpha in typ if alpha]
        )

        return type_list


print(pick_types())
