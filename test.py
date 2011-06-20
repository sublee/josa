# -*- coding: utf-8 -*-
import unittest
import josa


class JosaTestCase(unittest.TestCase):

    def test_jongseong_checking(self):
        assert josa.has_jongseong('game')
        assert josa.has_jongseong('lykit')
        assert josa.has_jongseong('kijun')
        assert josa.has_jongseong('incl')
        assert josa.has_jongseong('nexon')
        assert josa.has_jongseong('python')
        #assert josa.has_jongseong('facebook')
        assert josa.has_jongseong('hangul')
        assert josa.has_jongseong('gothic')
        #assert josa.has_jongseong('google')
        #assert josa.has_jongseong('apple')
        assert josa.has_jongseong('aladin')
        assert not josa.has_jongseong('hangulize')
        assert not josa.has_jongseong('josa')
        assert not josa.has_jongseong('sublee')
        assert not josa.has_jongseong('dahlia')
        assert not josa.has_jongseong('shinvee')
        assert not josa.has_jongseong('java')
        assert not josa.has_jongseong('kart')
        assert not josa.has_jongseong('rider')
        assert not josa.has_jongseong('architecture')

    def test_empty_word(self):
        try:
            josa.has_jongseong(u'')
            assert False
        except Exception, e:
            assert isinstance(e, ValueError)
        try:
            josa.josa(u'', u'를')
            assert False
        except Exception, e:
            assert isinstance(e, ValueError)
        try:
            josa.append(u'', u'를')
            assert False
        except Exception, e:
            assert isinstance(e, ValueError)

    def test_josa_english(self):
        assert u'를' == josa.josa(u'false positive', u'를')
        assert u'를' == josa.josa(u'false negative', u'을')
        assert u'이' == josa.josa(u'function', u'가')
        assert u'이랑' == josa.josa(u'deterministic', u'랑')

    def test_append_english(self):
        assert u'false positive를' == josa.append(u'false positive', u'를')
        assert u'false negative를' == josa.append(u'false negative', u'을')
        assert u'function이' == josa.append(u'function', u'가')
        assert u'deterministic이랑' == josa.append(u'deterministic', u'랑')

    def test_josa_korean(self):
        assert u'를' == josa.josa(u'택시', u'를', lang='kor')
        assert u'를' == josa.josa(u'버스', u'을', lang='kor')
        assert u'이' == josa.josa(u'나뭇잎', u'가', lang='kor')
        assert u'이랑' == josa.josa(u'넥슨', u'랑', lang='kor')

    def test_append_korean(self):
        assert u'택시를' == josa.append(u'택시', u'를', lang='kor')
        assert u'버스를' == josa.append(u'버스', u'을', lang='kor')
        assert u'나뭇잎이' == josa.append(u'나뭇잎', u'가', lang='kor')
        assert u'넥슨이랑' == josa.append(u'넥슨', u'랑', lang='kor')

    def test_josa_italian(self):
        assert u'와' == josa.josa(u'mario', u'과', lang='ita')
        assert u'는' == josa.josa(u'luigi', u'은', lang='ita')
        assert u'이' == josa.josa(u'italian', u'가', lang='ita')

    def test_append_italian(self):
        assert u'mario와' == josa.append(u'mario', u'과', lang='ita')
        assert u'luigi는' == josa.append(u'luigi', u'은', lang='ita')
        assert u'italian이' == josa.append(u'italian', u'가', lang='ita')

    def test_append_japanese(self):
        assert u'あなた가' == josa.append(u'あなた', u'이', lang='jpn')


def suite():
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(JosaTestCase))
    return suite
