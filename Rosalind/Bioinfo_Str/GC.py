from Bio import SeqIO
from Bio.SeqUtils import gc_fraction
import sys

def main():
    file_fasta = sys.argv[1]
    records_dict = SeqIO.to_dict(SeqIO.parse(file_fasta, "fasta"))

    max_id = None
    max_gc = 0

    # Spacchettamento del dizionario attraverso items()
    # id_seq viene associato alla chiave, record al valore dalla funzione items()
    # id_seq è il nome della sequenza
    # record è un SeqRecord (contiene id, seq e altre informazioni)
    for id_seq, record in records_dict.items():
        gc = round((gc_fraction(record.seq) * 100), 6)
        if gc > max_gc:
            max_gc = gc
            max_id = record.id

    print(f"id: {max_id}\nfraction: {max_gc}%")

    
if __name__ == "__main__": 
    main()
