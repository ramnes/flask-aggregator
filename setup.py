from setuptools import setup


def get_description():
    with open("README.rst") as file:
        return file.read()


setup(
    name='Flask-Aggregator',
    version='0.2.0',
    url='https://github.com/ramnes/flask-aggregator',
    license='MIT',
    author='Guillaume Gelin',
    author_email='contact@ramnes.eu',
    description='Batch the GET requests to your REST API into a single POST',
    long_description=get_description(),
    py_modules=['flask_aggregator'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=['Flask'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
