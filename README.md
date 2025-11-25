# DocLogic

DocLogic est une application web de gestion hospitalière développée avec Django, intégrant des fonctionnalités avancées pour la gestion des patients, du personnel médical, des départements et la communication via DynamoDB. L’interface utilisateur est moderne, responsive et utilise HTMX pour des interactions dynamiques et rapides.

---

## Sommaire

- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Utilisation](#utilisation)
- [Technologies](#technologies)
- [Structure des dossiers](#structure-des-dossiers)
- [API & Endpoints](#api--endpoints)
- [Sécurité](#sécurité)
- [Tests](#tests)
- [Contribuer](#contribuer)
- [Licence](#licence)

---

## Fonctionnalités

- **Gestion des patients** : création, édition, consultation, rapport personnel.
- **Gestion du personnel médical** : listing, filtrage par département.
- **Dashboard staff & patient** : vue personnalisée selon le rôle.
- **Sidebar dynamique** : navigation latérale, responsive, ouverture/fermeture animée.
- **Contact hospitalier** : formulaire connecté à AWS DynamoDB.
- **Chargement dynamique HTMX** : modals, formulaires, listes.
- **Authentification & autorisations** : accès sécurisé selon le rôle (staff/patient).
- **Administration Django** : gestion avancée des modèles.
- **Support des fichiers statiques** : CSS, JS, images.

---

## Architecture

- **Backend** : Django 5.2.3, Django REST Framework, boto3 pour AWS.
- **Frontend** : HTML, CSS, JS, HTMX, Django templates.
- **Base de données** : PostgreSQL (par défaut), DynamoDB pour les messages de contact.
- **Organisation MVC** : séparation claire des modèles, vues, templates.

---

## Installation

1. **Cloner le dépôt**
   ```bash
    git clone https://github.com/letEmmDev/DocLogic
    cd DocLogic/code
   ```

2. **Créer et activer un environnement virtuel**
   ```bash
    python3 -m venv .venv
    source .venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
    pip install -r requirements.txt
   ```

4. **Configurer les variables d’environnement**
   - Crée un fichier `.env` à la racine :
    ```
    AWS_ACCESS_KEY_ID=...
    AWS_SECRET_ACCESS_KEY=...
    AWS_REGION=...
    ```

5. **Migrer la base de données**
    ```bash
    python manage.py migrate
    ```

6. **Créer un superutilisateur**
    ```bash
    python manage.py createsuperuser
    ```

7. **Lancer le serveur**
    ```bash
    python manage.py runserver
    ```

---

## Configuration

- **Fichiers statiques** :  
    Les CSS et JS sont dans `/static/`.
    Utilise `python manage.py collectstatic` pour la production.

- **AWS DynamoDB** :  
    Configure les credentials dans `.env` et assure-toi que la table `ContactMessages` existe.

---

## Utilisation

- **Accès admin** : `/admin`
- **Dashboard patient** : `/patients_management/my_report/`
- **Dashboard staff** : `/hospital/dashboard_staff/`
- **Formulaire de contact** : `/hospital/contact/`
- **Navigation sidebar** : accessible sur toutes les pages principales.

---

## Technologies

- Django
- Django REST Framework
- HTMX
- boto3 (AWS)
- PostgreSQL
- HTML/CSS/JS

---

## Structure des dossiers

```
code/
├── core/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── hospital/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── patient_management/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── manage.py
```

---

## API & Endpoints

- **REST API** : endpoints pour les rapports patients (`PatientReportViewSet`).
- **HTMX endpoints** : chargement dynamique des formulaires et listes.
- **Contact** : POST vers `/hospital/contact/` pour envoyer un message à DynamoDB.

---

## Sécurité

- **Décorateurs personnalisés** : `@staff_required`, `@patient_required` pour sécuriser les vues.
- **CSRF** : protection sur tous les formulaires.
- **Gestion des erreurs** : redirection vers la homepage ou affichage de pages personnalisées.

---

## Tests

- **Unitaires** : à écrire dans chaque app (`tests.py`).
- **Manuels** : vérification des dashboards, formulaires, sidebar, et intégration DynamoDB.

---

## Contribuer

1. Fork le projet
2. Crée une branche : `git checkout -b feature/ma-feature`
3. Push et ouvre une Pull Request

---

## Licence

Ce projet est sous licence MIT.

---

## Auteurs

- LetEmmDev
- Contributeurs

---

## Contact

Pour toute question : Vous pouvez ouvrir une issue / PR sur GitHub ou me contacter directement via email.