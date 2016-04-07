# Caesar Cipher

Un petit script qui chiffre des texts en clair avec le chiffre de cesar .
Il permet aussi de les déchiffrer sans clé .

Pour plus d'informations : [Chiffre de César](https://fr.wikipedia.org/wiki/Chiffrement_par_d%C3%A9calage)

# Utilisation

``` 
$ python3 caesar.py --help
 
Usage: python3 caesar [OPTION] ... [FILE] ...
Un petit script qui chiffre via chiffre de Cesar il permet aussi de dechiffrer un text chiffre avec ce dernier .

Options : 
	--chiffre=CAESAR_KEY	 Le texte en entré est chiffre via CAESER_KEY, ne peut pas etre utilisé mutuellement avec l'option --dechiffre
 	--dechiffre	 Le texte en entré est dechiffre sans avoir besoin d'une clé 
 	--filein=FILE	 Le fichier content le texte en entré (par défaut entré standard
 	--fileout=FILE	 Le fichier ou le texte en sortie sera stoké (par défaut sortie standard)
```
