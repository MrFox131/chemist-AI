# INSTALL DEPENDENCIES WITH THIS COMMAND
# pip install -r requirements.txt
# RUN THIS COMMAND TO RUN SERVER:
# python main.py and go to http://localhost:5000/
import flask
from . import db
from . import rec
import urllib
import json
import os

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False


# @app.route('/find_items/<string:request>')
# def find_items(request):
#     names, prices, categories, ids = [[] for i in range(4)]
#     items = db.find_items(request)
#     for g in items:
#         names.append(g.name)
#         prices.append(g.price)
#         ids.append(g.pk)
#         categories.append('')
#     return flask.jsonify(
#         list(zip(names, prices, categories, ids)),
#     )


@app.route('/get_goods/<int:n_page>')
def get_goods(n_page):
    names, prices, categories, ids = [[] for i in range(4)]
    goods = db.get_page_goods(n_page)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        ids.append(g.pk)
        categories.append('')
    return flask.jsonify(
        list(zip(names, prices, categories, ids)),
    )


@app.route('/get_recs')
def get_recs():
    '''return json response with goods we recommend'''
    names, prices, categories, ids = [[] for i in range(4)]
    cart_ids, ns = [], []
    cookie = flask.request.cookies.get('cart', '')
    if cookie:
        cookie = urllib.parse.unquote(cookie)
        cookie = json.loads(cookie)
    for (pk, n) in cookie:
        cart_ids.append(pk)
        ns.append(n)
    r_names, r_prices, r_categories, r_ids = [[] for i in range(4)]
    recommendations = rec.get_recs_from_db(cart_ids, ns)
    for g in recommendations:
        r_names.append(g.name)
        r_prices.append(g.price)
        r_ids.append(g.pk)
        r_categories.append('')
    rec_info = zip(r_names, r_prices, r_categories, r_ids)
    return flask.jsonify(list(rec_info))


@app.route('/')
def index():
    names, prices, categories, ids = [[] for i in range(4)]
    goods = db.get_page_goods(1)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        ids.append(g.pk)
        categories.append('')
    info = zip(names, prices, categories, ids)
    return flask.render_template(
        'index.html', info=info
    )


@app.route('/cart')
def cart():
    cart_ids, ns = [], []
    cookie = flask.request.cookies.get('cart', '')
    if cookie:
        cookie = urllib.parse.unquote(cookie)
        cookie = json.loads(cookie)
    for (pk, n) in cookie:
        cart_ids.append(pk)
        ns.append(n)
    r_names, r_prices, r_categories, r_ids = [[] for i in range(4)]
    recommendations = rec.get_recs_from_db(cart_ids, ns)
    for g in recommendations:
        r_names.append(g.name)
        r_prices.append(g.price)
        r_ids.append(g.pk)
        r_categories.append('')
    rec_info = zip(r_names, r_prices, r_categories, r_ids)
    names, prices, categories, ids = [[] for i in range(4)]
    goods = db.get_goods_by_ids(cart_ids)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        ids.append(g.pk)
        categories.append('')
    info = zip(names, prices, categories, ids)
    return flask.render_template(
        'cart.html', info=info, rec_info=rec_info
    )


@app.route('/search/<string:request>')
def search(request):
    names, prices, categories, ids = [[] for i in range(4)]
    items = db.find_items(request)
    isEmpty = False
    for g in items:
        names.append(g.name)
        prices.append(g.price)
        ids.append(g.pk)
        categories.append('')
    if len(items) == 0:
        isEmpty = True
    info = zip(names, prices, categories, ids)
    return flask.render_template(
        'search.html', info=info, request=request, isEmpty=isEmpty
    )


@app.route('/static/images/products/<string:name>')
def get_image(name):
    fullpath = 'web/static/images/products/' + name
    filepath = 'static/images/products/' + name
    if os.path.isfile(fullpath):
        return flask.send_file(filepath)
    else:
        default = 'static/images/products/default.png'
        return flask.send_file(default)
