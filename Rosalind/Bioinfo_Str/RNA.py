coding_DNA = input("DNA: ")

RNA = ""

for nt in coding_DNA:
    if nt == "T":
        RNA += "U"
    else:
        RNA += nt

print(f"\n{RNA}")