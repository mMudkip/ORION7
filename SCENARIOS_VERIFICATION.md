# Scénarios de vérification fonctionnelle

Ces scénarios décrivent les **comportements** attendus et non une interface précise. Pour chaque scénario, indiquez dans le README comment vous l'avez vérifié.

1. Depuis le sas, l'accès au laboratoire et à la réserve fonctionne.
2. Depuis le laboratoire, on ne peut pas pénétrer dans les machines tant que l'accès maintenance n'a pas été déverrouillé.
3. Un objet collecté disparaît de la salle et ne peut pas être collecté deux fois.
4. Un objet absent de l'inventaire ne peut pas être utilisé.
5. Le badge déverrouille durablement la porte maintenance ; il reste réutilisable ou possédé, selon votre conception clairement justifiée.
6. Installer seulement le câble ou seulement le fusible ne permet pas de redémarrer le réacteur.
7. Une tentative avec un code erroné ne redémarre pas le réacteur et consomme l'oxygène prévu.
8. Après installation des deux composants et saisie du bon code, le réacteur devient actif.
9. L'accès à la commande est interdit avant le redémarrage.
10. La bonbonne ne peut recharger qu'une seule fois et ne dépasse pas la capacité maximale.
11. L'oxygène ne devient jamais négatif ; à zéro, la partie est perdue et les actions sont bloquées.
12. L'évacuation depuis la commande après la réparation est une victoire, si l'oxygène est toujours positif.
13. Une commande invalide ou une action physiquement impossible n'entraîne ni déplacement ni dépense d'oxygène.
14. Les actions de consultation gratuites n'entraînent aucune dépense ; l'inspection du journal en entraîne une.
15. Une mission complète peut être gagnée ; la même partie peut aussi se terminer par une défaite.

**Conseil :** Vous pouvez fournir vos propres tests automatiques, mais une démonstration reproductible des scénarios suffit pour ce devoir.
