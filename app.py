from flask import Flask, render_template, request, redirect
from jinja2 import TemplateNotFound

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html')


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/<string:page_name>')
def html_page(page_name):
    try:
        return render_template(page_name)
    except TemplateNotFound:
        return render_template('404.html')


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        return redirect('/thankyou.html')
    else:
        return 'error!!'


def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'\n{email},{subject},{message}')


if __name__ == '__main__':
    app.run(debug=True)
