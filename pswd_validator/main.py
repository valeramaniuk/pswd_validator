import sys
from string import ascii_letters, digits, punctuation
import urllib.request
from typing import List
import click
import logging

logging.basicConfig(format='%(levelname)s - %(message)s')

VALID_CHARACTERS = set(ascii_letters + digits + punctuation)

DEFAULT_WEAK_PASS_FILE_URL = \
    "https://github.com/danielmiessler/SecLists/raw/" \
    "master/Passwords/Common-Credentials/10-million-password-list-top-1000000.txt"

default_config = {
    "nocheck_length": False,
    "nocheck_commonality": False,
    "nocheck_character_set": False,
    "max_length": 64,
    "min_length": 8
}


class PasswordChecker:
    def __init__(self, common_passwords: set, config: dict):
        self.common_passwords = common_passwords
        self.min_length = config["min_length"]
        self.max_length = config["max_length"]
        self.nocheck_length = config["nocheck_length"]
        self.nocheck_commonality = config["nocheck_commonality"]
        self.nocheck_character_set = config["nocheck_character_set"]
        self.valid_characters = VALID_CHARACTERS

    def check(self, password) -> List[str]:
        validation_errors = []

        def is_charset_valid():
            error_msg = "has invalid characters: {}"
            invalid_chars = set()

            for ch in set(password):
                if ch not in self.valid_characters:
                    invalid_chars.add(ch)
            if invalid_chars:
                print(invalid_chars)
                validation_errors.append(error_msg.format(r",".join(list(invalid_chars))))

        def is_length_valid():
            password_length = len(password)
            if self.min_length > password_length:
                validation_errors.append("is too short")
            elif self.max_length < password_length:
                validation_errors.append("is too long")

        def is_not_common():
            if password in self.common_passwords:
                validation_errors.append("is too common")

        if not self.nocheck_character_set:
            is_charset_valid()
        if not self.nocheck_length:
            is_length_valid()
        if not self.nocheck_commonality:
            is_not_common()

        return validation_errors


@click.command()
@click.option('-f', '--common-passwords-path', default=None, type=str,
              help="Path to the filename containing common passwords")
@click.option('--nocheck-common_passwords', is_flag=True,
              help="Disables check of the password against the set of the most common passwords")
@click.option('--nocheck-char-set', is_flag=True,
              help="Disables check of the character set for the password ")
@click.option('--nocheck-length', is_flag=True, help="Disables check of the length of the password")
@click.option(
    '--fetch-common-passwords',
    is_flag=True,
    help='Fetches the set of ~1M of common passwords from the {}'.format(DEFAULT_WEAK_PASS_FILE_URL)
)
def main(fetch_common_passwords, nocheck_length, nocheck_char_set, nocheck_common_passwords, common_passwords_path):
    default_config["nocheck_character_set"] = nocheck_char_set
    default_config["nocheck_length"] = nocheck_length
    default_config["nocheck_commonality"] = nocheck_common_passwords

    if not fetch_common_passwords and not common_passwords_path:
        logging.warning("The common passwords file is not supplied. Continuing without the validations of commonality")

    common_passwords = get_common_passwords(filename=common_passwords_path, get_default_remote=fetch_common_passwords)

    password_checker = PasswordChecker(common_passwords=common_passwords, config=default_config)
    while True:
        line = sys.stdin.readline()

        if line.rstrip() == '':
            exit(0)

        if validation_errors := password_checker.check(line.rstrip()):
            click.echo("{} -> Error: {}".format(line.rstrip(), ", and ".join(validation_errors)))


def get_common_passwords(filename, get_default_remote) -> set:
    common_passwords = set()

    def get_remote_default_common_passwords() -> set:
        nonlocal common_passwords
        with urllib.request.urlopen(DEFAULT_WEAK_PASS_FILE_URL) as r:
            body = r.read().decode('utf-8')
            common_passwords |= {x for x in body.split('\n')}
        return common_passwords

    if get_default_remote:
        try:
            get_remote_default_common_passwords()
        except ValueError:
            logging.error("URL {} cannot be reached and common passwords file cannot be fetched. Aborting...")
            sys.exit(1)

    if filename:
        try:
            with open(filename, 'r') as f:
                for line in f.readlines():
                    common_passwords.add(line.rstrip('\n'))
        except FileNotFoundError as e:
            logging.error("{}, current is. Aborting...".format(str(e)))
            sys.exit(1)

    return common_passwords
