.. _users_guide:


.. image:: _static/images/index.jpeg
   :align: left
   :width: 85px
*****************************
MANUEL DE GUIDE D’UTILISATION
*****************************

* Application de gestion des collectes de données pluviométriques. *

Sommaire
********

* Avant-Propos
* Accès a l’application
* Interface du projet

1. interface utilisateur
2. interface administrateur

* Utilisation des fonctionnalités

1. fonctionnalités Sructure de Base
2. fonctionnalités Collecte Pluviométrique
3. fonctionnalités Autorisation
4. insertion des données collectées

* Scénarios

1.image collecteurs sans téléphone
2.image collecteurs avec téléphone

AVANT-PROPOS
************

Ce document est entièrement dédié à l’utilisation des membres de la CNSA afin d'améliorer et de renforcer la collecte des données pluviométriques.
Il démontre point par point les diverses fonctionnalités et donne une explication sur chacune d’entre elle.
Elle présente chacune des scénarios portant sur  l’utilisateur publique, à l’administrateur, ainsi que de ceux qui gèrent les entrées et sorties de l’application.
La plupart de ces scénarios seront accompagne d'images à titre d'exemple.


ACCÈS À L’APPLICATION
*********************

L’application SMS-LAPLI possède deux interfaces:

1. une interface publique
2. une interface administrative

L’interface publique ou encore \ **interface utilisateur** \ affichent des données susceptibles à être partagées à la population.
Ces dernières sont présentées dans le but d'informer la population Haïtienne  sur les conditions pluviométriques des divers départements, communes et sections communales du pays.

\ **L’interface administrative** \: (la plus riche des interfaces) est donc le moteur de l’avancement de tous les processus.
Elle sera donc gérée par (2)deux ou (3)trois administrateurs et une secrétaire pour les cas d’échéances de données erronées des collecteurs, ou d’arrêt ou suspension de services téléphoniques .
L'accès à cette interface sera entièrement sur la garde des membres de la CNSA.


INTERFACE DU PROJET
*******************
Le projet possede deux interfaces: Interface Utilisateur, Interface Administrateur.

Interface Utilisateur
=====================

(IMAGE DE L’INTERFACE)

.. image:: _static/images/interUtilisateur.png
   :align: center

Du haut de la fenêtre, un menu horizontal permet à l’utilisateur de naviguer dans les différentes parties de l’application.
Ce menu contient:

1. le logo de la CNSA: celui-ci mène vers le site initial déjà bien élaboré pour informer le public sur la Coordination Nationale de la Sécurité Alimentaire.
2. l’accueil: la première fenêtre qui apparaît à l’utilisateur. Celle ci contient deux boutons notés respectivement Pluviométrie et Prix du Marché conduisant à des informations concernant la pluviométrie et le Marché.
3. À côté de l’accueil ces 2 boutons se présentent sous forme de lien menant aussi à ces informations, ces liens seront sur toutes les autres fenêtres pour faciliter la navigation  sans pour autant se rendre à chaque fois dans la page principale pour pouvoir y accéder.


Interface Pluviométrie
----------------------


(IMAGE PAGE PLUVIOMÉTRIE)

.. image:: _static/images/pluviometrie.png
   :align: center


En plus de la barre de menu horizontal une nouvelle apparaît en vertical. celui- ci prend en compte les différentes représentations des rapports pluviométriques de la CNSA.
ce menu contient:

1. Aperçu: qu’est la présentation en (3) trois catégories des rapports de données pluviométriques pour  tous les critères présents dans la base de données. Soit celle des rapports globaux sur les données pluviométriques par départements, communes, sections communales.
Ces (3) catégories sont  des rapports présents sous forme de Graphe, de Tableau, et de carte. Il existe aussi une possibilité de filtrer ces derniers suivant des critères de sélections sous forme de menu déroulant se trouvant au haut de chaque présentation.

(IMAGE EXPLICATIVE Apercu)
.. image:: _static/images/pluviometrie.png
   :align: center

2. Rapports:

(IMAGE  EXPLICATIVE Rapportd)

.. image:: _static/.png
   :align: center


