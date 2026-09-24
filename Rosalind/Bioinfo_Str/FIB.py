def main():
    n = int(input("how many months: "))
    k = int(input("how many newborn each generation: "))

    serie = count(k, n)
    print(f"Couples number after {n} months: {serie[-1]}")
    


def count(k, n):
    serie = []

    if n == 1:
        serie.append(1)
        return serie

    elif n == 2:
        for i in range(1, 3):
            serie.append(1)
        return serie

    elif n > 2:
        for i in range(1, 3):
            serie.append(1)
        for i in range(2, n):
            couples = serie[i-1] + k * serie[i-2]
            serie.append(couples)
        return serie 

    else:
        print("Error")
        

if __name__ == "__main__":
    main()