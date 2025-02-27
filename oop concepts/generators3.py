def read_large_file(filename):
    with open(filename, "r") as file:
        for line in file:
            yield line.strip()  # Yield each line lazily

for line in read_large_file("bigdata.txt"):
    print(line)  # ✅ Processes one line at a time, saving memory
