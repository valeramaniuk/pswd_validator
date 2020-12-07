from click.testing import CliRunner
from pswd_validator.main import main


def test_bad_weak_passwords_file():
    runner = CliRunner()
    result = runner.invoke(main, ['--common-passwords-path=pass11.txt'])
    assert result.exit_code == 1


def test_character_validation():
    runner = CliRunner()
    result = runner.invoke(main, ['--common-passwords-path=test/data/common_passwords.txt'], input="\u267a")
    assert "invalid characters" in result.output

    result = runner.invoke(main, ['--common-passwords-path=test/data/common_passwords.txt'], input="normalpassword")
    assert "invalid characters" not in result.output


def test_size_validations():
    tests = [
        {"input": "short\n", "want": "short -> Error: is too short\n", "description": ""},
        {"input": "toolong" * 20 + "\n", "want": "{} -> Error: is too long".format("toolong" * 20) + "\n",
         "description": ""},
        {"input": "qwerty", "want": "qwerty -> Error: is too short, and is too common\n", "description": ""},
        {"input": "fdlkjgdfkljgdfjg3", "want": "", "description": "Password is OK"},
    ]

    runner = CliRunner()

    for test in tests:
        result = runner.invoke(main, ['--common-passwords-path=test/data/common_passwords.txt'], input=test["input"])

        assert not result.exception
        assert result.output == test["want"]

    result = runner.invoke(main, input="")
    assert result.exit_code == 0
