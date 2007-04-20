from ez_setup import use_setuptools
use_setuptools()
from setuptools import setup, find_packages

setup(
    name='Restin',
    version="",
    #description="",
    #author="",
    #author_email="",
    #url="",
    install_requires=["Pylons>=0.9.5"],
    packages=find_packages(),
    include_package_data=True,
    test_suite = 'nose.collector',
    package_data={'restin': ['i18n/*/LC_MESSAGES/*.mo']},
    entry_points="""
    [paste.app_factory]
    main=restin:make_app
    [paste.app_install]
    main=pylons.util:PylonsInstaller
    """,
)
