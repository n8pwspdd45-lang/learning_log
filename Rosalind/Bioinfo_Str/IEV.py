def main():
    AA_AA = int(input("AA-AA: "))
    AA_Aa = int(input("AA-Aa: "))
    AA_aa = int(input("AA-aa: "))
    Aa_Aa = int(input("Aa-Aa: "))
    Aa_aa = int(input("Aa-aa: "))
    aa_aa = int(input("aa-aa: "))

    # total_offspring = 2*(AA_AA + AA_Aa + AA_aa + Aa_Aa + Aa_aa + aa_aa)
    dominant_phenotype = 2*(AA_AA + AA_Aa + AA_aa + Aa_Aa * 0.75 + Aa_aa * 0.5)
    print(dominant_phenotype)

main()