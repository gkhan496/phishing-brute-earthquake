import glob




output = open("output.txt","a")

words = ["donate"]




read_files = glob.glob("resources/*.txt")
with open("allregistereddomains.txt", "wb") as outfile:
    for f in read_files:
        with open(f, "rb") as infile:
            outfile.write(infile.read())
    

with open("allregistereddomains.txt") as file:
    lines = [line.rstrip() for line in file]
    for i in range(len(lines)):
        for j in range(len(words)):
            if words[j] in lines[i]:
                output.write(lines[i]+"\n")