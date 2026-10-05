def main():
    s = input("sequence s: ").strip().upper()
    t = input("sequence t: ").strip().upper()
    hamming_distance = count(s, t)
    print(f"Hamming distance is: {hamming_distance}")

def count(s1, s2):
    mismatches = 0
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            mismatches += 1
        else:
            pass

    return mismatches

if __name__ == "__main__":
    main()


