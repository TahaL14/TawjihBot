## TawjihBot - Chatbot d'Orientation Scolaire

TawjihBot est un chatbot intelligent développé en Flask qui aide les étudiants marocains dans leur orientation scolaire. Le bot peut guider les étudiants du primaire au supérieur en analysant leurs préférences et en leur proposant des conseils personnalisés.

## Fonctionnalités

- **Orientation Primaire** : Aide à choisir entre littérature, scientifique et technologique
- **Orientation Supérieure** : Conseils pour médecine, ingénierie et autres filières
- **Interface Conversationnelle** : Chat en temps réel avec interface web moderne
- **Intelligence Artificielle** : Utilise l'algorithme de similarité pour comprendre les questions
- **Réponses Personnalisées** : Recommandations basées sur les préférences de l'étudiant

## Technologies Utilisées

- **Backend** : Python 3.x, Flask
- **Frontend** : HTML5, CSS3, JavaScript
- **IA** : difflib.SequenceMatcher pour la similarité de texte
- **Base de données** : JSON pour stocker les questions et réponses

## Prérequis

- Python 3.6 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. **Cloner le repository**
   ```bash
   git clone https://github.com/TahaL14/TawjihBot.git
   cd TawjihBot
   ```

2. **Créer un environnement virtuel (recommandé)**
   ```bash
   python -m venv venv
   
   # Sur Windows
   venv\Scripts\activate
   
   # Sur macOS/Linux
   source venv/bin/activate
   ```

3. **Installer les dépendances**
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

1. **Lancer l'application**
   ```bash
   python app.py
   ```

2. **Ouvrir votre navigateur**
   - Accédez à `http://localhost:5000`
   - Commencez à chatter avec TawjihBot !

## Structure du Projet

```
TawjihBot/
├── app.py                 # Application Flask principale
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation du projet
├── .gitignore           # Fichiers à ignorer par Git
├── data/
│   └── responses.json   # Base de données des questions/réponses
├── static/
│   └── style.css       # Styles CSS
└── templates/
    └── index.html      # Template HTML principal
```

## 🎯 Comment ça marche

1. L'utilisateur pose une question via l'interface web
2. L'algorithme calcule la similarité avec les patterns connus
3. Si la similarité dépasse 60%, une réponse appropriée est retournée
4. Le bot guide l'étudiant à travers un processus d'orientation structuré

## 📝 Exemples de Questions

- "Bonjour, j'ai besoin d'aide pour mon orientation"
- "Je ne sais pas quelle filière choisir"
- "Je veux faire médecine après le bac"
- "Quelles matières dois-je maîtriser pour le concours médical ?"
