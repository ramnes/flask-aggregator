from setuptools import setup


def get_description():
    with open("README.rst") as file:
        return file.read()


setup(
    name='Flask-Aggregator',
    version='0.1',
    url='',
    license='MIT',
    author='Guillaume Gelin',
    author_email='contact@ramnes.eu',
    description='Requests aggregator for Flask.',
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
