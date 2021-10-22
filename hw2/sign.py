from flask import redirect, request, url_for, render_template
from flask.views import MethodView
import gbmodel

class Sign(MethodView):
    def get(self):
        return render_template('sign.html')

    def post(self):
        """
        Accepts POST requests, and processes the form;
        Redirect to index when completed.
        """
        model = gbmodel.get_model()
        model.insert(request.form['department'], request.form['coursenumber'], request.form['quarter'],request.form['year'], request.form['instructor'],request.form['review']) #Calls function to insert into database. 
        return redirect(url_for('index'))