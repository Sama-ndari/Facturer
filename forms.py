import csv
from datetime import datetime


def all_objects():
    with open('objects.csv', 'r', encoding='utf-8') as file:
        data = csv.DictReader(file)
        objects = []
        for row in data:
            objects.append(row["Designation"])
    return objects


def the_object(designation, quantite):
    with open('objects.csv', 'r', encoding='utf-8') as file:
        data = csv.DictReader(file)
        for row in data:
            if designation == row["Designation"]:
                obj = Object(designation=row["Designation"],
                             unite=row["Unite"],
                             pu=row["PU"],
                             quantity=quantite,
                             )
    return obj


def convertir_en_lettres(nombre):
    mots_base = {
        0: 'zéro',
        1: 'un',
        2: 'deux',
        3: 'trois',
        4: 'quatre',
        5: 'cinq',
        6: 'six',
        7: 'sept',
        8: 'huit',
        9: 'neuf',
        10: 'dix',
        11: 'onze',
        12: 'douze',
        13: 'treize',
        14: 'quatorze',
        15: 'quinze',
        16: 'seize',
        20: 'vingt',
        30: 'trente',
        40: 'quarante',
        50: 'cinquante',
        60: 'soixante',
        70: 'soixante-dix',
        80: 'quatre-vingts',
        90: 'quatre-vingt-dix'
    }

    if nombre in mots_base:
        return mots_base[nombre]

    if 16 < nombre < 20:
        return mots_base[nombre % 10] + '-dix'

    if 70 <= nombre < 80 or 90 <= nombre < 100:
        dizaine = nombre // 10
        reste = nombre % 10
        if reste == 0:
            return mots_base[dizaine * 10]
        else:
            return mots_base[(dizaine-1) * 10] + '-' + convertir_en_lettres(reste+10)

    if nombre < 100:
        dizaine = nombre // 10
        unite = nombre % 10
        if unite == 1:
            return mots_base[dizaine * 10] + ' et un'
        elif unite == 0:
            return mots_base[dizaine * 10]
        else:
            return mots_base[dizaine * 10] + '-' + mots_base[unite]

    if nombre < 1000:
        centaine = nombre // 100
        reste = nombre % 100
        if reste == 0:
            if centaine == 1:
                return 'cent'
            else:
                return mots_base[centaine] + ' cents'
        else:
            if centaine == 1:
                return 'cent ' + convertir_en_lettres(reste)
            else:
                return mots_base[centaine] + ' cent ' + convertir_en_lettres(reste)

    if nombre < 1000000:
        millier = nombre // 1000
        reste = nombre % 1000
        if reste == 0:
            if millier == 1:
                return 'mille'
            else:
                return convertir_en_lettres(millier) + ' mille'
        else:
            if millier == 1:
                return 'mille ' + convertir_en_lettres(reste)
            else:
                return convertir_en_lettres(millier) + ' mille ' + convertir_en_lettres(reste)

    if nombre < 1000000000:
        million = nombre // 1000000
        reste = nombre % 1000000
        if reste == 0:
            if million == 1:
                return 'un million'
            else:
                return convertir_en_lettres(million) + ' millions'
        else:
            if million == 1:
                return 'un million ' + convertir_en_lettres(reste)
            else:
                return convertir_en_lettres(million) + ' millions ' + convertir_en_lettres(reste)

    return str(nombre)


# Exemple d'utilisation
nombre = 86
en_lettres = convertir_en_lettres(nombre)
print(en_lettres)


def date():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%d/%m/%Y")
    return formatted_date


class Object:
    def __init__(self, designation, unite, pu, quantity):
        self.designation = designation
        self.unite = unite
        self.pu = pu
        self.quantite = quantity
        self.pt = int(pu) * int(quantity)


class Company:
    def __init__(self, name, nature):
        self.name = name
        self.nature = nature


class Responsable:
    def __init__(self, name, post, adress, mail, contact):
        self.name = name
        self.post = post
        self.adress = adress
        self.mail = mail
        self.contact = contact


def total(the_list):
    the_total = 0
    for el in the_list:
        the_total += el.pt
    return the_total


class Facture:
    def __init__(self, account, responsable, company):
        self.account = account
        self.responsable = responsable
        self.company = company
        self.date = date()
        self.numero = 0
        self.objects = []
        self.total_number = 0
        self.total_char = ''
        self.tva = False

