DNA = input("DNA string to reverse: ").strip().upper()
DNA_reversed = "".join(reversed(DNA))
DNA_rc = ""

for nt in DNA_reversed:
    if nt == "A":
        DNA_rc +="T"
    elif nt == "T":
        DNA_rc += "A"
    elif nt == "C":
        DNA_rc += "G"
    else:
        DNA_rc += "C"

print(f"The reverse complement is: {DNA_rc}")
