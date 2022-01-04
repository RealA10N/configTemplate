from setuptools import setup, find_packages


def load_readme():
    with open('README.md', encoding='utf8') as readme:
        return readme.read()


EXTRAS = {
    'dev': (
        'pytest>=6.2, <6.3',
        'flake8>=3.9, <3.10'
    ),
}


REQUIRES = (
    # the dataclasses module is prebuilt into python>=3.7
    # For Python 3.6, it is supported using a backport
    'dataclasses; python_version < "3.7"',
)


setup(
    name='validit',
    description='Easily define and validate configuration file structures 📂🍒',
    version='2.0.0-dev',
    author='RealA10N',
    author_email='downtown2u@gmail.com',
    long_description=load_readme(),
    long_description_content_type='text/markdown',
    url='https://github.com/RealA10N/validit',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Operating System :: OS Independent',
    ],
    packages=find_packages(),
    python_requires='>=3.6',
    install_requires=REQUIRES,
    extras_require=EXTRAS,
)
