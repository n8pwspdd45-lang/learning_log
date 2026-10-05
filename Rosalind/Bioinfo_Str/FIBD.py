def main():
    n = int(input("how many months: "))
    m = int(input("how many months they live: "))

    rabbits_couples = count(n, m)
    print(f"Couples number after {n} months: {rabbits_couples}")
    


def count(n, m):
    ls = [0] * m
    ls[0] = 1 
    fib = [ls[0]]
    for i in range(n-1):
        ls.insert(0, sum(ls[1:]))
        ls.pop()
        fib.append(sum(ls))

    return fib[-1]

if __name__ == "__main__":
    main()