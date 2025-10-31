# RPM
https://rpm.org/

## Environnement

sudo dnf install rpm-build rpmdevtools tree
rpmdev-setuptree 

## Config files

| Directive            | Écrase fichier modifié ? | Installe `.rpmnew` ? | Utilisation                        |
| -------------------- | ------------------------ | -------------------- | ---------------------------------- |
| `%config`            | ✅ Oui  (+ .save)         | ❌ Non                | Config forcée (systèmes contrôlés) |
| `%config(noreplace)` | ❌ Non                    | ✅ Oui                | Config utilisateur personnalisable |
| `%config(missingok)` | N/A                      | N/A                  | Ne plante pas si absent            |

## Versions des dépendances

| Opérateur | Signification     |
| --------- | ----------------- |
| `>`       | supérieur à       |
| `>=`      | supérieur ou égal |
| `<`       | inférieur à       |
| `<=`      | inférieur ou égal |
| `=`       | égal à            |