Interface administrative
========================

Pour accéder à l’interface d'administration , le bouton ADMIN situé au haut à gauche du menu horizontal  fait office de porte.
Contrairement à l’interface utilisateur, elle n’est accessible qu’à la saisie d’un username et d’un mot de passe administratif. Ceux qui ne seront créés que par un administrateur de la CNSA. En effet, seules les personnes concernées pourront y accéder.

(IMAGE ADMIN)

.. image:: _static/.png
   :align: center


Après la saisie du username et du mot de passe, la page suivante apparaît

(IMAGE DE L’ADMIN)

.. image:: _static/.png
   :align: center


La barre de menu est maintenant portée à gauche laissant la place à tous types de contenus disponible dans la base.
Tel que vu sur l'image:

1. Le Dashboard: la page d’accueil de l’interface administrateur
2. les Rapports: vu également dans l'interface utilisateur
3. La structure de base: permet de gérer les données concernant les départements, les communes, les sections communales, les sites sentinelles, les différents postes de la CNSA, et les personnes attribuées a ces postes.
4. La collecte pluviométrique: permet de gérer les données se rattachant à la pluviométrie telles que, le type de station, les stations, les observatoires, les unités de mesures de chaque station et des stations observatoires.
5. l'autorisation: fait la gestion des différents groupes et utilisateurs de l'ADMIN.

Le dashboard
------------

Cette page présente toutes les informations disponible dans la base de données:

* Au haut de la page à droite, 3 icônes apparaissent,
1. celle d'une enveloppe pour les notifications,
2. le logo de la CNSA
3. le username avec lequel,l'administrateur ou un responsable y a accédé.

Ce compte peut bien aussi être modifié par son propriétaires.
Pour des modifications au niveau du compte ADMIN il ne suffit que de faire un clic sur le UserName qui affiche les liens suivants: modifier le mot de passe, à propos, voir le site, et enfin Déconnexion.


(IMAGE DE mod. mot 2 pass)

.. image:: _static/images/modmo2pass.png
   :align: center

Pour la modification du mot de passe la personne doit tout d'abord taper l'ancien mot de passe dans la case correspondante ensuite elle devra insérer le nouveau  dans les deux autres cases suivantes et  pour finir un clic sur le bouton «modifier». Le nouveau mot de passe est alors mis-à-jour.


(IMAGE DE voir le site)

.. image:: _static/images/.png
   :align: center
Ce lien ci envoie directement sur l'interface utilisateur vu auparavant.
(IMAGE Deconnect)

.. image:: _static/images/.png
   :align: center
Après Déconnexion, les deux interfaces seront toujours accessibles.  le processus de demande d’accès pour l'interface administrateur est à nouveau opérationnel. la personne va devoir à nouveau entrer son mot de passe et son UserName pour pouvoir y accéder.

Rapports
--------

(IMAGE Rapports Admin)

.. image:: _static/images/.png
   :align: center
La page administrative présente tout comme celle du public:  une section pour les graphes, une autre pour les cartes de données pluviométriques, ainsi que les différents départements. elle présente également les agents actifs ou inactifs de la CNSA ainsi que les notifications de message des données collectées qui seront automatiquement insérées dans la table d'observations pluviométriques.


UTILISATION DES FONCTIONNALITES
*******************************
La gestion des données se fait  dans cette partie de l'application. Les données  peuvent ainsi être ajouter, supprimer, et modifier suivant les autorisations des utilisateurs et des personnes responsables de la CNSA qui vont pouvoir interagir dans la base où les données seront stockées et accessibles à tout moment.


Fonctionnalites Structure de Base
=================================

Dans la structure de base qui se présente sous la forme d'un menu déroulant, les liens cités précédemment s'y trouvent. Ce sont:

1. Départements
2. Communes
3. Sections communales
4. Sites sentinelles
5. Postes
6. Personnes Contacts

