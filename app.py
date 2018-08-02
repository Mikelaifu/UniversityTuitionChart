from flask import Flask, render_template, jsonify, redirect
import datetime as dt
import numpy as np
import pandas as pd
import json
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


app = Flask(__name__)

engine = create_engine("sqlite:///university.sqlite")
Base = automap_base()

print(Base.classes.keys())
Base.prepare(engine, reflect= True)
df_standerd = Base.classes.df_standerd
session = Session(engine)

app = Flask(__name__)


def read_data(result1):
    
    df = pd.DataFrame(result1)   
    df1 = df[list(df.columns)[0:7]]
    df2list = list(df.columns)[7:]
    df2list.insert(0, "Year")
    df2 = df[df2list]
    universityName = ['Year',
            'University of Alabama in Huntsville - AL',
            'Alabama State University - AL',
            'The University of Alabama - AL',
            'Auburn University at Montgomery - AL',
            'Alabama A & M University - AL',
            'University of Alabama at Birmingham - AL',
            'Auburn University - AL',
            'Birmingham Southern College - AL',
            'Concordia College Alabama - AL',
            'Faulkner University - AL']
    changedict = dict(zip(list(df2.columns), universityName ))

    df2 = df2.rename(columns = changedict)
    
    dictt1 = {}
    for i in list(df1.columns):
        dictt1[i] = list(df1)  

    
    
    dictt2 = {}
    for i in list(df2.columns):
        dictt2[i] = list(df2[i])
    
    finaldict = { 'standerd' : dictt1, 'college': dictt2 }

    return finaldict




@app.route("/")
def home():
    return render_template("index.html")

@app.route("/dropdown")
def names():
    session = Session(engine)
    result1 = session.query(df_standerd.Year, df_standerd.Percentile0_40, 
                        df_standerd.Percentile40_60, 
                        df_standerd.Percentile60_75,
                        df_standerd.Percentile75_86, 
                        df_standerd.Percentile86_95, 
                        df_standerd.Percentile95_100,
                        df_standerd.Degree1,
                        df_standerd.Degree2,
                        df_standerd.Degree3,
                        df_standerd.Degree4,
                        df_standerd.Degree5,
                        df_standerd.Degree6,
                        df_standerd.Degree7,
                        df_standerd.Degree8,
                        df_standerd.Degree9,
                        df_standerd.Degree10).all()
    dictt = read_data(result1)
    transformed_list = list(dictt['college'].keys())[1:]
    session.close()
    return jsonify(transformed_list)

@app.route("/line")
def makeline():
    session = Session(engine)
    result1 = session.query(df_standerd.Year, df_standerd.Percentile0_40, 
                        df_standerd.Percentile40_60, 
                        df_standerd.Percentile60_75,
                        df_standerd.Percentile75_86, 
                        df_standerd.Percentile86_95, 
                        df_standerd.Percentile95_100,
                        df_standerd.Degree1,
                        df_standerd.Degree2,
                        df_standerd.Degree3,
                        df_standerd.Degree4,
                        df_standerd.Degree5,
                        df_standerd.Degree6,
                        df_standerd.Degree7,
                        df_standerd.Degree8,
                        df_standerd.Degree9,
                        df_standerd.Degree10).all()
    dictt = read_data(result1)
    session.close()
    # transformed_dictt = dictTranform(dictt['standerd'])
    return jsonify(dictt)





if __name__ == "__main__":
    app.run(debug=True)

