# -*- coding: utf-8 -*-
import warnings

from korean import Loanword, Noun, Particle, hangul, morphology


warnings.warn('This library has been deprecated. Use "korean" instead.',
              DeprecationWarning)


def has_jongseong(word, lang='eng'):
    if lang == 'kor':
        word = Noun(word)
    else:
        if lang == 'eng':
            lang = 'nld'
        word = Loanword(unicode(word), lang)
    try:
        return bool(hangul.get_final(word.read()[-1]))
    except IndexError:
        raise ValueError


def josa(word, particle, lang='eng'):
    if lang == 'kor':
        word = Noun(word)
    else:
        if lang == 'eng':
            lang = 'nld'
        word = Loanword(unicode(word), lang)
    try:
        return morphology.pick_allomorph(Particle(particle), suffix_of=word)
    except IndexError:
        raise ValueError


def append(word, type, lang='eng', spacing=False):
    space = ' ' if spacing else ''
    return word + space + josa(word, type, lang)
