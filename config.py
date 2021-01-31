# coding: UTF-8
__author__ = 'Jón Ragnarsson'
# Demo configuration file

from os import path

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    texts = {
        'njala': {
            'file': 'njala.txt',
            'title': 'Brennu-Njáls saga',
            'lang': 'is',
        },
        'pilturstulka': {
            'file': 'pilturogstulka.txt',
            'title': 'Piltur og stúlka',
            'lang': 'is',
        },
        'sult': {
            'file': 'sult.txt',
            'title': 'Sult',
            'lang': 'no',
        },
        'roda': {
        	'file': 'roda.txt',
        	'title': 'Röda rummet',
        	'lang': 'se',
        },
        'ormstunga': {
        	'file': 'ormstunga.txt',
        	'title': 'Ormsipsum',
        	'lang': 'is',
        },
    }

    textpath = path.join(basedir, 'texts')