Chacun d'entre eux mène à une page respective, permettant soit d'ajouter, de modifier ou de supprimer les données les concernant. Cependant certains d'entre les liens sont pour ainsi dire relies entre eux. tels que chaque site sentinelle est intégrée dans une section communale, une section communale est reliée a une commune, et chaque personne contact doit être intégrée dans un poste. Dans ce cas l’ajout doit se faire tout d’abord des parents par exemple pour ajouter une nouvelle personne, il faut tout d’abord l’attribuer à un poste, de ce fait le poste devra donc être ajouter en premier.
il faut alors suivre l'ordre tel qu'il est indiqué sous la structure de base. En premier lieu, ajouter les départements et ainsi de suite. Ce qui ne veut pas dire qu'un ajout quelconque ne peut se faire autrement.
Dans le cas où le lien précédant soit vide l'application elle même vous enverra des warning pour vous montrer qu'il va falloir ajouter tout d'abord dans ce dernier avant de pouvoir continuer.



(IMAGE aJOUT NORMAL)

.. image:: _static/.png
   :align: center


(IMAGE ajout avec erreur)

.. image:: _static/.png
   :align: center

 IMAGE ajout Personne Contact)

.. image:: _static/.png
   :align: center
Le lien Personne Contact fait référence aux personnes travaillant à la CNSA ainsi que les collecteurs. Chaque personne sera attribuée à son poste tel qu’indiquer sur l'image.

Pour chacun des liens cités précédemment, certaines de leur case à remplir peuvent être facultatif pour cela, l'application via un message de warning( Une petite note apparaissant à côté des cases  ) vous montre celles qui sont obligatoires.
Les données ne seront enregistrées que quand toutes les cases obligatoires seront remplies.


Fonctionnalites Collecte Pluviometrique
=======================================


La collecte Pluviométrique se présente elle aussi sous forme de menu déroulant comportant les indications suivantes:

1. Type  Stations
2. Stations
3. Observations Pluviométriques
4. Observateurs
5. Unité Mesures
6. logs

IMAGE collecte ajout)

.. image:: _static/.png
   :align: center


Les restrictions faites pour la structure de base sont aussi attribuées à la collecte pluviométrique. En plus de pouvoir enregistrer les données sur l'application, cette partie admet aussi l’enregistrement des données pluviométriques collectées par les agents de terrain à partir d’un téléphone portable et les place automatiquement dans le lien dit: Observations Pluviométriques.
Cependant ces données ne seront acceptées que si et seulement si le collecteur est enregistré dans la base Personne Contact en tant qu'observateur et que le numéro de téléphone avec lequel il envoie les données est aussi enregistrées dans la base.
Dans le cas contraire, aucune donnée ne sera acceptée, si les conditions ne sont pas respectées.

IMAGE restriction)

.. image:: _static/.png
   :align: center

Fonctionnalites Autorisation
============================

L'administrateur est celui qui attribue l'autorisation faite pour chaque groupe. Pour une meilleure gestion des données certaines d'entre elles ne seront accessible pour la modification que par les personnes ayant reçu cette autorisation.

Cette partie est aussi un menu déroulant, les liens Groupe et Utilisateurs qui s'y trouvent sont ceux qui permettent de voir les droits réservés à chaque groupe créé. En tenant compte du groupe auquel une personne appartient il est alors facile de connaître les autorisations allouées à  cette dernière.

 IMAGE ajout groupe)

.. image:: _static/.png
   :align: center

Le Lien Utilisateur permet de voir les diverses connections qui se font sur l’interface administratif. Ils affichent les informations de l’utilisateur admin et ainsi permet soit d’en ajouter un nouveau ou de supprimer un utilisateur existant.
IMAGE utlisateur)

.. image:: _static/.png
   :align: center
Insertion des données collectées
================================

Les données envoyées par téléphones par les collecteurs seront automatiquement diriger vers le lien de la collecte Pluviométrique appelée observations pluviométriques, Ceci peut aussi être enregistrées par une personne responsable via l'application sans pour autant le faire via téléphone.
Cependant ces données seront enregistrées mais pas encore validées seul le responsable de validation aura le privilège d’accomplir cette tâche.

 IMAGE explicatif de l'isertion desdonnees)

.. image:: _static/.png
   :align: center
