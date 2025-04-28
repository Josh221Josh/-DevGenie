from setuptools import setup, find_packages

setup(
    name='devgenie',
    version='0.1.0',
    author='Joshua Teyi Tukuh',
    author_email='teyilliongroup006@gmail.com',
    description='AI-powered CLI assistant for developers using OpenAI Codex/GPT',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/josh221josh/devgenie',
    license='MIT',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Development Status :: 4 - Beta',
    ],
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
    python_requires='>=3.8',
)
