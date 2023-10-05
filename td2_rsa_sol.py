#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Mathieu Cunche : mathieu.cunche@insa-lyon.fr

import math

def encodage(s):
    l = []
    s1 = ""
    for c in s:
        s1+=(str(ord(c)-ord('a')+1).rjust(2,'0'))
    n = 3
    chunks = [s1[i:i+n] for i in range(0, len(s1), n)]
    for i in chunks:
        l.append(int(i))
    return l

def decodage(l):
    s = ""
    s1 = ""
    for i in l:
        s1+=str(i).rjust(3,'0')
    n=2
    chunks = [s1[i:i+n] for i in range(0, len(s1), n)]
    for i in chunks:
        s+=f"{chr(int(i)+ord('a')-1)}"
    return s

p = 223
q = 307
n = p * q
phi = (p-1)*(q-1)
print(f"phi = {phi}")
e = 5 
print(f"e = {e}")
print(f"pgcd(e,phi) = {math.gcd(phi,e)}")
d = pow(e,-1,phi)

# chiffrement

clair = [31,825,162,15]
print(f"clair={clair}")
chiffre = []

for i in clair :
    chiffre.append(pow(i,e,n))

print(f"chiffre={chiffre}")


# dechiffrement
dechiffre = []
for i in chiffre :
    dechiffre.append(pow(i,d,n))

print(f"dechiffre={dechiffre}")

# encodage decodage
print(encodage("crypto"))
print(decodage(encodage("crypto")))
