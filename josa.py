# -*- coding: utf-8 -*-
from hangulize import hangulize, hangul


INDO_EUROPEANS = [('ita', 0.5), ('deu', 0.1), ('spa', 1), ('por', 0.3)]
POSTPOSITIONS = [(u'을', u'를'), (u'은', u'는'), (u'과', u'와'),
                 (u'이', u'가'), (u'이랑', u'랑'), (u'이라', u'라'),
                 (u'이면', u'면'), (u'이야', u'야'), (u'이다', u'다'),
                 (u'이든', u'든'), (u'이던', u'던')]


def has_jongseong(word, lang='eng'):
    if lang == 'eng':
        return has_jongseong_for_eng(word)
    elif lang != 'kor':
        word = hangulize(word, lang)
    return bool(hangul.split(word[-1])[2])


def has_jongseong_for_eng(word):
    point = 0
    for lang, accuracy in INDO_EUROPEANS:
        if has_jongseong(word, lang):
            point += accuracy
        else:
            point -= accuracy
    return point > 0


def add_josa(after_jongseong, after_jungseong):
    POSTPOSITIONS.append(after_jongseong, after_jungseong)


def josa(word, type, lang='eng'):
    if not isinstance(word, unicode):
        word = word.encode()
    if not isinstance(type, unicode):
        type = type.encode()
    for pp in POSTPOSITIONS:
        if type in pp:
            return pp[0] if has_jongseong(word, lang) else pp[1]
    raise ValueError('%s is not an available postposition' % type)


def append(word, type, lang='eng', spacing=False):
    space = ' ' if spacing else ''
    return word + space + josa(word, type, lang)
