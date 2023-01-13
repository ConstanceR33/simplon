import requests
import numpy as np
import pandas as pd
import streamlit as st


choice_etat = ['Vigoureux', 'Moyen', 'Mauvais', 'Sénescent']
choice_sol = ['Terre nue', 'Pelouse', 'Sol minéralisé', 'Sol planté', 'Terre piétinée']
choice_commune = ["Ville D'Avray", 'Antony', 'Asnieres Sur Seine', 'Bagneux',
                  'Bois Colombes', 'Boulogne Billancourt', 'Bourg La Reine',
                  'Chatenay Malabry', 'Chatillon', 'Chaville', 'Clamart',
                  'Clichy', 'Colombes', 'Courbevoie', 'Fontenay Aux Roses',
                  'Garches', 'Gennevilliers', 'Issy Les Moulineaux',
                  'La Garenne Colombes', 'Le Plessis Robinson', 'Levallois Perret',
                  'Malakoff', 'Marnes La Coquette', 'Meudon', 'Montrouge',
                  'Nanterre', 'Neuilly Sur Seine', 'Puteaux', 'Rueil Malmaison',
                  'Saint Cloud', 'Sceaux', 'Sevres', 'Suresnes', 'Vanves',
                  'Vaucresson', "Ville D'Avray", 'Villeneuve La Garenne']
choice_nom_fr = ['Chêne', 'Acacia de Constantinople', 'Ailante', 'Alisier blanc',
                 'Alisier de Fontainebleau', 'Alisier du Nord', 'Amandier',
                 'Amélanchier du Canada', 'Arbousier commun. arbre aux fraises',
          'Arbre aux mouchoirs', 'Arbre aux quarante écus',
          'Arbre aux quarante écus pleureur', 'Arbre de Judée',
          'Aubépine hybride (cultivar greffé)', 'Aubépine monogyne',
          'Aulne commun', 'Aulne de Corse', 'Bouleau commun',
          'Calocèdre. libocèdre', 'Catalpa commun', "Cerisier du Japon 'Kanzan'",
          'Cerisier à fleurs du Japon', 'Cerisier à fruits', 'Chamaerops',
          'Charme commun', 'Charme fastigié', 'Charme houblon', 'Châtaignier',
          'Chêne chevelu', 'Chêne chevelu panaché', 'Chêne commun hybride',
          'Chêne liège', 'Chêne pédonculé', 'Chêne pédonculé fastigié',
          "Chêne rouge d'Amérique", 'Chêne rouvre ovoïde',
          'Chêne rouvre à feuilles laciniées', 'Chêne rouvre. chêne sessile',
          'Chêne vert', 'Chêne à feuille de myrsine', "Copalme d'Amérique",
          'Cormier', 'Cornouiller mâle', 'Cyprès chauve de Louisiane',
          'Cyprès de Lawson', 'Cyprès de Leyland', 'Cyprès de Nootka',
          "Cyprès de l' Arizona", 'Cyprès des Etangs', 'Cèdre bleu',
          "Cèdre de l'Atlas", "Cèdre de l'Atlas bleu pleureur",
          "Cèdre de l'Atlas fastigié", "Cèdre de l'Himalaya", 'Cèdre du Liban',
          "Epicéa de l'Himalaya. de Morinda", 'Erable Negundo', 'Erable argenté',
          'Erable argenté lacinié pleureur', 'Erable champêtre',
          "Erable d'Italie", 'Erable de Cappadoce', 'Erable de Montpellier',
          'Erable plane', 'Erable plane à port compact', 'Erable sycomore',
          'Erable sycomore doré', 'Faux orme de Sibérie', 'Faux orme du Japon',
          'Figuier', 'Filaire', 'Filaire 2', 'Frêne', 'Frêne commun',
          "Frêne d'Amérique", 'Frêne pleureur', 'Frêne à feuilles simples',
          'Frêne à fleurs', 'Févier à trois épines', 'Grisard', 'Houx commun',
          'Hêtre commun', 'Hêtre fastigié', 'Hêtre pleureur', 'Hêtre pourpre',
          'Hêtre tricolore', 'If commun', "If d'Irlande", 'Laurier du Portugal',
          'Laurier du Portugal à feuilles de Myrte', 'Magnolia toujours vert',
          'Marronnier commun', 'Marronnier commun à feuilles laciniées',
          "Marronnier d'Inde vrai", 'Marronnier à fleurs rouges', 'Merisier',
          'Merisier à fleurs blanches doubles', 'Micocoulier',
          "Micocoulier d'Amérique", 'Micocoulier de Provence',
          'Muscadier de Californie', 'Métaséquoïa', 'Mûrier', 'Mûrier blanc',
          'Mûrier noir', 'Mûrier à papier', 'Noisetier de Byzance',
          "Noyer noir d'Amérique", 'Noyer royal. Noyer de Perse',
          'Olivier de Bohème', 'Oranger des Osages', 'Orme', 'Orme de Chine',
          'Orme à feuilles de charme', 'Palmier', 'Paulownia impérial', 'Pavia',
          'Peuplier blanc fastigié', 'Peuplier de Chine',
          'Peuplier de Chine fastigié', 'Peuplier du Setchuan variété tibétaine',
          'Peuplier euraméricain', 'Peuplier neige',
          'Peuplier noir. liard. piboule', 'Pin', 'Pin de Corse. laricio',
          'Pin maritime. pin des Landes', 'Pin noir', "Pin noir d'Autriche",
          'Pin parasol', "Pin pleureur de l'Himalaya. Pin du Bhoutan",
          'Pin sylvestre', 'Pin sylvestre de Riga', 'Plaqueminier de Chine. Kaki',
          "Platane commun. à feuille d'érable", "Platane d'Orient",
          'Poirier commun', 'Poivrier du Japon', 'Pommier pourpre',
          'Prunier de Pissard', 'Prunier myrobolan',
          'Ptérocaryer à feuilles de frêne', 'Pêcher', 'Robinier',
          'Sapin de Céphalonie', 'Sapin de Douglas', 'Sapin du Caucase',
          'Saule blanc', 'Saule fragile', 'Saule pleureur',
          'Saule pleureur à bois jaune.', 'Saule tortueux', 'Savonnier',
          'Sophora', 'Sophora panaché', 'Sorbier sp',
          'Séquoia géant de Californie', 'Séquoïa toujours vert',
          "Thuja d' Orient", 'Thuja occidentalis', 'Thuya géant de Californie',
          'Tilleul', 'Tilleul argenté', 'Tilleul commun', 'Tilleul de Hollande',
          'Tilleul à petites feuilles', 'Troène', 'Tulipier de Virginie',
          'Virgilier jaune']


