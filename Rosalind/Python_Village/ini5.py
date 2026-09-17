name_filein = input("File name? ")
name_fileout = "Even-numbered_lines_from_ini5.txt"


with open(name_filein) as fin:
    even_lines = fin.readlines()[1::2]
    with open(name_fileout, 'w') as fout:
        for line in even_lines:
            line = line.strip()
            fout.writelines(f"{line}\n")
