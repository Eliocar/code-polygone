# PARTIE 1 : géométrie des polygones dans le cercle unité :

# afficher le cercle unité puis ajouter le polygone à n cotés sur python

import matplotlib
matplotlib.use('TkAgg')  # Force l'utilisation d'un backend compatible avec PyCharm

import matplotlib.pyplot as plt

# Créer la figure et les axes
fig, ax = plt.subplots()

# Définir les limites des axes
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)

# Afficher la grille pour repérer les points
ax.grid(True)
ax.set_axisbelow(True)

# Forcer l’aspect carré (x et y à même échelle)
ax.set_aspect('equal')

# Étape 2 : Créer le cercle (centre x=0.5, y=0.5, rayon=0.3)
cercle = plt.Circle((0, 0), 1, color='black', fill=False, linestyle ='--', linewidth=1, zorder=0)

# Étape 3 : Ajouter le cercle à l'axe
ax.add_patch(cercle)

# → ligne horizontale (parallèle à X)
ax.axhline(y=0, color='grey', linewidth=1.5)
# → ligne verticale (parallèle à Y)
ax.axvline(x=0, color='grey', linewidth=1.5)

# Rendre les axes du bas et de gauche visibles et en gras
ax.spines['left'].set_linewidth(2)
ax.spines['bottom'].set_linewidth(2)

# Ajouter des ticks (graduations) sur les axes
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')


import math
import sympy


def est_de_fermat(p):
    if not sympy.isprime(p) :
        return False
    if not ((p-1)%2==0) :
        return False
    n = p-1
    if not math.log2(n).is_integer() :
        return False
    else :
        m = math.log2(n)
        if not math.log2(m).is_integer() :
            return False
    return True


def constructible(n) :
    while n%2==0 :
        n= n//2
    facteurs = sympy.factorint(n)  # Dictionnaire {facteur: exposant}
    for p in facteurs:
        if not facteurs[p] == 1 :
            return False
        if not est_de_fermat(p):
            return False
    return True

def polygone(n) :
   if not constructible(n) :
     return "ce polygone n'est pas constructible"
   else :
    for i in range(n):
      x1 = math.cos((2*i*math.pi)/n)
      y1 = math.sin((2*i*math.pi)/n)
      x2 = math.cos((2*(i+1)*math.pi)/n)
      y2 = math.sin((2*(i+1)*math.pi)/n)
      plt.plot([x1,x2],[y1,y2], color='blue', linewidth=1.5, zorder=1)
      plt.scatter([x1], [y1], color='black', s=20, zorder=2)
    plt.title(f"Polygone régulier à {n} cotés")
    print("ce polygone est constructible")


# Tester les entiers de 1 à 25
#for n in range(1, 26):
# statut = "✅ constructible" if constructible(n) else "❌ non constructible"
# print(f"{n:2} → {statut}")


print(polygone(9))

#plt.show()

# PARTIE 2 : cyclotomic polynomial :


from sympy import symbols, Poly, sympify, cyclotomic_poly, is_primitive_root, gcd_list, gcd_terms

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
#print(l)

# PARTIE 3 : polynome cyclo dans le cercle unité :

#fonction 1 : liste des k premiers avec n :
def list_k_et_n_prem(n) :
    l = []
    for k in range(n) :
        if math.gcd(k,n) == 1 :
            l.append(k)
    return l

#fonction 2 : coordonnées des racines primitives :
def coord_prim(n) :
    l = list_k_et_n_prem(n)
    for k in l :
        x1 = math.cos((2 * k * math.pi) / n)
        y1 = math.sin((2 * k * math.pi) / n)
        plt.scatter([x1], [y1], color='black', s=20, zorder=2)

print(coord_prim(9))
plt.show()

