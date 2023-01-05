from flask import Flask, render_template, request, redirect, url_for
import csv
app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('html_page', page_name='index.html'))


@app.route('/<string:page_name>')
def html_page(page_name='index.html'):
    return render_template(page_name)


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_database_csv(data)
            return redirect('thankyou.html')
        except Exception as err:
            raise err
    else:
        return 'Try again'


def write_to_database_txt(data):
    with open('database.txt', 'a') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        db.write(f'\n{email}, {subject}, {message}')


def write_to_database_csv(data):
    with open('database.csv', 'a', newline='') as db:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            db, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
