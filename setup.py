import pathlib

from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name='pswd_validator',
    version='0.1',
    description="Checks the password for Digital Identity Guidelines compliance",
    long_description=README,
    long_description_content_type="text/markdown",
    author="Valera Maniuk",
    author_email="valeramaiuk@protonmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click",
        "flake8",
        "mock",
        "pytest",
        "tox",
    ],
    entry_points={
        'console_scripts': [
            'pswd_validator=pswd_validator.main:main',
        ],
    }
)
