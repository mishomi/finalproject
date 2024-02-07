with open('example.txt', 'w') as file:
    for i in range(2, 18):
        if i == 2:
            file.write("ori\n")
        elif i == 8:
            file.write("rva\n")
        elif i == 10:
            file.write("ati\n")
        elif i == 13:
            file.write("tsameti\n")
        elif i == 17:
            file.write("chvidmeti\n")
        else:
            file.write("\n")
with open('example.txt', 'r') as file:
    reader = file.read()

    print(reader)
