#!/usr/bin/env python3

from flask import Flask, request, render_template, abort

from app.data import fruit_data

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html', items=fruit_data)


@app.route('/search')
def search():
    query = request.args.get('query', '')
    if not query:
        return render_template('search.html')

    query = query.lower().strip()
    results = [item for item in fruit_data if query
               in item['name'].lower()]

    return render_template('results.html', results=results)


@app.route('/detail/<slug>')
def detail(slug=None):
    item = next(
        (item for item in fruit_data if item.get('slug') == slug),
        None
    )
    if not item:
        abort(404)
    return render_template('detail.html', item=item)


if __name__ == '__main__':
    app.run(
        debug=True, port=5001
    )
