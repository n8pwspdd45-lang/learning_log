DNA = input("DNA: ")

RNA = ""

for nt in DNA:
    if nt == "T":
        RNA += "U"
    else:
        RNA += nt

print(f"\n{RNA}")