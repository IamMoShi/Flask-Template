# 🧪 Qualité logicielle dans ce projet Flask REST

Ce projet utilise un ensemble d’outils de **formatage**, **linting**, et **analyse statique** pour garantir un code propre, lisible, sécurisé et maintenable.
Ces outils sont automatiquement exécutés grâce à [**pre-commit**](https://pre-commit.com/) lors de chaque commit Git.

---

## 📋 Table des matières

1. [Installation des outils](#installation-des-outils)
2. [Présentation des outils](#présentation-des-outils)

   * [Black (formateur automatique)](#1-black)
   * [isort (tri des imports)](#2-isort)
   * [flake8 (analyse de style)](#3-flake8)
   * [Bandit (analyse de sécurité)](#4-bandit)
   * [Pylint (analyse complète)](#5-pylint)
   * [Validation des messages de commit](#6-validation-du-message-de-commit)
   * [docformatter (formateur de docstrings)](#7-docformatter)
   * [detect-secrets (détection de secrets)](#8-detect-secrets)
   * [Hooks généraux (YAML, EOL, espaces)](#9-hooks-généraux)
   * [pytest (tests unitaires)](#10-pytest)
   * [radon (complexité cyclomatique)](#11-radon)
3. [Utilisation manuelle](#utilisation-manuelle)
4. [Bonnes pratiques](#bonnes-pratiques)

---

## 💾 Installation des outils

1. Installe les dépendances de développement :

```bash
pip install -r requirements-dev.txt
```

2. Installe les hooks Git (à faire une seule fois) :

```bash
# Hooks de qualité de code
pre-commit install

# (Optionnel) Hook de validation des messages de commit
pre-commit install --hook-type commit-msg
```

---

## 🛠️ Présentation des outils

### 1. [Black](https://black.readthedocs.io/en/stable/) – Formateur automatique

> "The uncompromising code formatter."

* Formate automatiquement le code Python selon des règles strictes.
* Vise la cohérence totale : pas de débats de style.
* Compatible avec `isort`.

**Configuration :**

* Longueur de ligne max : `79`
* Répertoires exclus : `.git`, `.venv`, `build`, etc.

**Commande manuelle :**

```bash
black .
```

---

### 2. [isort](https://pycqa.github.io/isort/) – Organisation des imports

> Trie les imports en blocs logiques.

* Sépare les imports standards, tiers et locaux.
* Compatible avec le style de Black (`profile = "black"`).

**Configuration :**

* Longueur de ligne : `79`
* Prend en compte le module local `monpackage`

**Commande manuelle :**

```bash
isort .
```

---

### 3. [flake8](https://flake8.pycqa.org/en/latest/) – Linting de style

> Combine PyFlakes, pycodestyle, McCabe complexity checker.

* Détecte les erreurs de style, de syntaxe et la complexité du code.
* Complète Black en détectant les erreurs non liées à la mise en forme.

**Configuration :**

* Longueur max de ligne : `79`
* Complexité max par fonction : `10`
* Dossiers exclus : `.venv`, `.github`

**Commande manuelle :**

```bash
flake8 .
```

---

### 4. [Bandit](https://bandit.readthedocs.io/en/latest/) – Analyse de sécurité

> Recherche les vulnérabilités courantes.

* Signale l’usage de fonctions dangereuses comme `eval`, `exec`, etc.
* Ignore certains faux positifs.
* Configuré via `pyproject.toml`.

**Dossiers exclus :** `tests`, `.venv`, `.github`

**Tests inclus :** ports ouverts, secrets en dur, injection de templates/XSS, SSL/TLS, etc.

**Commande manuelle :**

```bash
bandit -c pyproject.toml -r .
```

---

### 5. [Pylint](https://pylint.pycqa.org/en/latest/) – Analyse complète

> Outil d’analyse statique très strict et complet.

* Vérifie la syntaxe, les types, les conventions de nommage, la documentation manquante, etc.
* Attribue une note de qualité à chaque fichier.

**Configuration :**

* Longueur max : `79`
* Désactivation partielle des docstrings (ex : `missing-module-docstring`)
* Intégré via hook local pour éviter les conflits de version

**Commande manuelle :**

```bash
pylint monpackage/
```

---

### 6. ✅ Validation du message de commit

> S’assure que les messages de commit respectent une convention.

* Script local : `scripts/check_commit_msg.py`
* Exécuté uniquement lors d’un commit (`commit-msg`)
* Idéal pour appliquer la convention [Conventional Commits](https://www.conventionalcommits.org/fr/v1.0.0/)

---

### 7. [docformatter](https://github.com/PyCQA/docformatter) – Formateur de docstrings

> Met en forme les docstrings selon la norme PEP 257.

* Améliore la lisibilité des commentaires inline.
* Complémentaire à Black.

**Commande manuelle :**

```bash
docformatter --in-place --recursive .
```

---

### 8. [detect-secrets](https://github.com/Yelp/detect-secrets) – Détecteur de secrets

> Empêche la fuite de secrets (clés API, mots de passe, tokens...)

* Analyse les fichiers avant commit.
* Utilise une baseline pour ignorer les faux positifs connus.

**Installation et création de baseline :**

```bash
pip install detect-secrets
detect-secrets scan > .secrets.baseline
```

---

### 9. Hooks généraux – [pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks)

> Hygiène générale du dépôt.

* Validation des fichiers YAML
* Suppression des espaces en fin de ligne
* Ajout de saut de ligne final

---

### 10. [pytest](https://docs.pytest.org/) – Exécution des tests (optionnel)

> Empêche les commits si les tests échouent.

* Hook local pré-configuré pour lancer `pytest` avant commit.

---

### 11. [radon](https://radon.readthedocs.io/) – Analyse de complexité

> Analyse la complexité cyclomatique et l’indice de maintenabilité.

**Commande manuelle :**

```bash
radon cc -nc -s .
```

---

## 🧪 Utilisation manuelle

Tu peux exécuter manuellement les outils de contrôle qualité :

```bash
# Exécute tous les hooks sur tous les fichiers
pre-commit run --all-files

# Exécute un hook spécifique (ex : Black)
pre-commit run black --all-files
```

---

## ✅ Bonnes pratiques

* 🔄 **Avant chaque commit important** : exécute `pre-commit run --all-files`
* 🧼 **Laisse Black et isort formater le code automatiquement**
* ⚠️ **Si un hook échoue**, lis les messages d'erreur (souvent flake8, bandit ou pylint)
* 📚 **Respecte les conventions de nommage et documente ton code**
