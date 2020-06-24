from io import open
from setuptools import setup

with open('README.md') as read_me:
    long_description = read_me.read()

setup(
    name='Eel-Flask',
    version='0.0.1',
    author='Kelly',
    url='https://github.com/guo40020/Eel-Flask',
    packages=['eel_flask'],
    package_data={
        'eel_flask': ['eel_flask.js'],
    },
    install_requires=['flask', 'flask_sockets', 'whichcraft'],
    python_requires='>=3.5',
    description='For little HTML GUI applications, with easy Python/JS interop',
    long_description=long_description,
    long_description_content_type='text/markdown',
    keywords=['gui', 'html', 'javascript', 'electron'],
)
