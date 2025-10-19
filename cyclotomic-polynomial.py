from sympy import symbols, Poly, sympify, cyclotomic_poly

x = symbols('x')

# fonction 1 : liste coeff version sympy
def list_coeffs(p):
    p_str = str(p)
    p_str = p_str.replace("_x", "x").replace(" ", "")
    expr = sympify(p_str)
    poly = Poly(expr, x)
    return poly.all_coeffs()

# fonction 2 : dico coeff
def dico_cf(p) :

    str_p = str(p)
    str_p = str_p.replace(" ","").replace("_","").replace("-","+-")
    str_p = "+" + str_p

    l = str_p.split("+")
    d = {}

    if "x" not in l[len(l) - 1]:
        d[int('0')] = int(l[(len(l) - 1)])

    for term in l :
        if term == "" or "x" not in term:
            continue

        if "-x" in term :
             term = term.replace("-x","-1*x")
        elif "x" in term and "*x" not in term :
             term = term.replace("x","1*x")


        if "*x**" in term :
          (a,b,c) = term.partition("*x**")
          d[int(c)] = int(a)

        if "*x" in term and "*x**" not in term :
          (a,b,c) = term.partition("*x")
          d[1] = int(a)

    return d

#_x = symbols('_x')
#p = cyclotomic_poly(11) #"- _x**6 + 3*_x**4 - 2*_x**2 + _x - 1
#print(p)
#print(dico_cf(p))

# fonction 3 : liste coeff version dur
def list_cf(p):
    d = dico_cf(p)
    max_deg = max(d.keys())
    return [d.get(i, 0) for i in range(max_deg + 1)]


# fonction 4 : degré polynome
def deg_poly(p) :
    deg = len(list_cf(p))-1
    return deg


# fonction 5 : résumé polynome
def polynome(p) :
    d = deg_poly(p)
    l = list_cf(p)
    return (p,l,d)

#print(polynome(cyclotomic_poly(3)))

l = [polynome(cyclotomic_poly(i)) for i in range(1,105)]
print(l)

