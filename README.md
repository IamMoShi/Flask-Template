
> English below

# 🧪 Qualité logicielle dans ce projet Flask REST

Ce projet utilise un ensemble d’outils de **formatage**, **linting**, et **analyse statique** pour garantir un code propre, lisible, sécurisé et maintenable.
Ces outils sont automatiquement exécutés grâce à [**pre-commit**](https://pre-commit.com/), lors de chaque commit Git.

---

## 📋 Table des matières

1. [Installation des outils](#installation-des-outils)
2. [Présentation des outils](#présentation-des-outils)

   * [Black (formateur automatique)](#1-black)
   * [isort (tri des imports)](#2-isort)
   * [flake8 (analyse de style)](#3-flake8)
   * [Bandit (analyse de sécurité)](#4-bandit)
   * [Pylint (analyse complète)](#5-pylint)
   * [Validation des messages de commit](#6-commit-message-checker)
3. [Utilisation manuelle des outils](#utilisation-manuelle)
4. [Bonnes pratiques](#bonnes-pratiques)

---

## 💾 Installation des outils

1. Installe les dépendances de développement :

```bash
pip install -r requirements-dev.txt
```

2. Installe les hooks Git (à faire une seule fois par projet) :

```bash
# Pour les hooks de code
pre-commit install

# (Optionnel) Pour le hook de validation de message de commit
pre-commit install --hook-type commit-msg
```

---

## 🛠️ Présentation des outils

### 1. [Black](https://black.readthedocs.io/en/stable/) – Formateur automatique

> "The uncompromising code formatter."

* Formate automatiquement le code Python selon une convention stricte.
* Objectif : uniformité et simplicité, aucun débat de style.
* Intégré avec `isort` (même longueur de ligne).

**Configuration :**

* Longueur max de ligne : `79`
* Exclusion des dossiers : `.git`, `.venv`, `build`, etc.

**Exemple de commande :**

```bash
black .
```

---

### 2. [isort](https://pycqa.github.io/isort/) – Organisation des imports

> Trie automatiquement les `import` en respectant une structure définie.

* Classe les imports par catégories : standard, tiers, et locaux.
* Compatible avec le style Black via `profile = "black"`.

**Configuration :**

* Respecte le même `line_length = 79`.
* Connaît le package local `monpackage`.

**Exemple de commande :**

```bash
isort .
```

---

### 3. [flake8](https://flake8.pycqa.org/en/latest/) – Linting de style

> Combine PyFlakes, pycodestyle et McCabe complexity.

* Vérifie les erreurs de style, de syntaxe, et la complexité cyclomatique.
* Complémentaire à Black, qui ne détecte pas tous les problèmes.

**Configuration :**

* Longueur max de ligne : `79`
* Complexité max d'une fonction : `10`
* Dossiers ignorés : `.venv`, `.github`, etc.

**Exemple de commande :**

```bash
flake8 .
```

---

### 4. [Bandit](https://bandit.readthedocs.io/en/latest/) – Analyse de sécurité

> Analyse de vulnérabilités courantes dans le code Python.

* Vérifie l'usage de fonctions dangereuses : `eval`, `exec`, `os.system`, `subprocess`, etc.
* Ignore certains faux positifs (ex. `assert`, `try/except pass`).
* Configuré avec les règles dans `pyproject.toml`.

**Exclusions notables :**

* `tests`, `.venv`, `.github`

**Tests activés :**

* Ports ouverts, secrets codés en dur, XSS/Template Injection, SSL/TLS, etc.

**Exemple de commande :**

```bash
bandit -c pyproject.toml -r .
```

---

### 5. [Pylint](https://pylint.pycqa.org/en/latest/) – Analyseur complet

> L’outil le plus strict et complet pour Python.

* Analyse syntaxique, typage, conventions de nommage, documentation manquante, etc.
* Donne une note globale à chaque fichier.

**Configuration personnalisée :**

* Longueur max de ligne : `79`
* Docstring désactivées partiellement (`missing-module-docstring` uniquement)
* Hook local via `pre-commit` pour éviter les conflits avec les versions installées

**Exemple de commande :**

```bash
pylint monpackage/
```

---

### 6. ✅ Validation du message de commit

> S'assure que les messages de commit respectent un format.

* Script local dans `scripts/check_commit_msg.py`
* Hook exécuté **uniquement lors du commit (`commit-msg`)**
* Tu peux l’utiliser pour appliquer une convention `conventional commits` (`feat:`, `fix:`, `chore:`...)

---

## 🧪 Utilisation manuelle

Voici comment exécuter les outils indépendamment :

```bash
# Exécuter tous les hooks sur tous les fichiers
pre-commit run --all-files

# Exécuter un seul outil (ex : Black)
pre-commit run black --all-files
```

---

## ✅ Bonnes pratiques

* 🔄 **Avant chaque commit important** : `pre-commit run --all-files`
* 💡 **Corriger automatiquement le code** : laisse Black et isort réécrire les fichiers
* ⚠️ **Si un commit échoue**, lis les messages d’erreur (souvent flake8, bandit ou pylint)
* 📚 **Respecte les conventions de nommage** pour éviter les avertissements de pylint

---
Voici la **version anglaise traduite** et légèrement adaptée pour plus de fluidité en contexte anglophone. Tu peux la copier directement dans un fichier `docs/code_quality.md` ou l’intégrer dans un `README.md`.

---

# 🧪 Code Quality in This Flask REST Project

This project uses a set of **formatting**, **linting**, and **static analysis** tools to ensure the code is clean, readable, secure, and maintainable.
These tools are automatically run using [**pre-commit**](https://pre-commit.com/) hooks on every Git commit.

---

## 📋 Table of Contents

1. [Tool Installation](#tool-installation)
2. [Tool Overview](#tool-overview)

   * [Black (auto-formatter)](#1-black)
   * [isort (import organizer)](#2-isort)
   * [flake8 (style linter)](#3-flake8)
   * [Bandit (security scanner)](#4-bandit)
   * [Pylint (code analyzer)](#5-pylint)
   * [Commit Message Validation](#6-commit-message-validation)
3. [Manual Usage](#manual-usage)
4. [Best Practices](#best-practices)

---

## 💾 Tool Installation

1. Install development dependencies:

```bash
pip install -r requirements-dev.txt
```

2. Install Git hooks for pre-commit:

```bash
# Install hooks for code checks
pre-commit install

# (Optional) Install commit message validation hook
pre-commit install --hook-type commit-msg
```

---

## 🛠️ Tool Overview

### 1. [Black](https://black.readthedocs.io/en/stable/) – Code auto-formatter

> "The uncompromising code formatter."

* Automatically formats Python code according to strict conventions.
* Focuses on consistency and simplicity — no style debates.
* Integrated with `isort` (shares the same line length limit).

**Config highlights:**

* Max line length: `79`
* Excludes folders like `.git`, `.venv`, `build`, etc.

**Run manually:**

```bash
black .
```

---

### 2. [isort](https://pycqa.github.io/isort/) – Import organizer

> Automatically sorts `import` statements into logical groups.

* Groups imports: standard, third-party, and local.
* Fully compatible with Black's formatting style (`profile = "black"`).

**Config highlights:**

* Line length: `79`
* Recognizes local packages like `monpackage`.

**Run manually:**

```bash
isort .
```

---

### 3. [flake8](https://flake8.pycqa.org/en/latest/) – Style linter

> Combines PyFlakes, pycodestyle, and McCabe complexity checker.

* Detects style issues, syntax errors, and cyclomatic complexity problems.
* Complements Black — catches things Black doesn’t fix.

**Config highlights:**

* Max line length: `79`
* Max function complexity: `10`
* Excludes: `.venv`, `.github`, etc.

**Run manually:**

```bash
flake8 .
```

---

### 4. [Bandit](https://bandit.readthedocs.io/en/latest/) – Security scanner

> Scans for common security issues in Python code.

* Detects unsafe function usage like `eval`, `exec`, `os.system`, `subprocess`, etc.
* Ignores some known false positives like `assert`, `try/except pass`.
* Configured in `pyproject.toml`.

**Excluded folders:**

* `tests`, `.venv`, `.github`

**Included tests:**

* Open ports, hardcoded secrets, XSS/Template Injection, SSL/TLS, YAML injection, and more.

**Run manually:**

```bash
bandit -c pyproject.toml -r .
```

---

### 5. [Pylint](https://pylint.pycqa.org/en/latest/) – Full static analyzer

> The most strict and comprehensive Python linter.

* Checks syntax, typing, naming conventions, missing docstrings, and more.
* Assigns a score to each file based on code quality.

**Config highlights:**

* Max line length: `79`
* Docstrings partially disabled (e.g., `missing-module-docstring` ignored)
* Runs via a local `pre-commit` hook to avoid version issues

**Run manually:**

```bash
pylint monpackage/
```

---

### 6. ✅ Commit Message Validation

> Ensures consistent and meaningful commit messages.

* Custom script: `scripts/check_commit_msg.py`
* Runs only at commit time (`commit-msg` hook)
* Useful for enforcing [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/):
  `feat:`, `fix:`, `chore:`, etc.

---

## 🧪 Manual Usage

Run checks manually without committing:

```bash
# Run all hooks on all files
pre-commit run --all-files

# Run a single hook (example: Black)
pre-commit run black --all-files
```

---

## ✅ Best Practices

* 🔄 **Before committing large changes**: run `pre-commit run --all-files`
* 🧼 **Let Black and isort handle formatting** — don’t fight them
* ⚠️ **If a hook blocks your commit**, read the error (usually flake8, bandit, or pylint)
* 📚 **Follow naming conventions** to avoid unnecessary warnings

---

Would you like a `Makefile` or `dev.sh` to automate these checks as well?
