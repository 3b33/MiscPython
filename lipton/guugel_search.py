from googlesearch import search

names = ["\digika\"", "ahlo"]
for name in names:
    for f in search(name):
        print(f)

