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

Pour des instructions détaillées, veuillez consulter le script `install_stage_management.sh` fourni.

Les étapes générales sont les suivantes :

1.  **Arrêter** votre serveur Odoo.
2.  **Placer** le répertoire du module (nommé `stage_management`) dans le chemin des addons de votre instance Odoo.
3.  **Définir** les permissions de fichiers appropriées pour l'utilisateur Odoo (si nécessaire).
4.  **Redémarrer** votre serveur Odoo.
5.  **Mettre à jour la liste des applications** dans Odoo (Mode développeur -> Applications -> Mettre à jour la liste des applications).
6.  **Rechercher** "Stage Management" dans la liste des applications et cliquer sur **Installer** ou **Mettre à niveau**.

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
