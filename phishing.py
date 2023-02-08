import itertools

fp = open("domains.txt", "a")

with open("brute.txt") as f:
    words = [word.strip() for word in f]

fs = open("tekil.txt", "a")


stri = ""

subdomains = ["", "crypto.", "bagis.", "yardim."]
tlds_csv = "top-level-domain-names.csv"
tlds = list(map(lambda x: x.replace("\n", ""), open(tlds_csv).readlines()))[1:]

for s in itertools.permutations(words, 1):
    for subdomain in subdomains:
        for tld in tlds:
            stri = str("https://"+subdomain+s[0] + tld)
            fp.write(stri+"\n")

for p in itertools.permutations(words, 2):
    for subdomain in subdomains:
        for tld in tlds:
            stri = str("https://"+subdomain+p[0] + p[1] + tld)
            fp.write(stri+"\n")
    # stri = str("https://twitter.com/"+p[0]+ p[1]) //validate httpx
    # fp.write(stri+"\n")

# delete startswith -

file1 = open('domains.txt', 'r')
file2 = open('domainsupdated.txt', 'w')

for line in file1.readlines():

    if not (line.startswith('https://-')):
        file2.write(line)

file2.close()
file1.close()
