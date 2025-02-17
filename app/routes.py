from flask import render_template, request

from models import IICS, GIA

def register_routes(app, db):

    @app.route('/', methods=['GET', 'POST'])
    def index():
        if request.method == 'GET':
            iics = IICS.query.all()
            return render_template('index.html', iics=iics)

        elif request.method == 'POST':
            infants =request.form.get('infants')
            diplomats = request.form.get('diplomats')
            deportees = request.form.get('deportees')

            new_iics = IICS(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_iics)
            db.session.commit()

            iics = IICS.query.all()
            return render_template('index.html', iics=iics)
