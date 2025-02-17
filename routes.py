from flask import render_template, request, redirect, url_for

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


            new_gia = GIA(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_gia)
            db.session.commit()

            gia = GIA.query.all()
            return render_template('index.html', gia=gia)



    @app.route('/add_iics', methods=['POST'])
    def add_iics():
        if request.method == 'POST':
            # Get form data for IICS
            infants = request.form['infants']
            diplomats = request.form['diplomats']
            deportees = request.form['deportees']

            # Save to the database (Assuming you're using an IICS model)
            new_iic = IICS(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_iic)
            db.session.commit()

            return redirect(url_for('index'))

    @app.route('/add_gia', methods=['POST'])
    def add_gia():
        if request.method == 'POST':
            # Get form data for GIA
            infants = request.form['infants']
            diplomats = request.form['diplomats']
            deportees = request.form['deportees']

            # Save to the database (Assuming you're using a GIA model)
            new_gia = GIA(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_gia)
            db.session.commit()

            return redirect(url_for('index'))