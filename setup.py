from setuptools import setup, find_packages
import os

version = '0.4.2'


def read(*rnames):
    return open(os.path.join(os.path.dirname(__file__), *rnames)).read()

long_description = (
    read('README.txt')
    + '\n' +
    read('js', 'jquery_notify', 'test.txt')
    + '\n' +
    read('CHANGES.txt'))

setup(
    name='js.jquery_notify',
    version=version,
    description="fanstatic JQuery Notify.",
    long_description=long_description,
    classifiers=[],
    keywords='',
    author='Heberte Fernandes de Moraes',
    author_email='brebete@gmail.com',
    url='https://github.com/hmoraes/js.jquery-notify',
    license='BSD',
    packages=find_packages(),
    namespace_packages=['js'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'fanstatic',
        'setuptools',
        'js.jquery>=1.12.4',
    ],
    entry_points={
        'fanstatic.libraries': [
            'jquery_notify = js.jquery_notify:library',
        ],
    },
)
