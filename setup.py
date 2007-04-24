from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(
    name='Restin',
    version='0.1a0',
    description='RESTful admin app for Pylons',
    long_description='',
    author='Wyatt L Baldwin, byCycle.org',
    author_email='wyatt@byCycle.org',
    license='MIT',
    url='http://code.google.com/p/restin/',
    keywords='web pylons REST admin',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Paste',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        ],
    install_requires=(
        'Pylons>=0.9.5',
        'Elixir>=0.3.0',
        'simplejson>=1.7.1',
        'Restler',
        ),
    packages=find_packages(),
    include_package_data=True,
    package_data={'restin': ['i18n/*/LC_MESSAGES/*.mo']},
    zip_safe=False,
    test_suite = 'nose.collector',
    entry_points="""
    [paste.app_factory]
    main=restin:make_app
    [paste.app_install]
    main=pylons.util:PylonsInstaller
    """,
)
