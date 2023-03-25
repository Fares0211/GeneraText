# GeneraText

Implémentation : Nous montrons au modèle de nombreux exemples d'entraînement afin qu'il puisse apprendre un modèle entre l'entrée et la sortie.

Chaque entrée est une séquence de caractères et la sortie est le caractère unique suivant. Par exemple, si nous voulons nous entraîner sur la phrase "python is a great language", l'entrée du premier échantillon est "python is a great langua" et la sortie sera "g". L'entrée du deuxième échantillon serait "ython is a great languag" et la sortie serait "e", et ainsi de suite, jusqu'à ce que nous bouclions tout l'ensemble de données. Nous devons montrer au modèle autant d'exemples que possible afin d'obtenir des prédictions raisonnables.

Comment faire pour créer cette IA ? Nous allons effectuer différentes étapes : préparation du dataset, construction du modèle, entrainement du modèle et génération du texte.

## 1. Préparation du dataset
Dans un premier temps, nous allons préparer la dataset et effectuer du preprocessing afin de nettoyer et de fiabiliser les données pour notre entrainement.
Ensuite, nous allons encoder notre dataset ce qui nous permettra de convertir les caractères en entier, ce qui nous facilitera la tâche.
Nous voulons que chaque échantillon d'entrée soit une séquence de caractères de la longueur de la séquence et la sortie d'un seul caractère qui est le suivant.

## 2. Construction du modèle
Maintenant, construisons le modèle ; ce dernier a fondamentalement deux couches LSTM avec un nombre arbitraire de 128 unités LSTM (LSTM =
La couche de sortie est une couche entièrement connectée avec 39 unités où chaque neurone correspond à un caractère.

## 3. Entrainement du modèle et génération du texte
Tout ce que nous faisons ici, c’est commencer avec un texte de départ, de construire la séquence d'entrée, puis de prédire le caractère suivant. Après cela, nous décalons la séquence d'entrée en supprimant le premier caractère et en ajoutant le dernier caractère prédit. Cela nous donne une séquence d'entrées légèrement modifiée qui a toujours une longueur égale à la taille de notre longueur de séquence.

