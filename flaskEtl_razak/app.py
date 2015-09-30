from flask import Flask, render_template, redirect, \
     url_for, request, session, flash, g
from flask.ext.sqlalchemy import SQLAlchemy
#from funtools import wraps

#create application object
app = Flask(__name__)

app.secret_key = "cool etl"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/etldb'

#create the sqlalchemy object
db = SQLAlchemy(app)

