from flask import render_template, request, redirect, url_for, flash
from models import IICS, GIA


def register_routes(app, db):
    # ---------------- IICS Routes ---------------- #

    @app.route('/')
    def index():
        iics = IICS.query.all()
        return render_template('index.html', iics=iics)

    @app.route('/iics/add', methods=['GET', 'POST'])
    def add_iics():
        if request.method == 'POST':
            infants = request.form.get('infants')
            diplomats = request.form.get('diplomats')
            deportees = request.form.get('deportees')

            new_iic = IICS(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_iic)
            db.session.commit()

            flash("New IICS entry added successfully!", "success")
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
            flash("IICS entry updated successfully!", "success")
            return redirect(url_for('index'))

        return render_template('update.html', iic=iic)

    @app.route('/delete/<int:iic_id>', methods=['POST'])
    def delete_iic(iic_id):
        iic = IICS.query.get_or_404(iic_id)
        db.session.delete(iic)
        db.session.commit()
        flash("IICS entry deleted successfully!", "danger")
        return redirect(url_for('index'))

    # ---------------- GIA Routes ---------------- #

    @app.route('/gia')
    def gia_index():
        gia_entries = GIA.query.all()
        return render_template('gia/list.html', gia_entries=gia_entries)

    @app.route('/gia/add', methods=['GET', 'POST'])
    def add_gia():
        if request.method == 'POST':
            infants = request.form.get('infants')
            diplomats = request.form.get('diplomats')
            deportees = request.form.get('deportees')

            new_gia = GIA(infants=infants, diplomats=diplomats, deportees=deportees)
            db.session.add(new_gia)
            db.session.commit()

            flash("New GIA entry added successfully!", "success")
            return redirect(url_for('gia_index'))

        return render_template('gia/add.html')

    @app.route('/gia/update/<int:gia_id>', methods=['GET', 'POST'])
    def update_gia(gia_id):
        gia = GIA.query.get_or_404(gia_id)

        if request.method == 'POST':
            gia.infants = request.form.get('infants')
            gia.diplomats = request.form.get('diplomats')
            gia.deportees = request.form.get('deportees')

            db.session.commit()
            flash("GIA entry updated successfully!", "success")
            return redirect(url_for('gia_index'))

        return render_template('gia/update.html', gia=gia)

    @app.route('/gia/delete/<int:gia_id>', methods=['POST'])
    def delete_gia(gia_id):
        gia = GIA.query.get_or_404(gia_id)
        db.session.delete(gia)
        db.session.commit()
        flash("GIA entry deleted successfully!", "danger")
        return redirect(url_for('gia_index'))
