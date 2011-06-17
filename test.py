# -*- coding: utf-8 -*-
import unittest
import josa


class HangulPostpositionTestCase(unittest.TestCase):

    def runTest(self):
        pass

    def test_josa_english(self):
        assert u'를' == josa.josa(u'false positive', u'를')
        assert u'를' == josa.josa(u'false negative', u'을')
        assert u'이' == josa.josa(u'function', u'가')
        assert u'이랑' == josa.josa(u'deterministic', u'랑')

    def test_append_english(self):
        assert u'false positive를' == josa.append(u'false positive', u'를')
        assert u'false negative' == josa.append(u'false negative', u'을')
        assert u'function이' == josa.append(u'function', u'가')
        assert u'deterministic이랑' == josa.josa(u'deterministic', u'랑')

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
    suite = unittest.TestSuite()
    suite.addTest(HangulPostpositionTestCase())
    return suite
