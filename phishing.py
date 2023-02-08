import itertools

fp = open("domains.txt", "a")

with open("brute.txt") as f:
    words = [word.strip() for word in f]

fs = open("tekil.txt", "a")


stri = ""

for s in itertools.permutations(words, 1):
    stri = str("https://"+s[0] + ".com")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".net")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".org")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".xyz")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".biz")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".co")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".ru")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".site")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".com.tr")
    fp.write(stri+"\n")
    stri = str("https://"+s[0] + ".cf")
    fp.write(stri+"\n")        


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
    stri = str("https://"+p[0]+ p[1]+ ".co")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".ru")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".com.tr")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".cf")
    fp.write(stri+"\n")
    stri = str("https://"+p[0]+ p[1]+ ".site")
    fp.write(stri+"\n")
    #stri = str("https://twitter.com/"+p[0]+ p[1]) //validate httpx
    #fp.write(stri+"\n")

#delete startswith - 

file1 = open('domains.txt', 'r')
file2 = open('domainsupdated.txt','w')
 
for line in file1.readlines():

    if not (line.startswith('https://-')):
        file2.write(line)
 
file2.close()
file1.close()

