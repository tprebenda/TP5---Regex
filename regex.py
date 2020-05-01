#!/usr/bin/python
import re

def carre(s):
    m = re.fullmatch(r"(.*)\1", s)
    return m.group(1) if m != None else None

def contientcarre(s):
    m = re.search(r"(..+)\1", s)
    return m.group(1) if m != None else None


def extraire_ligne(s, expr):
    m = expr.fullmatch(s)
    # cela renvoie un 4-uplet de la forme (a, n, i, p)
    return (m.group(1).strip(), m.group(2).strip(), m.group(3).strip(), 
            m.group(4).strip()) if m != None else None


def extraire_fichier(fichier, expr):
    d = {}

    with open(fichier) as f:
        for ligne in f:
            res = extraire_ligne(ligne, expr)
            if res:
                # cela crée des nouvelles variables pour 
                # chaque valeur du 4-uplet 'res'
                (a,n,i,p) = res

                if (p, a) in d:
                    # n est un str, en ce moment
                    d[(p,a)] += int(n)
                else:
                    d[(p,a)] = int(n)

    return d


def popularite(d):
    pop = {}
    for (p, a) in d.keys():
        if p in pop:
            pop[p] += d[(p, a)]
        else:
            pop[p] = d[(p, a)]
    
    return pop



def liste_prenoms(d):
    # on utilise UN ENSEMBLE pour eviter les doublons
    return list({p for (p,a) in d.keys()})




# Tests the functionality of above methods, and does some other Regex work:
if __name__== "__main__":
    print(carre("baba"))

    print(contientcarre("J'espere que toto est parti"))

    # 3:
    r = re.compile(r"(\d{4}),(\d*),(\d*),(.+)\n")
    m = r.fullmatch("1998,231,2,Toto\n")
    for i in range(1,5):
        print(m.group(i))

    print()
    print(extraire_ligne("1998,231,2,Toto\n", r))

    d = extraire_fichier("prenoms.txt", r)
    # cela devrait afficher 33932
    print(d[('Jean','1932')])

    pop = popularite(d)
    # cela devrait afficher 1962089
    print(pop['Jean'])

    prenoms = liste_prenoms(d)
    print()

    # EXERCISE 3,1:
    print(len([p for p in prenoms if carre(p.lower())]))

    # EXERCISE 3,2:
    print(len([p for p in prenoms if contientcarre(p.lower())]))

    # EXERCISE 3,3:
    print(len([p for p in prenoms if re.fullmatch(r"([a-z]|[A-Z]).*\1.*\1.*\1.*\1", p.lower())]))

    # EXERCISE 3,4:
    # print([p for p in prenoms if re.fullmatch(r"(a|e|i|o|u){4,}", p.lower())])
    print(len([p for p in prenoms if re.fullmatch(r"(a|e|i|o|u){4,}", p.lower())]))
