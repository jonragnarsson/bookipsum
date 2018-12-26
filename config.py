# coding: UTF-8
__author__ = 'Jón Ragnarsson'
# Demo configuration file

from os import path

basedir = path.abspath(path.dirname(__file__))


class Config(object):
    texts = {
        'njala': {
            'file': 'njala.txt',
            'title': 'Brennu-Njáls ipsum',
            'lang': 'is',
        },
        'ormstunga': {
            'file': 'ormstunga.txt',
            'title': 'Gunnlaugs ipsum Ormstungu',
            'lang': 'is',
        },
        'pilturstulka': {
            'file': 'pilturogstulka.txt',
            'title': 'Piltur og ipsum',
            'lang': 'is',
        },
        'sult': {
            'file': 'sult.txt',
            'title': 'Sult ipsum',
            'lang': 'no',
        },
    }

    textpath = path.join(basedir, 'texts')
