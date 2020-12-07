##### Disclaimer: 

This is just a lab to help me to brush up on some fundamentials.

# Password Validator

Simple CLI tool to check the strength of the passwords against  Digital Identity Guidelines as of June 2017
Specifically a password MUST:
- Have an 8 character minimum
- AT LEAST 64 character maximum
- Allow all ASCII characters and spaces (unicode optional) **In the current version only ASCII letters, digits and punctuation is allowed**
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

TBD (no machine available for testing atm)

## Usage example
![usage example](https://github.com/valeramaniuk/pswd_validator/blob/main/img/example.gif)


For all available options
```sh
pswd_validator --help
```

Windows: To pipe the newline separated file into the validator
```sh
type pass.txt | pswd_validator
```
To check against the file of known weak passwords
```sh
pswd_validator -f=/path/to/weakpasswords.txt
```
To fetch ~1M of weak passwords from the Internet and check against them. Currently it fetches the file on every run without saving it locally.
```sh
pswd_validator  --fetch-common-passwords
```
Remote and local weak passwords files can be used on the same run.

## Development setup
Activate your [virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
```sh
git clone git@github.com:valeramaniuk/pswd_validator.git
cd pswd_validator
pip install -rrequirements.txt
```
to run unit and integrations tests, the linter(flake8), and a code coverage check simply:
```sh
tox
```
## Release History

* 0.0.1
    * MVP, with functionality and deployment tested on Win10 only
* 0.0.2
    * README and help fixed and expanded
* 0.1.0
    * requirements.txt added
## Meta

Valera Maniuk –  valeramaniuk@protonmail.com

Distributed under the MIT license. 

[https://github.com/valeramaniuk/pswd_validator](https://github.com/valeramaniuk/pswd_validator)

## Roadmap

- [ ] Expand the character set, make it configurable
- [ ] Save the weak passwords file after fetching
- [ ] Allow check against multiple files of weak passwords

## Contributing

1. Fork it (<https://github.com/valeramaniuk/pswd_validator/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
6. Please keep code coverage at the level you found it with :)


