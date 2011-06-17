# -*- coding: utf-8 -*-
"""
Josa
~~~~

Appends the correct postposition to a given word by checking whether the word
has jongseong (final consonant) or not.

>>> print josa.append('false positive', u'를')
false positive를
>>> print josa.append('deterministic', u'랑')
deterministic이랑

"""
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def run_tests():
    from test import suite
    return suite()


setup(
    name='josa',
    version='0.0.1',
    license='BSD',
    author='Heungsub Lee',
    author_email='h@subl.ee',
    description='Appends the correct korean postposition',
    long_description=__doc__,
    platforms='any',
    install_requires=['hangulize'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: Korean',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Text Processing :: Linguistic'
    ],
    test_suite='__main__.run_tests'
)
