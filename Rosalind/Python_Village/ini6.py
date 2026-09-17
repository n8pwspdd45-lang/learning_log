string_in = input("Frase: ").split(" ")

counting = {}

for word in string_in:
    # "in" controlla se word fa parte delle chiavi del dizioanrio, no valori
    if word not in counting:
        counting[word] = 1  # crea una nuova associazione
    else:
        counting[word] += 1  # aggiorna il valore della chiava a +1


# spacchetta la coppie, per ogni item del dizionario il primo elemento
# è la chiave il secondo il valore
with open("ini6_output.txt", 'w') as fout:
    for key, value in counting.items():
        fout.writelines(f"{key} {value}\n")