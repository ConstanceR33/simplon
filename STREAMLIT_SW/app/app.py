import requests
import numpy as np
import pandas as pd
import streamlit as st

st.title(':red[Welcome to the] _Star Wars API_ :red[!]')
st.title(':smiley:')
st.write('\n')
st.markdown('With this app you will have access to any information about Star Wars\'s characters, films, species, planets, starships or vehicles. \nHope you\'ll find the information you need !')

st.write('\n')
st.write('\n')

st.subheader('First step, select by category')

st.write('\n')
st.write('\n')

category = st.selectbox(
    'Choose your category :',
    ('---', 'People', 'Films', 'Species', 'Planets', 'Starships', 'Vehicles'))


rows = ['name','model','length','max_atmospher','population','height',
        'mass','hair_color','skin_color','eye_color','birth_year',
        'gender','director','episode_id','opening_crawl','producer',
        'release_date','title','MGLT','cost_in_credits','crew',
        'hyperdrive_rating','manufacturer','max_atmosphering_speed',
        'passengers','starship_class','average_height','average_lifespan',
        'classification','designation','eye_colors','hair_colors',
        'language','skin_colors','climate','diameter','gravity',
        'orbital_period','rotation_period','surface_water','terrain']



def bar_search(categorie):
    instruction = categorie + ' name or letters :'
    search = st.text_input(instruction)
    return search


def requete_cate(categorie, entry):
    url = f'https://swapi.dev/api/{categorie.lower()}'
    if entry == "":
        req_c = requests.get(url).json()
        st.write(f'*Number of results for this category : {req_c["count"]}*')
    else:
        infos = f'/?search={entry}'
        req_s = requests.get(url+infos).json()
        word = 'results' if req_s["count"] > 1 else 'result'
        st.write(f'{req_s["count"]} {word} for \"{entry}\" in {categorie.lower()} category')
   #     try:
        result = pd.DataFrame(req_s['results'])
        for column in result.columns:
            if column not in rows:
                result = result.drop(columns=[f'{column}'])
        if req_s["count"] == 0:
            return st.error('No match found')
        elif req_s["count"] < 11:
            return st.write(result)
        else:
            return boucle_page(categorie, entry, result)
      #  except IndexError:
       #     st.error('No match found')


def boucle_page(cat, entry, res):
    dataframe = pd.DataFrame()
    n=2
    while True:
        req_p = requests.get(f'https://swapi.dev/api/{cat.lower()}/?search={entry}&page={n}').json()
        req_df = pd.DataFrame(req_p['results'])
        for column in req_df.columns:
            if column not in rows:
                req_df = req_df.drop(columns=[f'{column}'])
        dataframe = pd.concat([dataframe, req_df], axis=0, ignore_index=True)
        n+=1
        if req_p['next']==None:
            break
    final_df = pd.concat([res,dataframe], axis=0, ignore_index=True)
    return st.write(final_df)



if category == '---':
    st.stop()


if category != '---':
    st.write('\n')
    st.write('\n')
    st.subheader('Then you can specify your research')
    st.write('\n')
    st.write('\n')
    bar_input = bar_search(category)
    requete_cate(category, bar_input)
