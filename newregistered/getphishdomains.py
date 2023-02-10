



filename = input("Filename: ")


words = ["afad","ahbap","yardim","bagis","crypto","destek"]

with open(filename) as file:
    lines = [line.rstrip() for line in file]
    print (len(lines))
    for i in range(len(lines)):
        for j in range(len(words)):
            if words[j] in lines[i]:
                print(lines[i])