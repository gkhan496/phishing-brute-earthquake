import itertools

fp = open("domains.txt", "a")

with open("brute.txt") as f:
    words = [word.strip() for word in f]

fs = open("tekil.txt", "a")


stri = ""


tlds = [".com", ".net", ".org", ".xyz", ".biz", ".co", ".ru", ".site",
        ".com.tr", ".cf", ".ga", ".gq", ".fun", ".one", ".online",
        ".xn--p1ai", ".de", ".fr", ".es", ".store"]

for s in itertools.permutations(words, 1):
    for tld in tlds:
        stri = str("https://" +s[0] + tld)
        fp.write(stri+"\n")


for p in itertools.permutations(words, 2):
    for tld in tlds:
        stri = str("https://"+ p[0] + p[1] + tld)
        fp.write(stri+"\n")


# delete startswith -

file1 = open('domains.txt', 'r')
file2 = open('domainsupdated.txt','w')
 
for line in file1.readlines():
    if not (line.startswith('https://-')):
        file2.write(line)
 
file2.close()
file1.close()

#notes
# stri = str("https://twitter.com/"+subdomain+p[0]+ p[1]) //validate httpx
# fp.write(stri+"\n")
#subdomains = ["", "crypto.", "bagis.", "yardim."]
