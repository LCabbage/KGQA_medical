from flask import Flask, render_template, request, jsonify
from query_graph import *

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index(name=None):
    return render_template('index.html', name = name)


@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')


@app.route('/KGQA', methods=['GET', 'POST'])
def KGQA():
    return render_template('KGQA.html')

@app.route('/KGQA_answer_text', methods=['GET', 'POST'])
def KGQA_answer_text():
    question = request.args.get('name')
    json_data = get_KGQA_answer_text(question)
    print(json_data)
    return jsonify(json_data)


@app.route('/KGQA_answer_graph', methods=['GET', 'POST'])
def KGQA_answer_graph():
    question = request.args.get('name')
    json_data = get_KGQA_answer_graph(question)
    # print(json_data)
    return jsonify(json_data)

@app.route('/search_name', methods=['GET', 'POST'])
def search_name():
    name = request.args.get('name')
    json_data=query((name))
    return jsonify(json_data)

# @app.route('/get_all_relation', methods=['GET', 'POST'])
# def get_all_relation():
#     return render_template('all_relation.html')

if __name__ == '__main__':
    app.debug=True
    app.run()
