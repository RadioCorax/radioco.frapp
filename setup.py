from setuptools import setup, find_packages
import sys, os

version = '0.1'

requires = [
#    'django-radio',
    'Django<1.9',
    'django-solo-grappelli',
]

setup(name='radioco.frapp',
      version=version,
      description="Manages xml metadata for Freie Radios App in RadioCo.",
      long_description="""\
XXX long description""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='radioco frn',
      author='Stefan Walluhn',
      author_email='stefan@walluhn.de',
      url='https://github.com/stefan-walluhn/radioco.frapp',
      license='GPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      namespace_packages=['radioco'],
      include_package_data=True,
      zip_safe=False,
      install_requires=requires,
#      dependency_links=['http://github.com/stefan-walluhn/django-radio/tarball/production#egg=django-radio-3.0'],
      tests_require=['django-nose'],
      test_suite='radioco.frapp.test.runner.runtests',
      entry_points="""
      # -*- Entry points: -*-
      """,
)
