#! /usr/bin/python3
import textwrap
from pathlib import Path
import shutil
import glob
import argparse


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 description=textwrap.dedent(
                                     '''Script Python permettant de renommer des fichiers en masse.
                                     \nAuteur: psy
                                     \nATTENTION: Le processus peut être lent si le nombre de fichiers à renommer est 
           grand.'''), prog="koma_files v1.0")
parser.add_argument('-p', '--path', type=str, dest='src_path', help='Le repertoire contenant les fichiers à renommer. '
                                                                    'Ce paramètre doit être fourni.')
parser.add_argument('-t', '--type', type=str, dest='files_type', help='Le type ou extension des fichiers à modifier. Ce'
                                                                      ' paramètre doit être fourni. Exemples de types'
                                                                      ' de fichiers: jpg, png, mp4, ...')
parser.add_argument('-a', '--prefix', type=str, dest='files_prefix', help="Le préfixe donné aux fichiers. "
                                                                          "Exemple de préfixe: image_, image, photo, "
                                                                          "photo_, ...")
parser.add_argument('-d', '--dest', type=str, dest='files_dest', help='Le repertoire de destination des '
                                                                      'fichiers renommés')
parser.add_argument('-v', '--verbose', action='store_true', help='Activé/désactivé le mode verbose')

args = parser.parse_args()

if args.src_path and args.files_type:
    if args.verbose:
        src_path = Path(args.src_path)

        # Si c'est un repertoire
        if src_path.is_dir():
            print(f"Les fichiers d'extension {args.files_type} vont être renommés")

            response = input("Voulez-vous poursuivre ? (o/n): ")

            if str(response.strip().lower()) == 'o':
                # On crée une liste contenant tous les fichiers dont l'extension correspond
                files = glob.glob('*.' + str(args.files_type), root_dir=src_path.absolute())
                index = 0  # Un numéro de fichier

                # Si aucun fichier de ce type
                if len(files) == 0:
                    print('Aucun fichier de ce type trouvé dans le répertoire source')
                # Si au moins un fichier de ce type trouvé
                else:
                    # Si le repertoire de destination est fourni
                    if args.files_dest:
                        dest = Path(args.files_dest)

                        # On vérifie si le repertoire de destination existe
                        if dest.is_dir():
                            # On vérifie si un préfixe a été fourni
                            if args.files_prefix:
                                # On modifie chaque fichier selon les paramètres fournis
                                for file in files:
                                    # Le nouveau nom fichier précédé par son emplacement
                                    new_file = str(dest.absolute()) + '/' + str(args.files_prefix) + '_' + str(index) +\
                                               '.' + args.files_type
                                    shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                    print(f'Fichier {file} renommé avec succès')
                                    index += 1
                            # Si aucun préfixe n'a été fourni
                            else:
                                # On modifie chaque fichier selon les paramètres fournis
                                for file in files:
                                    # Le nouveau nom fichier précédé par son emplacement
                                    new_file = str(dest.absolute()) + '/' + str(index) + '.' + args.files_type
                                    shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                    print(f'Fichier {file} renommé avec succès')
                                    index += 1
                            print(f'Tous les fichiers ont été renommés avec succès. Un total de {index} fichiers')
                        else:
                            print("Le repertoire de destination est incorrecte ou n'existe pas")
                    # Si on n'a pas fourni de repertoire de destination
                    else:
                        # On vérifie si un préfixe a été fourni
                        if args.files_prefix:
                            # On modifie chaque fichier selon les paramètres fournis
                            for file in files:
                                # Le nouveau nom fichier précédé par son emplacement
                                new_file = str(src_path.absolute()) + '/' + str(args.files_prefix) + '_' + str(index) +\
                                           '.' + args.files_type
                                shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                print(f'Fichier {file} renommé avec succès')
                                index += 1
                        # Si aucun préfixe n'a été fourni
                        else:
                            # On modifie chaque fichier selon les paramètres fournis
                            for file in files:
                                # Le nouveau nom fichier précédé par son emplacement
                                new_file = str(src_path.absolute()) + '/' + str(index) + '.' + args.files_type
                                shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                print(f'Fichier {file} renommé avec succès')
                                index += 1

                        print(f'Tous les fichiers ont été renommés avec succès. Un total de {index} fichiers')

        else:
            print("Le repertoire (ou chemin de repertoire) mentionné n'existe pas ou est incorrecte")
    else:
        src_path = Path(args.src_path)

        # Si c'est un repertoire
        if src_path.is_dir():
            print(f"Les fichiers d'extension {args.files_type} vont être renommés")

            response = input("Voulez-vous poursuivre ? (o/n): ")

            if str(response.strip().lower()) == 'o':
                # On crée une liste contenant tous les fichiers dont l'extension correspond
                files = glob.glob('*.' + str(args.files_type), root_dir=src_path.absolute())
                index = 0  # Un numéro de fichier

                # Si aucun fichier de ce type trouvé
                if len(files) == 0:
                    print("Aucun fichier de ce type trouvé dans le répertoire fourni")
                # Si au moins un fichier de ce type trouvé
                else:
                    # Si le repertoire de destination est fourni
                    if args.files_dest:
                        dest = Path(args.files_dest)

                        # On vérifie si le repertoire de destination existe
                        if dest.is_dir():
                            # On vérifie si un préfixe a été fourni
                            if args.files_prefix:
                                # On modifie chaque fichier selon les paramètres fournis
                                for file in files:
                                    # Le nouveau nom fichier précédé par son emplacement
                                    new_file = str(dest.absolute()) + '/' + str(args.files_prefix) + '_' + str(index) +\
                                               '.' + args.files_type
                                    shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                    index += 1
                            # Si aucun préfixe n'a été fourni
                            else:
                                # On modifie chaque fichier selon les paramètres fournis
                                for file in files:
                                    # Le nouveau nom fichier précédé par son emplacement
                                    new_file = str(dest.absolute()) + '/' + str(index) + '.' + args.files_type
                                    shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                    index += 1
                            print(f'Tous les fichiers ont été renommés avec succès. Un total de {index} fichiers')
                        else:
                            print("Le repertoire de destination est incorrecte ou n'existe pas")
                    # Si on n'a pas fourni de repertoire de destination
                    else:
                        # On vérifie si un préfixe a été fourni
                        if args.files_prefix:
                            # On modifie chaque fichier selon les paramètres fournis
                            for file in files:
                                # Le nouveau nom fichier précédé par son emplacement
                                new_file = str(src_path.absolute()) + '/' + str(args.files_prefix) + '_' + str(index) +\
                                           '.' + args.files_type
                                shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                index += 1
                        # Si aucun préfixe n'a été fourni
                        else:
                            # On modifie chaque fichier selon les paramètres fournis
                            for file in files:
                                # Le nouveau nom fichier précédé par son emplacement
                                new_file = str(src_path.absolute()) + '/' + str(index) + '.' + args.files_type
                                shutil.move(str(src_path.absolute()) + '/' + file, new_file)
                                index += 1

                        print(f'Tous les fichiers ont été renommés avec succès. Un total de {index} fichiers')

        else:
            print("Le repertoire (ou chemin de repertoire) mentionné n'existe pas ou est incorrecte")
else:
    parser.print_help()
