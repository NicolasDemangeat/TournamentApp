# Tournament Application
Application de gestion de tournois d'échec.

## *Table des matières*
1. [Prérequis](#1-prérequis)
2. [Informations générales](#2-informations-générales)   
3. [Exécuter le script](#3-exécuter-le-script)
4. [Fonctionnement](#4-fonctionnement)
5. [Futures améliorations](#5-futures-améliorations)
6. [Auteur](#6-auteur)

## 1. Prérequis
Pour pouvoir exécuter les scripts il nécessaire d'installer la version 3.9.0 de python : 
https://www.python.org/downloads/release/python-390/

## 2. Informations générales
   TournamentApp est une application hors ligne de gestion de tournoi d'échec, avec sauvegarde en base de données et génération de rapports.
  Le système de création de match est le système Suisse.
  
  Vous allez dans un premier temps créer un tournoi, puis les joueurs participants à ce tournoi.
  
  Vous pouvez affichez ensuite différents rapports :
  - Liste de tous les acteurs :
    - par ordre alphabétique
    - par classement
  - Liste de tous les joueurs d'un tournoi :
    - par ordre alphabétique
    - par classement
  - Liste de tous les tournois.
  - Liste de tous les tours d'un tournoi.
  - Liste de tous les matchs d'un tournoi. 


## 3. *Exécuter le script*
Après avoir téléchargé TournamentApp-main.zip depuis GitHub, il faut l'extraire dans un dossier de votre choix.   
Ensuite, en utilisant l'invite de commandes Windows (ou le terminal si vous êtes sur Mac ou Linux) :  
- Placez vous dans le dossier  
- Créez un environnement virtuel  
- Activez le  
- Installez les modules depuis requirements.txt
### Pour windows
```
$ CD /chemin/vers/TournamentApp-main
$ python -m venv env
$ env\Scripts\activate
$ py -m pip install -U pip
$ pip install -r requirements.txt
```
Vous pouvez maintenant exécuter le script.
```
$ python main.py
```
### Pour Unix
```
$ cd /chemin/vers/TournamentApp-main
$ python3 -m venv env
$ source env/bin/activate
$ python3 -m pip install -U pip
$ pip install -r requirements.txt
```
Vous pouvez maintenant exécuter le script.
```
$ python3 main.py
```

## 4. *Fonctionnement*
L'application vous guide pas à pas a travers les différents choix possible.

## 5. *Futures améliorations*
Voici une liste des améliorations envisageable :
- Faire une interface graphique (ou web)
- ~~Possibilité de choisir parmis les joueurs déjà enregistrés en base de données.~~

## 6. *Auteur*
- Nicolas Demangeat > Profil : [CodeWars](https://www.codewars.com/users/Morkai) - [CodinGame](https://www.codingame.com/profile/12632339c7b1539aedc9bb480ed2cac44538993)
