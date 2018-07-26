from flask import Flask, render_template, request, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)
client = MongoClient('mongodb://marinabar:lollipop1@ds247061.mlab.com:47061/catsproj1')
db = client['catsproj1']
cat_collection = db['cats']
like = 0


def pluslike():
    request['like'] += 1
    print(1)


@app.route('/')
def main():
    cats = cat_collection.find()
    return render_template('main.html', cats=cats)


@app.route('/add', methods=['get', 'post'])
def add():
    #comment
    name = request.form.get('name', '')
    img = request.form.get('img', '')
    description = request.form.get('description', '')

    if name == '' or img == '' or description == '':
        return render_template('add.html')
    else:
        new_cat = {
            'name': name,
            'img': img,
            'description': description,
        }
        cat_collection.insert(new_cat)
        return redirect('/cat?id={}'.format(str(new_cat['_id'])))


@app.route('/cat', methods=['get', 'post'])
def details():
    print(123)
    comment = request.form.get('com', '')
    #if comment == '':
        #return render_template('cat.html')
    try:
        id = request.args.get('id', '')

        cat = cat_collection.find_one({'_id': ObjectId(id)})
        print(cat)

        return render_template('cat.html', cat=cat)
    except:
        return 'Cat not found'


app.run(debug=True, port=8080)
