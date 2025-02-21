from flask import render_template, request, redirect, url_for, flash
from models import IICS, GIA

def register_routes(app, db):

    @app.route('/', methods=['GET'])
    def index():
        iics = IICS.query.all()
        return render_template('index.html', iics=iics)

    @app.route('/add', methods=['GET', 'POST'])
    def add_iics():
        if request.method == 'POST':
            infants = request.form.get('infants')
            diplomats = request.form.get('diplomats')
            deportees = request.form.get('deportees')

            new_iic = IICS(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_iic)
            db.session.commit()

            flash("New entry added successfully!", "success")
            return redirect(url_for('index'))

        return render_template('iics/add.html')

    @app.route('/update/<int:iic_id>', methods=['GET', 'POST'])
    def update_iic(iic_id):
        iic = IICS.query.get_or_404(iic_id)

        if request.method == 'POST':
            iic.infants = request.form.get('infants')
            iic.diplomats = request.form.get('diplomats')
            iic.deportees = request.form.get('deportees')

            db.session.commit()
            flash("Entry updated successfully!", "success")
            return redirect(url_for('index'))

        return render_template('update.html', iic=iic)

    @app.route('/delete/<int:iic_id>', methods=['POST'])
    def delete_iic(iic_id):
        iic = IICS.query.get_or_404(iic_id)
        db.session.delete(iic)
        db.session.commit()
        flash("Entry deleted successfully!", "danger")
        return redirect(url_for('index'))
