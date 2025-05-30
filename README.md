# Module Odoo : Gestion des Stages (Stage Management)

## 1. Introduction

Ce module Odoo a pour objectif de fournir une solution complète pour la gestion des stages académiques au sein d'une entreprise ou d'un établissement d'enseignement. Il permet de suivre les étudiants, les entreprises partenaires, les tuteurs (académiques et professionnels), les conventions de stage et les rapports associés.

## 2. Nom Technique

Le nom technique du module est `stage_management`. Il est crucial d'utiliser ce nom (avec un underscore `_`) pour le répertoire du module et dans toutes les références d'identifiants externes (XML IDs) dans le code et les fichiers XML pour assurer la cohérence et éviter les erreurs.

## 3. Dépendances

Ce module dépend des modules Odoo standard suivants :

*   `base`: Module de base d'Odoo.
*   `mail`: Pour les fonctionnalités de suivi (chatter), d'activités et de notifications.
*   `hr`: Potentiellement utilisé pour lier les tuteurs à des employés ou pour d'autres fonctionnalités RH (bien que l'utilisation directe ne soit pas évidente dans le code fourni, il est listé comme dépendance).

Assurez-vous que ces modules sont installés dans votre instance Odoo.

## 4. Installation

Suivez ces étapes pour installer le module :

1.  **Arrêter le serveur Odoo**.

2.  **Préparer le répertoire du module** :
    *   Assurez-vous que le répertoire contenant le code du module est nommé `stage_management` (avec un underscore).
    *   Si votre répertoire actuel est différent (par exemple, `Odoo-Internship-Management-main`), renommez-le :
        ```bash
        # Exemple : Remplacez /chemin/vers/votre/module par le chemin réel
        mv /chemin/vers/votre/module/Odoo-Internship-Management-main /chemin/vers/votre/module/stage_management
        ```

3.  **Copier le module dans le répertoire des addons Odoo** :
    *   Identifiez le chemin vers votre répertoire d'addons Odoo (souvent défini dans votre fichier `odoo.conf`).
    *   Copiez le répertoire `stage_management` dans ce chemin :
        ```bash
        # Exemple : Remplacez /chemin/vers/vos/addons par le chemin réel
        # et /chemin/vers/votre/module par le chemin où se trouve stage_management
        cp -r /chemin/vers/votre/module/stage_management /chemin/vers/vos/addons/
        ```

4.  **Définir les permissions (si nécessaire)** :
    *   Assurez-vous que l'utilisateur qui exécute le processus Odoo a les droits de lecture sur les fichiers du module.
    *   Si nécessaire, ajustez le propriétaire et les permissions :
        ```bash
        # Exemple : Remplacez 'odoo' par l'utilisateur système Odoo si différent
        # et /chemin/vers/vos/addons par le chemin réel
        sudo chown -R odoo:odoo /chemin/vers/vos/addons/stage_management
        sudo chmod -R 755 /chemin/vers/vos/addons/stage_management
        ```

5.  **Redémarrer le serveur Odoo**.

6.  **Mettre à jour la liste des modules et installer** :
    *   **Option 1 (Ligne de commande)** : Redémarrez Odoo en mettant à jour le module directement (recommandé pour s'assurer que les modifications sont prises en compte).
        ```bash
        # Exemple : Adaptez le chemin vers odoo-bin et le fichier de configuration
        ./odoo-bin -c /etc/odoo/odoo.conf -u stage_management
        ```
        *Si le module n'était pas installé, remplacez `-u stage_management` par `-i stage_management` lors du premier démarrage après copie.*
    *   **Option 2 (Interface Odoo)** :
        *   Activez le mode développeur.
        *   Allez dans le menu `Applications`.
        *   Cliquez sur `Mettre à jour la liste des applications`.
        *   Recherchez le module "Stage Management".
        *   Cliquez sur `Installer` (ou `Mettre à niveau` si déjà installé).

## 5. Configuration

Aucune configuration spécifique n'est requise après l'installation pour le fonctionnement de base du module.

## 6. Fonctionnalités Principales

*   **Gestion des Étudiants** (`stage.student`): Enregistrement des informations sur les étudiants stagiaires.
*   **Gestion des Entreprises** (`stage.company`): Enregistrement des entreprises accueillant des stagiaires.
*   **Gestion des Tuteurs** (`stage.tutor`): Distinction entre tuteurs académiques et professionnels.
*   **Gestion des Stages** (`stage.internship`): Suivi complet des stages incluant les dates, l'étudiant, l'entreprise, les tuteurs et l'état (Brouillon, En cours, Terminé, Annulé).
*   **Génération de Conventions**: Création automatique de la convention de stage au format PDF via un rapport QWeb.
*   **Gestion des Rapports de Stage** (`stage.report`): Suivi des rapports soumis par les étudiants, avec un système de validation.
*   **Vues et Menus**: Intégration dans l'interface Odoo avec des menus dédiés et des vues (liste, formulaire, kanban, recherche) pour chaque modèle.

## 7. Modèles de Données Principaux

*   `stage.student`: Informations sur l'étudiant.
*   `stage.company`: Informations sur l'entreprise.
*   `stage.tutor`: Informations sur le tuteur (avec type académique/professionnel).
*   `stage.internship`: Données centrales du stage, liant les autres modèles.
*   `stage.report`: Informations sur les rapports de stage.

## 8. Rapports

*   **Convention de Stage**: Un rapport QWeb (`stage_management.report_internship_agreement`) est défini pour générer la convention au format PDF.

## 9. Sécurité

Les droits d'accès aux différents modèles sont définis dans le fichier `security/ir.model.access.csv`. Assurez-vous que les groupes d'utilisateurs appropriés ont les permissions nécessaires.

## 10. Auteur et Licence

*   **Auteur**: (À compléter - voir `__manifest__.py`)
*   **Licence**: LGPL-3 (selon `__manifest__.py`)

