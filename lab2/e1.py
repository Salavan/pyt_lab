# coding=utf-8

def iflatten_collection(collection):
    for e in collection:
        if isinstance(e, list) or isinstance(e, tuple):
            for i in iflatten_collection(e):
                yield i
        else:
            yield e


def flatten_collection(collection, result_type=list):
    """
    Spłaszcza kolekcję, która jest dowolnie zagnieżdzona.
    Zwraca typ taki jak podano w argumencie, np. tuple lub list.
    Używa generatora.
    """
    return result_type(iflatten_collection(collection))


def iflatten_dictionary(dictionary, crumb="", name_crumbs=True):
    for e in dictionary.items():
        if isinstance(e[1], dict):
            for i in iflatten_dictionary(e[1], crumb + e[0] + "_" if name_crumbs else "", name_crumbs):
                yield i
        else:
            if name_crumbs:
                e = (crumb + e[0], e[1])
            yield e


def flatten_dictionary(dictionary, name_crumbs=True):
    """
    Spłaszcza słownik. Jeśli name_crumbs jest włączone klucze tworzone są jako ścieżka wszsytkich kluczy zagłębień.
    """
    if name_crumbs:
        return dict(iflatten_dictionary(dictionary, "", name_crumbs))
    else:
        temp = {}
        for e in iflatten_dictionary(dictionary, "", name_crumbs):
            if e[0] in temp:
                temp.update({e[0]: flatten_collection([e[1], temp[e[0]]])})
            else:
                temp[e[0]] = e[1]
        return temp