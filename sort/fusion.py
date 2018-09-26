

def fusion(lst):
    length = len(lst)
    # Si la liste contient 0 ou 1 élément, alors elle est naturellement triée
    if length <= 1:
        return lst
    # On cherche l'indice median de la liste
    median = length // 2
    # On sépare la liste en deux et on appel la fonction merge sur les deux sous-parties
    return merge(fusion(lst[:median]), fusion(lst[median:]))


def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a[0] <= b[0]:
        return [a[0]] + merge(a[1:], b)
    return [b[0]] + merge(a, b[1:])

