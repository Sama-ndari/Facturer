from flask import Flask, render_template, request, send_file
import os
from PIL import Image, ImageDraw, ImageFont
from forms import *


def generate():
    obj1 = Object(designation="Haricots", unite='kilo', pu=2000, quantity=20)
    obj2 = Object(designation="Riz", unite='koli', pu=3500, quantity=15)
    obj3 = Object(designation="Mais", unite='grammes', pu=1500, quantity=40)
    obj4 = Object(designation="Haricots", unite='kilo', pu=2000, quantity=20)
    obj5 = Object(designation="Riz", unite='koli', pu=3500, quantity=15)
    obj6 = Object(designation="Mais", unite='grammes', pu=1500, quantity=40)
    obj7 = Object(designation="Haricots", unite='kilo', pu=2000, quantity=20)
    obj8 = Object(designation="Riz", unite='koli', pu=3500, quantity=15)
    obj9 = Object(designation="Mais", unite='grammes', pu=1500, quantity=40)
    obj10 = Object(designation="Haricots", unite='kilo', pu=2000, quantity=20)
    obj11 = Object(designation="Riz", unite='koli', pu=3500, quantity=15)
    obj12 = Object(designation="Mais", unite='grammes', pu=1500, quantity=40)

    company = Company(name="TWITEZIMBERE", nature="Microfinance")
    responsable = Responsable(name="NDAYISENGA JULES CESAR JUNIOR", post="DIRECTEUR GENERAL",
                              adress="Rohero I,Av. de l'Amitie,Building Isanganiro",
                              mail="abcdefghigklmnopqrstuv@gmail.com",
                              contact=("79960955", "68562985"))
    account = "48651561519856"
    facture = Facture(account=account,
                      responsable=responsable,
                      company=company)
    facture.tva = True
    facture.objects.append(obj1)
    facture.objects.append(obj2)
    facture.objects.append(obj3)
    facture.objects.append(obj4)
    facture.objects.append(obj5)
    facture.objects.append(obj6)
    facture.objects.append(obj7)
    facture.objects.append(obj8)
    facture.objects.append(obj9)
    facture.objects.append(obj10)
    facture.objects.append(obj11)
    facture.objects.append(obj12)
    print(facture.total_number)
    badge = generate_facture(fact=facture)


def generate_facture(fact):
    facture = Image.open("static/images/Facture.jpeg")
    draw = ImageDraw.Draw(facture)

    font_number = ImageFont.truetype("arial.ttf", size=36)
    font_letter = ImageFont.truetype("arial.ttf", size=30)
    color = (0, 101, 148)

    # numero de facture
    draw.text((800, 785), f"{fact.numero}", font=font_number, fill=color)
    # TVA
    if fact.tva:
        draw.text((1315, 515), f"X", font=font_number, fill=color)
    else:
        draw.text((1470, 512), f"X", font=font_number, fill=color)
    # numero de compte
    draw.text((375, 640), f"{fact.account}", font=font_number, fill=color)
    # date
    draw.text((925, 790), f"{fact.date}", font=font_number, fill=color)
    # adress
    draw.text((940, 200), f"{fact.responsable.adress}", font=font_letter, fill=color)
    draw.text((280, 2045), f"{fact.responsable.adress}", font=font_letter, fill=color)
    # telephone
    draw.text((1180, 345), f"{fact.responsable.contact[0]} / {fact.responsable.contact[1]}", font=font_number, fill=color)
    # draw.text((470, 1998), f"{fact.responsable.contact[0]}", font=font_number, fill=color)
    # company
    draw.text((850, 640), f"{fact.company.nature}", font=font_number, fill=color)
    draw.text((1250, 640), f"{fact.company.name}", font=font_number, fill=color)
    # responsable
    draw.text((1000, 1820), f"{fact.responsable.name}", font=font_letter, fill=color)
    draw.text((1015, 1870), f"{fact.responsable.post}", font=font_letter, fill=color)
    # email
    draw.text((1020, 2045), f"{fact.responsable.mail}", font=font_letter, fill=color)
    # object
    y_line = 1050
    for my_object in fact.objects:
        draw.text((310, y_line), f"{my_object.designation}", font=font_letter, fill=color)
        draw.text((730, y_line), f"{my_object.unite}", font=font_letter, fill=color)
        draw.text((950, y_line), f"{my_object.quantite}", font=font_number, fill=color)
        draw.text((1100, y_line), f"{my_object.pu}", font=font_number, fill=color)
        draw.text((1300, y_line), f"{my_object.pt}", font=font_number, fill=color)
        y_line += 47
        fact.total_number += my_object.pt
    draw.text((1300, 1610), f"{fact.total_number}", font=font_number, fill=color)
    fact.total_char = convertir_en_lettres(nombre=fact.total_number)
    draw.text((550, 1715), f"{fact.total_char}", font=font_letter, fill=color)

    # Enregistrer la facture générée en tant qu'image
    facture_path = os.path.join("static/Facture_test.png")
    facture.save(facture_path)
    return facture


generate()

# <div class="field">
# 								<input type="text" name="compte" id="compte" placeholder="Numero de Compte" required/>
# 							</div>