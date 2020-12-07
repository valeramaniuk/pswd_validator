# Password Validator

Simple CLI tool to check the strength of the passwords against  Digital Identity Guidelines as in of June 2017
Specifically a password MUST:
- Have an 8 character minimum
- AT LEAST 64 character maximum
- Allow all ASCII characters and spaces (unicode optional) **unicode is disallowed in the current version**
- Not be a common password

It can be supplied with the newline separated file containing known weak passwords or the tool can fetch ~1M
of weak passwords at execution time.
Individual checks can be disabled with the corresponding flags.


## Installation
Windows:

```sh
python -m pip install --extra-index-url https://test.pypi.org/simple/ pswd_validator
```

OS X & Linux:

TBD

## Usage example
![usage example](https://github.com/valeramaniuk/pswd_validator/img/example.gif)


For all available options
```sh
pswd_validator --help
```

## Development setup
Activate your [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```sh
git clone git@github.com:valeramaniuk/pswd_validator.git
pip install -rrequirements.txt
```
to run unit and integrations tests, the linter(flake8), and a code coverage check simply:
```sh
tox
```
## Release History

* 0.0.1
    * MVP, with functionality and deployment tested on Win10 only

## Meta

Valera Maniuk –  valeramaniuk@protonmail.com

Distributed under the MIT license. 

[https://github.com/valeramaniuk/pswd_validator](https://github.com/valeramaniuk/pswd_validator)

## Contributing

1. Fork it (<https://github.com/valeramaniuk/pswd_validator/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


