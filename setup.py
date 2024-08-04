# setup.py

from setuptools import setup, find_packages

setup(
    name='snake_rl',
    version='0.1.0',
    description='A Snake game AI using Deep Q-Learning',
    author='Your Name',
    author_email='gaurav@gaurav.com',
    url='https://github.com/9Gaurav9/snake_rl',  
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pygame',
        'keras',
        'tensorflow'
    ],
    entry_points={
        'console_scripts': [
            'snake_rl_train=snake_rl.train:main',
        ],
    },
)
