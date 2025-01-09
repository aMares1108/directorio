from flask import Flask, render_template
from pymongo import MongoClient
from os import getenv

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.jinja')

@app.route('/all')
def person():
    with MongoClient(getenv('MONGOURI')) as mongo:
        results = mongo.jornada122.staff.find({},{'_id':0}).to_list()

    return render_template('person.jinja', results=results)


if __name__ == '__main__':
    app.run(debug=True)