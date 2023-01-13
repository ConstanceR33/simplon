from typing import Union
from fastapi import FastAPI
import pickle
import pandas as pd
import numpy as np


app = FastAPI()

@app.get("/")
def read_item(circonf: Union[float, None] = 2.80,
              envergure: Union[float, None] = 20.00,
              nom_fr: Union[str, None] = 'Chêne',
              etat: Union[str, None] = 'Vigoureux',
              sol: Union[str, None] = 'Terre nue',
              commune: Union[str, None] = 'VILLE D\'AVRAY'
              ):
    pickled_model = pickle.load(open('trees.pkl', 'rb'))
    X_user = pd.DataFrame({'circonf': [circonf],
                           'envergure': [envergure],
                           'nom_fr': [nom_fr],
                           'etat': [etat],
                           'sol': [sol],
                           'commune': [commune]
                            })
    pred = pickled_model.predict(X_user)
    return {'prediction': f" {np.round(pred, 2)[0]} mètres "}
