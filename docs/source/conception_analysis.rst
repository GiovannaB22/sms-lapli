.. _conception_analysis:

***********************************
Document de Conception et d'analyse
***********************************



* Application de gestion des collectes pluviométriques. *

Sommaire
========


* Avant-propos
* Introduction
* Présentation

1. Le projet
2. Les fonctionnalités du projet
3. Objectifs du projet
4. Les technologies utilisées

* Analyse

1. Choix des technologies
2. Structure du projet
3. Application Gestion de Données Pluviométrique


* Conception


1. Architecture du projet
2. Modèle de Base
3. Les interactions


* Annexe


Avant-propos
============

Créé en 1996, après l’échec des interventions massives d’aide alimentaire, au lendemain des réflexions et préoccupations soulevées par la préparation du sommet mondial de l’alimentation qui s’est tenu en novembre 1996,La Coordination Nationale de la Sécurité Alimentaire (CNSA) s’est  donnée pour objectif d’assurer l’harmonisation des interventions intersectorielles et inter-institutionnelles sur les problématiques complexes de politique alimentaire, de renforcement de la sécurité alimentaire et de gestion des risques.

Elle présente une structure étatique à trois niveaux. Tout d’abord, elle est coiffée par le Conseil interministériel de la sécurité alimentaire (CISA), qui représente le niveau décisionnel, qui est présidé par le ministre de l'agriculture. La CNSA elle-même, qui est le niveau technique, comprend la Coordination, une administration et un département technique. Le Conseil consultatif de la sécurité alimentaire, le troisième niveau, est ouvert à tous les autres acteurs de la société civile impliqués dans le secteur.

De ce fait, La CNSA, niveau technique en partenariat avec la CFR (Code For Résilience)qu’est une ?????? que la banque mondiale a mis sur pied dans le but de créer des groupes de programmeurs pouvant subvenir aux différents besoins techniques des organisations haïtiennes. Dans la même lancée nous (les 5 stagiaires (1)) avons été recrutés pour développer une application qui répondra à quelques difficultés techniques retrouvées au niveau de la CNSA.


Introduction 
============

La technologie au sein des entreprises et institution en Haïti se développe de jour en jour et une certaine automatisation des différentes données informatiques et analytiques dans certains secteurs sont maintenant disponibles. L’utilisation des interfaces web sont de plus en plus dense et les entreprises Haïtiennes se mettent à la disposition du public en exploitant la technologie la plus utilisée partout ailleurs, l’internet.

Dans ce contexte, la Coordination Nationale de la Sécurité Alimentaire (CNSA) avec l’aide de la CFR  décide de mettre sur pied un projet d’ application de gestion des collectes de données pluviométriques et des rapports des différents types de Marché afin d’atteindre certains objectifs qu’elle s’est fixée dans le cadre de sa mission.Ceux-ci consistent à influencer les politiques publiques de façon à améliorer les conditions de sécurité des aliments pour favoriser le développement alimentaire en Haïti.

Ce document prend en  compte une des parties du projet reliée sur la collecte de données pluviométriques. Durant trois mois, l’équipe de stagiaire aura à la développer et la perfectionner suivant les recommandations faites par les responsables de la CNSA durant les différentes rencontres  que nous avons effectuées.
l’analyse faite par les responsables des deux groupes c-a-d la banque mondiale via la CFR et la CNSA nous ont menés à l’utilisation des technologies open-source citées ci- dessous qui ont été un grand atout pour le développement et la concrétisation de ce projet.

*Présentation*

Le Projet
---------

Ce projet du nom smslapli est une application web qui s'occupe principalement de la gestion de collecte de données liées à la pluie et à l'alimentation.
En Haïti ces deux-là sont très liées. Pour gérer leur plantation et la cultiver jusqu’à la récolte, les agriculteurs et les paysans utilisent majoritairement l’eau de pluie.
Ce qui amène à dire que dans les saisons pluvieuses la récolte est abondante et dans les saisons sèches celle ci est assez maigre ou quasi inexistante.

Donc la CNSA avec l’application smslapli(2) sera en moyen de faire un rapport automatique des différentes données collectées et enregistrées  dans les différents départements par des agents ou collecteurs formés et équipés,
et ainsi elle pourra avoir l’oeil sur les différents changements sur ce sujet.


Les fonctionnalités du projet
------------------------------

