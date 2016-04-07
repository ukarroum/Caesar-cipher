#!/usr/bin/python3

#############################################
# Auteur    :   Yassir Karroum 
#               [ukarroum17@gmail.com] 
#               [https://github.com/ukarroum]

# Description   : Un petit script qui chiffre via chiffre de César il permet
#                 aussi de déchiffrer un text chiffré avec ce dernier
#############################################

import getopt
import sys

g_opts = {'chiffrer' : 1,
        'key' : 0,
        'filein' : sys.stdin,
        'fileout' : sys.stdout}

def print_help():
    """Affiche l'aide du script """
    
    print("Usage: python3 caesar [OPTION] ... [FILE] ...")
    print("Un petit script qui chiffre via chiffre de Cesar il permet aussi de dechiffrer un text chiffre avec ce dernier .\n")
    
    print("Options : ")
    print("\t--chiffre=CAESAR_KEY\t Le texte en entré est chiffre via CAESER_KEY, ne peut pas etre utilisé mutuellement avec l'option --dechiffre")
    print("\t--dechiffre\t Le texte en entré est dechiffre sans avoir besoin d'une clé ")
    print("\t--filein=FILE\t Le fichier content le texte en entré (par défaut entré standard" )
    print("\t--fileout=FILE\t Le fichier ou le texte en sortie sera stoké (par défaut sortie standard")

###### Chiffrement #########

def chiffrer(key, filein, fileout):
    """ Chiffre à l'aide du chiffre de César"""

    #Lecture
    if filein == sys.stdin:
        f = sys.stdin
    else:
        f = open(filein, 'r')
    inp = f.read()
    f.close()

    #Chiffrage
    inp = inp.lower()
    key = key % 26 #Pour éviter des itérations inutiles .
   
    inp = list(inp)
    for i in range(len(inp)):
        if inp[i] == ' ' or inp[i] == '\n':
            continue
        if ord(inp[i]) + key <= ord('z'):
            inp[i] = chr(ord(inp[i]) + key)
        else:
            inp[i] = chr(ord(inp[i]) + key - ord('z') + ord('a') - 1)

    inp = "".join(inp) 

    #Ecriture
    if fileout == sys.stdout:
        f = sys.stdout
    else:
        f = open(fileout, 'w')
    f.write(inp)
    f.close()

def dechiffrer(filein, fileout):
    """ Dechiffre un texte sans clé """

    #Lecture
    if filein == sys.stdin:
        f = sys.stdin
    else:
        f = open(filein, 'r')
    inp = f.read()
    f.close()

    # Calcul des frequences
    freq = [0.0]*26

    inp = inp.lower()
    for i in range(len(inp)):
        if inp[i] == ' ' or inp[i] == '\n':
            continue
        freq[ord(inp[i]) - ord('a')] += 1
    for i in range(26):
        freq[i] = freq[i] / len(inp)

    # Calcul de la clé
    charMax = chr(freq.index(max(freq)) + ord('a'))
    
    if charMax <= 'e':
        chiffrer(ord('e') - ord(charMax), filein, fileout)
    else:
        chiffrer(26 - (ord(charMax) - ord('e')), filein, fileout)

 
###### Main ##############

try:
    opts, args = getopt.getopt(sys.argv[1:], "", ["help", "chiffre=", "dechiffre", "filein=", "fileout="])
except:
    print_help()
    sys.exit(-1)

for opt, arg in opts:

    if opt == '--help':
        print_help()
        sys.exit(0)
    if opt == '--chiffre':
        g_opts['chiffrer'] = 1
        g_opts['key'] = int(arg)
    if opt == '--dechiffre':
        g_opts['chiffrer'] = 0
    if opt == '--filein':
        g_opts['filein'] = arg
    if opt == '--fileout':
        g_opts['fileout'] = arg

if(g_opts['chiffrer']):
    chiffrer(g_opts['key'], g_opts['filein'], g_opts['fileout'])
else:
    dechiffrer(g_opts['filein'], g_opts['fileout'])
