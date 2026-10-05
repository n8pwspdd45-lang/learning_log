import regex

def main():
    s = input("string s: ").strip().upper()
    t = input("substring t: ").strip().upper()

    if t in s:
        positions = regex.finditer(t, s.rstrip("\n"), overlapped=True)
        for i in positions:
            print(i.start()+1)

    else:
        print("not find")

main()