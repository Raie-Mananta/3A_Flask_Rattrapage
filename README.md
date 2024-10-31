# 3A - R5A4 - TP1 Rattrapage Nancy ASTIER Comment utiliser mon beau site

Ce TP étant entièrement fait en back je n'ai pas fait de front digne de ce nom désolée.

## Installer les dépendances et lancer le site.

```
pip install -r requirements.txt
```

Cette commande permettra d'installer toutes les dependances nécéssaires pour lancer le site en une fois.

```
python main.py
```

Celle ci permettra de demarrer le site et de charger la base de donnée associée.


## Naviguer dans le site

Le lien http://127.0.0.1:5000 vous ammenera à la page d'acceuil du site donnant juste un petit message de bienvenue.

http://127.0.0.1:5000/bookings affiche toutes les reservations faites.

http://127.0.0.1:5000/bookings/numerobooking_id ammene à une reservation specifique en fonction du booking id donné.

Et enfin http://127.0.0.1:5000/statistics/room_type donne les statistiques de l'utilisation de chaque type de chambre.

## Requetes PostMan

Il y a 3 requetes postman

Celle pour ajouter une reservation. Vous ferez une requete GET sur http://127.0.0.1:5000/bookings en envoyant un body de type raw et vous mettrez une donnée au format json comme celle ci.
```json
{
  "user_id": "34",
  "start_date": "2024-11-10",
  "end_date": "2024-11-15",
  "is_cancelled": false,
  "is_paid": true,
  "price": 200.00,
  "room_type": "SUITE"
}
```

Celle pour supprimer une reservation. Vous ferez une requete DELETE sur http://127.0.0.1:5000/bookings/idbooking

Et enfin celle pour modifier une reservation. Vous ferez une requete GET sur http://127.0.0.1:5000/bookings/idbooking en envoyant un body de type raw et vous mettrez une donnée au format json comme vu precedent.