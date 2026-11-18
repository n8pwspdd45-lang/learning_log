# From https://youtu.be/Lsue2gEM9D0?si=p-BYqYh_y0CY5T6m
import pandas as pd
import numpy as np
import random as rd
from sklearn.decomposition import PCA
from sklearn import preprocessing
import matplotlib.pyplot as plt

# Geni che analiziamo (100) -> random
genes = ["gene" + str(i) for i in range(1,101)]

# Campioni in cui guardiamo i geni -> wild-type (5) e knock-out (5)
wt = ["wt" + str(i) for i in range(1,6)]
ko = ["ko" + str(i) for i in range(1,6)]

# Creiamo un "pandas DataFrame" per salvare i dati che abbiamo creato.
data = pd.DataFrame(columns=[*wt, *ko], index=genes)
""" Le liste wt e ko vengono unpacked dall'* in modo che i nomi delle colonne siano in un'unica lista:
[wt1, wt2, wt3, wt4, wt5, ko1, ko2, ko2, ko3, ko4, ko5]. Se non avessi usato * avrei ottenuto una lista
contenente due liste, io invece ne voglio una unica con i 12 nomi delle colonne (i miei campioni). 
I nomi dei geni sono usati come indice, ovvero sono i nomi delle colonne. """

# Creiamo i random data
for gene in genes:
    data.loc[gene, "wt1":"wt5"] = np.random.poisson(lam=rd.randrange(10,1000), size=5)
    data.loc[gene, "ko1":"ko5"] = np.random.poisson(lam=rd.randrange(10,1000), size=5)
""" Per ogni gene (1-100) creo 5 valori per ogni campione wt e 5 per ogni campione ko.
I dati arrivano da due distribuzioni di Poisson, una per wt e una per ko. 
Per ogni gene la media può variare tra 10 e 1000. """

# Stampa le prime 5 righe dei nostri dati (.head() -> metodo)
print(data.head())
""" È utile per verificare che i dati abbiano la formattazione che vogliamo. """

# Stampa le dimensione della nostra matrice di dati (shape -> attributo)
print(data.shape)
""" Righe x colonne """

# I need to center and scale my data
scaled_data = preprocessing.scale(data.T)
""" Dopo aver centrato, il valore medio per ogni gene sarà 0.
Dopo aver scalato, la deviazione standard per i valori sarà 1. 
Stiamo dando come argomento il traspose of the data. La funzione si aspetta di avere i campioni sulle righe 
invece che sulle colonne. I dataset genomici sono settati con i campioni in colonne, quindi diamo la matrice 
trasposta  (data.T) come argomento alla funzione scale(). """

# Creo un pggetto PCA
pca = PCA()
pca.fit(scaled_data) # dove vengono fatti tutti i conti per PCA (loading scores e quanto pesa ogni componente principale)
pca_data = pca.transform(scaled_data) # creazione coordinate per un grafico PCA basato sui loading scores e i dati scalati

# Inizio con un scree plot per vedere quante sono le componenti principali, che dovranno andare del grafico finale
# Variazione percentuale di ogni componente principale
per_var = np.round(pca.explained_variance_ratio_* 100, decimals=1)
labels = ["PC" + str(x) for x in range(1, len(per_var)+1)]

plt.bar(x=range(1, len(per_var)+1), height=per_var, tick_label=labels)
plt.ylabel("Percentage of Explained Variance")
plt.xlabel("Principal Component")
plt.title("Scree Plot")
plt.savefig("scree_plot.png", dpi=150)
plt.close()

pca_df = pd.DataFrame(pca_data, index=[*wt, *ko], columns=labels)

plt.scatter(pca_df.PC1, pca_df.PC2)
plt.title("My PCA Graph")
plt.xlabel("PC1 - {0}%".format(per_var[0]))
plt.ylabel("PC2 - {0}%".format(per_var[1]))

for sample in pca_df.index:
    plt.annotate(sample, (pca_df.PC1.loc[sample], pca_df.PC2.loc[sample]))

plt.savefig("PCA_graph.png", dpi=150)
plt.close()

""" Per capire quali geni sono responsabili del maggior discostamento sulle X """
loading_scores = pd.Series(pca.components_[0], index=genes)
sorted_loading_scores = loading_scores.abs().sort_values(ascending=False)

top_10_genes = sorted_loading_scores[0:10].index.values

print(loading_scores[top_10_genes])
            