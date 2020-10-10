import os
from setuptools import setup

django_refer = __import__('django_refer')
VERSION = '1.0.0'

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name="django-refer",
    version=django_refer.__version__,
    include_package_data=True,
    packages=['django-refer'],
    url='https://github.com/shakyasaijal/django-refer',
    license='MIT',
    description="Refer and Reward application for Django.",
    long_description=README,
    author='Saijal Shakya',
    author_email='saijalshakya@gmail.com',
    version=VERSION
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    zip_safe=False,
)