from random import randrange, choice, randint
from copy import deepcopy

L = "E5, DS5, E5, DS5, E5, B4, D5, C5, A4, REST, C4, E4, A4, B4, REST, E4, GS4, B4, C5, REST, E4, C5, B4, A4".split(", ")
L2 = "SN, SN, SN, SN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN".split(", ")

def occurrence(liste):
    """ Return a dict with the number of occurrence of each element in
    the list """
    dico = {}
    for e in liste:
        try:
            dico[e] += 1
        except KeyError:
            dico[e] = 1
    return dico

def n_occurrence(liste, n=1):
    """ Return a dict with the number of occurrence of each n element in
    the list
    return {(a, b): {a: 3, b: 4, c: 5},
            (b, c): {a: 1, b: 5, c: 7}, ...} """
    dico = {}
    for i in range(len(liste)-n):
        tuple_note = tuple(liste[i:i+n])
        next_note = liste[i+n]
        if tuple_note not in dico:
            dico[tuple_note] = {}
        try:
            dico[tuple_note][next_note] += 1
        except KeyError:
            dico[tuple_note][next_note] = 1
    return dico

def proba_dict(dico):
    """ from {(a, b): {a: 2, b: 3, c: 4},
              (b, c): {...}, ...}
        return {(a, b): (9, {a: 2, b: 3, c: 4}),
                (b, c): (n, {...}), ...} """
    for key in dico:
        dico[key] = (sum(dico[key].values()), dico[key])
    return dico

def calcul_occurrence_with_proba(liste):
    """Return a list of the proba of each element in liste,
    refer to proba_dict:
    return [(proba, occurrence(...)), proba_dict(...),
                                      proba_dict(...), ...] """
    list_with_proba = [(len(liste), occurrence(liste))]
    for i in range(1, len(liste)):
        list_with_proba.append(proba_dict(n_occurrence(liste, i)))
    return list_with_proba

def calcul_occurrence(liste):
    list_total = [occurrence(liste)]
    for i in range(1, len(liste)):
        list_total.append(n_occurrence(liste, i))
    return list_total

def choose_according_proba(proba, dico):
    """Return a element in dico according to the proba"""
    assert proba > 0
    rand = debug_rand = randint(1, proba)
    for key in dico:
        value = dico[key]
        if value >= rand:
            return key
        else:
            rand -= value
    raise ValueError("Error with choose_according_proba: " +
       "proba = {}, debug_rand = {}, rand = {}, dico = {}".format(proba,
       debug_rand, rand, dico))

def create_occurrence(liste):  #version 1
    """ Create a new list of occurrence according to the proba of the
    element in the 1st. (no record of old elements) """
    calcul = calcul_occurrence_with_proba(liste)
    new = []
    i_choose = 0
    nb_elemt = 0
    while nb_elemt < len(liste):
        if i_choose == 0:
            proba, dico = calcul[i_choose]
        else:
            token = tuple(new[-i_choose:])
            if token not in calcul[i_choose]:
                i_choose -= 1
                continue
            else:
                proba, dico = calcul[i_choose][token]
        new_element = choose_according_proba(proba, dico)
        new.append(new_element)
        i_choose += 1
        nb_elemt += 1
    return new

def add_dict(dico1, dico2):
    for key in dico2:
        try:
            dico1[key] += dico2[key]
        except KeyError:
            dico1[key] = dico2[key]
    return dico1

def minus_dict_positive(dico1, dico2):
    dico1 = deepcopy(dico1)
    for key in dico2:
        if key in dico1:
            if dico1[key] <= dico2[key]:
                dico1.pop(key)
            else:
                dico1[key] -= dico2[key]
    return dico1

def create_occurrence2(liste, rec=True):  # version 2
    """ Create a new list of occurrence according to the proba of the
    element in the liste. Add each proba to calculate the "real" proba.
    rec for calculate the proba with elements already exist. """
    calcul = calcul_occurrence(liste)
    new = []
    i_choose = 0
    nb_elemt = 0
    while nb_elemt < len(liste):
        dico = calcul[0]
        if i_choose:
            token = tuple(new[-i_choose:])
            if token not in calcul[i_choose]:
                i_choose -= 1
                continue
            else:
                for i in range(1, i_choose + 1):
                    token = tuple(new[-i:])
                    dico = add_dict(dico, calcul[i][token])
                if rec:
                    dico = minus_dict_positive(dico, occurrence(new))
                    if dico == {}:  # For safe
                        dico = calcul[0]
        new_element = choose_according_proba(sum(dico.values()), dico)
        new.append(new_element)
        i_choose += 1
        nb_elemt += 1
    return new

def list_to_string_of_music(liste, n=1, version=2):
    """ Create a new liste and transform to string for JythonMusic """
    create = create_occurrence2 if version == 2 else create_occurrence
    res = []
    for i in range(n):
        res.extend(create(liste))
    return ", ".join(res)

def list_to_list_of_music(liste, n=1, version=2):
    """ Create a new liste for JythonMusic """
    res = []
    for i in range(n):
        if version == 3:
            res.extend(create_occurrence2(liste, False))
        elif version == 1:
            res.extend(create_occurrence(liste))
        else:
            res.extend(create_occurrence2(liste))
    return res

pitches = "E5, DS5, E5, DS5, E5, B4, D5, C5, A4, REST, C4, E4, A4, B4, REST, E4, GS4, B4, C5, REST, E4, C5, B4, A4".split(", ")
durations = "SN, SN, SN, SN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN, SN, SN, SN, SN, EN".split(", ")

for el in list_to_list_of_music(pitches):
    vars()[el] = 5


pitches1 = []
for note in list_to_list_of_music(pitches):
    pitches1.append(vars()[note])
#durations1 = [vars()[note] for note in list_to_list_of_music(durations)]
# La prochaine note est-elle dépendante des précédentes ?
# C'est-à-dire, faut-il enregistrer les notes déjà sorties ?
