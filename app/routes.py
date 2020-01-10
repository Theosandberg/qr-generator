from app import app
from flask import render_template, flash, redirect, url_for
from app.forms import QRForm
import qrcode
from uuid import uuid4 as uuid


@app.route('/')
def index():
    return 'Hello'

@app.route('/qrcode', methods=['GET', 'POST'])
def qrcode_gen():
    form = QRForm()
    if form.validate_on_submit():
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(form.qrgen.data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")

        id = str(uuid())

    

        app.logger.debug('Saving QR-code with id: %s' % id)
        img.save('{path}/{id}.png'.format(path=app.config['QRCODE_LOCATION'], id=id))

        return redirect(url_for('show_qrcode', id=id))

    return render_template('qrcode.html', title='Sign In', form=form)

@app.route('/qrcode/<id>')
def show_qrcode(id):
    return render_template('show_qrcode.html', id=id)
