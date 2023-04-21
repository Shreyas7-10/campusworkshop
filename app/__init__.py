"""Setup at app startup"""
from flask import Flask
import psycopg2


app = Flask(__name__)
postgres = psycopg2.connect(
        host="dpg-ch12v98rddl13a53n9ng-a.oregon-postgres.render.com",
        database="todo_t9ot",
        user="todo_t9ot_user",
        password="8mqMUpD2AndT0bzeDH9wu0470UOMYcNJ")
# To prevent from using a blueprint, we use a cyclic import
# This also means that we need to place this import here
# pylint: disable=cyclic-import, wrong-import-position
from app import routes
