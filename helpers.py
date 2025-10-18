from flask import g
import sqlite3

def getdb():
    if 'db' not in g:
        g.db = sqlite3.connect('main.db')
        g.db.row_factory = sqlite3.Row
    return g.db

