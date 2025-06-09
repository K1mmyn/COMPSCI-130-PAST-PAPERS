def read_questions(filename):
    try:
        file = open(filename)
        content = file.read().split("\n")
        return [(f"{line.split('?')[0]}?", line.split("?")[1]) for line in content]; file.close()
    except FileNotFoundError:
        print(f"ERROR: The file '{filename}' does not exist.")
        return []