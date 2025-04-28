from setuptools import setup, find_packages

setup(
    name='devgenie',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'typer',
        'httpx',
        'python-dotenv',
    ],
    entry_points={
        'console_scripts': [
            'devgenie=devgenie.cli:app',
        ],
    },
)
