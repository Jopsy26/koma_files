## koma_files

Script Python permettant de renommer des fichiers en masse

## Auteur

Jopsy O'Hara - jopsy.contact@gmail.com

## MODULES PYTHON UTILISÉS

1. glob
2. pathlib.Path
3. shutil
4. argparse

## USAGE

$ git clone https://github.com/Jopsy26/koma_files.git
$ cd ../path/to/the/file
$ python koma_files [-p repertoire_contenant_les_fichiers_à_renommer] [-t type_de_fichiers_à_renommer] [-a prefixe_utilisé] 
[-d repertoire_de_destination_des_fichiers] [-v mode_verbose]

NB: le repertoire contenant les fichiers et le type de fichiers doivent être fournis pour que le renommage soit effectif

## REMARQUE

Le système de fichier utilisé ici est basé sur Linux. Si vous l'utilisez sur un système Windows, veuillez remplacer les slash '/' par des anti-slash '\' pour éviter les erreurs éventuelles.

## SUGGESTIONS OU AMÉLIORATION

Pour toutes suggéstion ou amélioration de votre part, veuillez, je vous prie, me le faire part.
