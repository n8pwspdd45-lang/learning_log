k = int(input("k(AA): "))
m = int(input("m(Aa): "))
n = int(input("n(aa): "))
tot = k+m+n

# Probabilità aa x aa
p1 = (n/tot) * ((n-1)/(tot-1))

# Probabilità Aa x aa
p2 = (m/tot) * (n/(tot-1)) * 2

# Probabilità Aa x Aa
p3 = (m/tot) * ((m-1)/(tot-1))

p_aa = p1 + p2*0.5 + p3*0.25

p_A = round((1 - p_aa), 5)

print(f"A- probability: {p_A}")
