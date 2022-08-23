from app import app
from flask import (render_template, request, redirect, \
                    url_for, flash, jsonify)

from server import csv_df


@app.route('/')
def google_pie_chart():
    data = {'Task' : 'Hours per Day', 'Work' : 22, 'Eat' : 4, 'Commute' : 6, 'Watching TV' : 5, 'Sleeping' : 15}
    if request.is_json:
        if request.method == 'GET':
            # items = get_items()
            # return jsonify(items)
            pass

        if request.method == 'POST':          
            id = request.get_json().get('id')
            # do_some_thing()
            pass    
    
    return render_template('index.html', data=data)