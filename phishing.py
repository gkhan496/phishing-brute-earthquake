import itertools

fp = open("domains.txt", "a")

with open("brute.txt") as f:
    words = [word.strip() for word in f]

stri = ""
for p in itertools.permutations(words, 2):
    stri = str("https://"+p[0]+ p[1]+ ".com")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".net")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".org")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".xyz")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".biz")
    fp.write(stri+"\n")



    

