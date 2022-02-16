from googlesearch import search

names = ["\digika\""]
for name in names:
    for f in search(name):
        print(f)

