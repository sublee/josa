# -*- coding: utf-8 -*-
import unittest
import hanpp


class HangulPostpositionTestCase(unittest.TestCase):

    def runTest(self):
        pass

    def test_hanpp_english(self):
        assert u'를' == hanpp.hanpp(u'false positive', u'를')
        assert u'를' == hanpp.hanpp(u'false negative', u'을')
        assert u'이' == hanpp.hanpp(u'function', u'가')
        assert u'이랑' == hanpp.hanpp(u'deterministic', u'랑')

    def test_append_english(self):
        assert u'false positive를' == hanpp.append(u'false positive', u'를')
        assert u'false negative' == hanpp.append(u'false negative', u'을')
        assert u'function이' == hanpp.append(u'function', u'가')
        assert u'deterministic이랑' == hanpp.hanpp(u'deterministic', u'랑')

    def test_hanpp_korean(self):
        assert u'를' == hanpp.hanpp(u'택시', u'를', lang='kor')
        assert u'를' == hanpp.hanpp(u'버스', u'을', lang='kor')
        assert u'이' == hanpp.hanpp(u'나뭇잎', u'가', lang='kor')
        assert u'이랑' == hanpp.hanpp(u'넥슨', u'랑', lang='kor')

    def test_append_korean(self):
        assert u'택시를' == hanpp.append(u'택시', u'를', lang='kor')
        assert u'버스를' == hanpp.append(u'버스', u'을', lang='kor')
        assert u'나뭇잎이' == hanpp.append(u'나뭇잎', u'가', lang='kor')
        assert u'넥슨이랑' == hanpp.append(u'넥슨', u'랑', lang='kor')

    def test_hanpp_italian(self):
        assert u'와' == hanpp.hanpp(u'mario', u'과', lang='ita')
        assert u'는' == hanpp.hanpp(u'luigi', u'은', lang='ita')
        assert u'이' == hanpp.hanpp(u'italian', u'가', lang='ita')

    def test_append_italian(self):
        assert u'mario와' == hanpp.append(u'mario', u'과', lang='ita')
        assert u'luigi는' == hanpp.append(u'luigi', u'은', lang='ita')
        assert u'italian이' == hanpp.append(u'italian', u'가', lang='ita')


def suite():
    suite = unittest.TestSuite()
    suite.addTest(HangulPostpositionTestCase())
    return suite
