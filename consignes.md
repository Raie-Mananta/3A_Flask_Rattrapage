# 3A - R5A4 - TP1 Rattrapage

Pour ce TP, vous travaillez pour un hôtel qui veut implémenter une API pour gérer ses réservations.

## Modèle de données - Bookings_DB

Le fichier `bookings_db.py` sert de base de données.
C'est un dictionnaire contenant les réservations d'un hôtel.
Chaque clé est de type string, ce qui veut dire qu'une chaine de caractère est attendue lorsqu'on cherche ou ajoute une nouvelle réservation.

Pour chaque clé, on retrouve comme valeur la réservation associée sous forme de dictionnaire également.
Une réservation présente les champs et types suivants:

```json
{
    "booking_id": "string", // str
    "user_id": "string", // str
    "start_date": "string", // str
    "end_date": "string", // str
    "is_cancelled": true, // boolean
    "is_paid": false, // boolean
    "price": 0.00, // float
    "room_type": "string", // str
},

```

## Validation des données

En plus de la justesse des types, les règles de validation lorsqu'on reçoit une réservation sont les suivantes:

- Le champ booking_id ne fait jamais partie du payload
- Tous les autres champs sont obligatoires lors d'une requête de création ou de modification par remplacement
- Le champ price ne peut pas être inférieur à 0
- Le champ room_type ne peut avoir une autre valeur que "SINGLE", "DELUXE" ou "SUITE"
- Tout champ supplémentaire qui n'existerait pas dans le modèle d'une réservation doit faire échouer la requête.

## Pré-requis

- L'application aura besoin des dépéndances suivantes:
  - flask
  - flask_cors
  - flask_expects_json
  - python_dotenv
- La validation des payload se fait uniquement avec @expects_json
- La gestion des id est libre, tant que c'est une chaine de caractères unique
- L'application doit être accessible depuis un frontend d'un autre domaine, il faut donc mettre en place les configurations CORS nécessaires

## Fichier d'entrée

Votre fichier d'entrée devra être nommé main.py. L'application doit se lancer sans erreur.

## Routes

L'API est simple, composée de 6 routes:

- Retrouver toutes les réservations, de manière paginée
  - La requête renvoie une liste [] de réservations, il s'agit donc d'une liste de dictionnaires
  - Elle prend en arguments de query les variables `offset` et `limit` permettant de renvoyer un slice de la liste
  - Si ces arguments ne sont pas mis dans la requête, vous mettrez une valeur par défaut, de 0 pour `offset` et de 10 pour `limit`
- Retrouver une réservation, grâce à son `booking_id`
  - La requête doit prendre en paramètre l'id de la réservation
  - Si la réservation en question n'existe pas, renvoyer un code dédié à une ressource inexistante et un message d'erreur générique
  - Sinon renvoyer la réservation
- Créer une nouvelle réservation
  - Le payload doit être validé avec @expects_json
  - Le `booking_id` est généré par le backend
  - La réservation est enregistrée en DB
  - La réservation créée est renvoyée en sortie avec le code HTTP de création
- Modifier une réservation existante par remplacement total de ses champs
  - Le payload doit être valide
  - Si la réservation demandée n'existe pas, on renvoie une erreur avec code dédié à une ressource inexistante
  - Sinon, on renvoie la réservation telle qu'elle a été modifiée en base de données
- Supprimer une réservation
  - L'application renvoie systématiquement le code de réussite correspondant aux requêtes qui n'ont pas de réponse attachée.
  - Demander la suppression d'une réservation qui n'existe pas ne doit pas entrainer un plantage de l'application
- Une route statistiques, avec pour endpoint `/statistics/room_type`
  - Cette route renvoie un dictionnaire contenant le compte de réservations par type de chambre, uniquement si la réservation n'est pas cancelled.
    Pour ça il faudra nécessairement boucler sur les valeurs de `bookings_db`.
    Exemple:
  ```json
  {
    "SINGLE": 4,
    "DELUXE": 10,
    "SUITE": 3
  }
  ```

## Contours du projet

- Une documentation est attachée au projet
  - Un readme explique comment installer et utiliser le projet
  - Un fichier permettant d'installer les dépendances est présent
  - Les fichiers ne devant pas être versionnés ne doivent pas être présents dans votre rendu
- Architecture
  - Une séparation selon l'architecture vue en cours est effectuée (se limiter à controller et service)
  - On considèrera pour ce TP que le travail logique sur la DB est le rôle du service
- Qualité du code
  - Attention aux structures de données et à leurs méthodes associées.
  - Respectez la PEP 8 de Python
  - Si vous codez en français, codez l'entièreté en français
  - Le format des réponses est un json valide, {} ou []. Pas de chaine de caractères ou de nombre seuls.
- API REST
  - Respectez les principes vus en cours sur les caractéristiques et la forme d'une API REST

## Lecture du Markdown

- Pour lire le md, vous pouvez utiliser une extension VSCODE, un site de MD comme Dillinger ou bien héberger le projet sur Github.