st.subheader('API SUR LES ARBRES REMARQUABLES')

nom_fr = st.selectbox('Choisissez le nom d\'arbre de votre choix', choice_nom_fr)
commune = st.selectbox('Choisissez la commune des Hauts-de-Seine', choice_commune)
etat = st.selectbox('Choisissez l\'état phytosanitaire', choice_etat)
sol = st.selectbox('Choisissez le type de sol', choice_sol)
circonf = st.number_input(f'Entrez une circonférence comprise entre 0.5 et 6.00', min_value=0.5, max_value=6.00, value=2.8)
#circonf = st.text_input(f'Merci d\'entrer une valeur comprise entre 0.5 et 6.00', '2.80')
envergure = st.number_input(f'Entrez une envergure comprise entre 2.5 et 40.00', min_value=2.5, max_value=40.00, value=20.00)
#envergure = st.text_input(f'Merci d\'entrer une valeur comprise entre 2.5 et 40.00', '20.00')
clic = st.button('Try')


def the_choice():
    req = requests.get(f'https://f660-185-175-148-123.eu.ngrok.io/?nom_fr={nom_fr}&?commune={commune.upper()}&?etat={etat}&?sol={sol}&?circonf={circonf}&?envergure={envergure}').json()
    return st.write(f"Avec ces paramètres, on prédit que l\'arbre mesurera {req['prediction']}")

if clic:
    the_choice()