Ce projet se présente sous la forme de différents modules indépendants et liés s'occupant chacun d'une partie de l'application web entière.
Dans ce document nous allons porter l'accent sur les modules qui se rapprochent beaucoup plus à la collecte de données Pluviométriques qu’à ceux du Prix de Marché.

Cette partie est formée de deux blocs de données du nom : Structure de Base et collecte Pluviométrique. chacun d’entre eux sont constitues de liens spécifiques qui reçoivent et enregistrent les différentes données envoyées par les collecteurs ou par un des responsable de la CNSA.

Cette application web a donc deux interfaces. Une interface publique pour les utilisateurs désireux d’être informés sur les multiples travaux de la CNSA et sur les rapports de collecte effectuée par cette dernière.
Une interface d’administration qui permet de faire la gestion des données collectées, de faire les rapports de ces données, de gérer les agents de terrain et les équipes de la CNSA etc. En gros c'est cette partie qui forme le moteur du projet en soi.
c'est aussi dans cet interface qu'il y a possibilité de voir les différentes applications qui forment ensemble l'application web qu’est le projet nommé "smslapli".


Objectifs du projet
-------------------
L'objectif du projet est de faciliter la collecte et le partage des données au sein de la CNSA.
Cet objectif sera atteint à travers les fonctionnalités suivantes:

Gestion des Observatoires
Gestion des Sites sentinelles
Gestion des Indicateurs
Gestion des pluviomètres
Gestion des collectes
Recherche par critère
Gestion des Graphs
Gestion des cartographies
Gestion des utilisateurs
Gestion des privilèges


Les technologies utilisées
--------------------------
Pour arriver à la concrétisation de ce projet, Les spécialistes ont du se mettre d'accord sur les technologies à utiliser. De même, qu'on le sait, les types de technologies pouvant accomplir de telles tâches sont nombreuses.
Pour cela ils ont dû se tourner vers les logiciels dit «open source» très puissant et assez simple à manipuler.
Tout en tenant compte des objectifs fixés ils ont alors placé leur choix sur celles déjà utilisées auparavant et ayant fait leur preuve au sein des entreprises.
Là encore le choix est encore vaste, Cependant la technologie ne cesse d’avancer il va falloir avancer avec en comparaison a l’avancement de celle ci le choix a été très vite fixé.


* Analyse *
***********

Avant même de citer les différents choix fixés, il va falloir faire un état des lieux en expliquant tout d’abord, le processus de l’acheminement des données collectées vers le bureau central de la CNSA.

Tout d’abord les pluviomètres sont placés dans chaque section communale de chaque commune des départements de la ville d ’ Haïti. Un collecteur part recueillir les données qui s’y trouvent, les note sur le formulaire que son chef de section lui a soumis et les lui ramène. À son tour le responsable de commune l’envoie à son responsable de département qui l’expédie   au bureau central se trouvant dans le département de l’Ouest. Toute cette passe passe de formulaire consomme un temps fou sans autant mettre de côté les possibilités de perte de données ou même de données erronées.

Choix des technologies
----------------------
La concretisation du projet a ete possible grace a l'utilisation des logiciels suivants:

* Django
* PostgreSQL
* RapidSMS
* Kannel
* Ansible
* Vagrant


Structure du projet
-------------------
Étant donné que c'est à partir du framework Django qu'il a été créé, il suit alors la structure imposée par celui là. de ce fait, il se présente sous forme d'un grand projet possédant divers types d’applications qui chacun se charge d'accomplir l'objectif fixé pour le projet en soi.


Application Gestion de Données Pluviométrique
---------------------------------------------
.. image:: _static/images/pluviometrie.png
   :align: center


*Conception*
*************
Dans le but d'ameliorer le processus pour la collecte de donnees, l'application smslapli ajoute en plus de lascencement du formulaire comme vu auparavant, il permet egalement un enregistrement automatique de ces donnees par les collecteurs  a partir d'un simple telephone portable.


Architecture du projet
----------------------

Le projet est une application web possédant deux interfaces; une interface publique qui sera pour tout le monde, pour leur permettre de s'informer, et une interface admin pour ceux qui auront des droits à l'interne.

.. image:: _static/images/.png
   :align: center

.. image:: _static/images/.png
   :align: center

Modèle de Base
--------------

.. image:: _static/images/.png
   :align: center


Les interactions
----------------




*Annexe*
*********
