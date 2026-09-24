from Bio.Seq import Seq

def main():
    with open("RNA_seq.txt") as seq:
        for line in seq:
            AA_seq = Seq(line).translate(to_stop = True)

    with open("Protein.txt", 'w') as protein:
        protein.write(f"\nprotein: {AA_seq}")

if __name__ == "__main__":
    main()
