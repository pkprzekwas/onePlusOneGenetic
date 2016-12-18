from setuptools import setup

setup(
    name='Traveling Salesman',
    version='1.0',
    py_modules=['app/main'],
    install_requires=[
        'Click',
    ],
    entry_points='''
         [console_scripts]
         solve = app.main:run
    ''',
)
