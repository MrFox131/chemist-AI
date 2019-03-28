# INSTALL DEPENDENCIES WITH THIS COMMAND
# pip install -r requirements.txt
# RUN THIS COMMAND TO RUN SERVER:
# python server.py and go to http://localhost:5000/
import flask
import db
import rec

app = flask.Flask(__name__)
app.config['JSON_AS_ASCII'] = False


@app.route('/get_goods/<int:n_page>')
def get_goods(n_page):
    names, prices, categories, ids = [[] for i in range(4)]
    goods = db.get_page_goods(1)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        categories.append(g.category)
        ids.append(g.pk)
    return flask.jsonify(
        list(zip(names, prices, categories, ids)),
    )


@app.route('/get_recs')
def get_recs():
    '''return json response with goods we recommend'''
    names, prices, categories, ids = [[] for i in range(4)]
    if flask.request.is_xhr:
        ids = flask.request.json['ids']
    else:
        return flask.abort(404)
    goods = rec.get_recs_by_goods_ids(ids)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        categories.append(g.category)
        ids.append(g.pk)
    return flask.jsonify(
        info=list(zip(names, prices, categories, ids)),
    )


@app.route('/')
def index():
    names, prices, categories, ids = [[] for i in range(4)]
    goods = db.get_page_goods(1)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        categories.append(g.category)
        ids.append(g.pk)
    info = zip(names, prices, categories, ids)
    return flask.render_template(
        'index.html', info=info
    )


@app.route('/cart')
def cart():
    ids = [
        int(i) for i in flask.request.cookies.get(
            'goods_ids',
            '').split(';') if i]
    names, prices, categories, ids = [[] for i in range(4)]
    recommendations = rec.get_recs_by_goods_ids(ids)
    for g in recommendations:
        names.append(g.name)
        prices.append(g.price)
        categories.append(g.category)
        ids.append(g.pk)
    rec_info = zip(names, prices, categories, ids)
    names, prices, categories, ids = [[] for i in range(4)]
    goods = db.get_goods_by_ids(ids)
    for g in goods:
        names.append(g.name)
        prices.append(g.price)
        categories.append(g.category)
        ids.append(g.pk)
    info = zip(names, prices, categories, ids)
    return flask.render_template(
        'cart.html', info=info, rec_info=rec_info
    )


if __name__ == '__main__':
    app.run(debug=True)
