def read_content(filename="input.txt"):
    with open(filename) as f:
        t = f.read()
    return t.split("\n")[:-1]
