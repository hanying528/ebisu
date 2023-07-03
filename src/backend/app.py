#!flask/bin/python
from flask import jsonify, Blueprint
import pandas as pd

from .db import get_db

bp = Blueprint('blueprints', __name__, url_prefix='')

@bp.route('/')
def index():
    return "Welcome :fire_emoji:"


# A function to return user's total expenditure in current month
@bp.route('/api/v1.0/total_expenditure', methods=['GET'])
def total_expenditure():
    db = get_db()
    df = pd.read_sql_query("SELECT SUM(amount) FROM transactions WHERE amount < 0 "
                           "AND TO_DATE(trxn_dt) BETWEEN DATE('now', 'start of month') "
                           "AND DATE('now', 'end of month')", db)
    return jsonify(df.to_dict(orient='records'))


# A function to return user's total income in current month
@bp.route('/api/v1.0/total_income', methods=['GET'])
def total_income():
    db = get_db()
    df = pd.read_sql_query("SELECT SUM(amount) FROM transactions WHERE amount > 0 "
                           "AND TO_DATE(trxn_dt) BETWEEN DATE('now', 'start of month') "
                           "AND DATE('now', 'end of month')", db)
    return jsonify(df.to_dict(orient='records'))


# A function to return user's total expenditure by category in current month
def total_expenditure_by_category():
    db = get_db()
    df = pd.read_sql_query("SELECT category, SUM(amount) FROM transactions WHERE amount < 0 "
                           "AND TO_DATE(trxn_dt) BETWEEN BETWEEN DATE('now', 'start of month') "
                           "AND DATE('now', 'end of month') GROUP BY category", db)
    return jsonify(df.to_dict(orient='records'))

