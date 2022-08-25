from app import app
from flask import (render_template, request, redirect, \
                    url_for, flash, jsonify)

from server import csv_df, df_data_set, get_data_one_month, get_data_all_months, data_set
from datetime import datetime as dt


@app.route('/', methods=['GET', 'POST'])
def all_months_chart():
    data_all_months = get_data_all_months()
    labels = list(data_all_months.keys())
    data = list(data_all_months.values())
    
    return render_template('index.html', data=data, labels=labels)

@app.route('/data', methods=['GET', 'POST'])
def one_month_chart():
    if request.is_json:
        if request.method == 'GET': 
            labels = list(data_set.keys())
            label = labels[0]
            data_one_month = get_data_one_month(data_set, label)
         
            return jsonify(data_one_month)

        if request.method == 'POST':      
            label = request.get_json().get('label')
            data_one_month = get_data_one_month(data_set, label)

            return jsonify(data_one_month)

    return redirect('/')