from os import path
from flask import Flask, render_template, abort, request
import markovify
from config import Config

formvalues = {
    'book': 'njala',
    'num': '3',
    'length': '250'
}


app = Flask(__name__)


class Markov:

    _textmarkov = None

    def __init__(self, _filename):
        with open(_filename) as f:
            text = f.read()
            self._textmarkov = markovify.Text(text)

    def make_sentence(self, min_length=120):
        sentence = ''
        while len(sentence) < min_length:
            sentence += ' '+self._textmarkov.make_sentence()
        return sentence


@app.route('/')
@app.route('/<_book>')
def index(_book=formvalues['book']):
    paragraphs = []
    par_length = int(request.args.get('length', default=formvalues['length']))
    par_length = 800 if (par_length > 800) else par_length
    par_no = int(request.args.get('num', default=formvalues['num']))
    par_no = 20 if (par_no > 20) else par_no
    _book = request.args.get('book') if (request.args.get('book') is not None) else formvalues['book']
    formvalues['num'] = par_no
    formvalues['length'] = par_length
    formvalues['book'] = _book
    try:
        m = Markov(path.join(Config.textpath, _book+'.txt'))
    except FileNotFoundError:
        abort(404)
        return;
    for i in range(par_no):
        paragraphs.append(m.make_sentence(par_length))
    return render_template('index.html', text=paragraphs, title=Config.texts[_book]['title'], choices=Config.texts, formvalues=formvalues)


if __name__ == '__main__':
    app.run(debug=True)
