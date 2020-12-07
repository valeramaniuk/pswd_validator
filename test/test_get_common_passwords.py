from mock import patch, MagicMock

from pswd_validator.main import get_common_passwords, sys


@patch('pswd_validator.main.DEFAULT_WEAK_PASS_FILE_URL', "FOOBAR")
def test_remote_file_read_fails_and_exits():
    with patch.object(sys, "exit") as mock_exit:
        get_common_passwords(None, True)
    assert mock_exit.call_args[0][0] == 1


@patch('pswd_validator.main.DEFAULT_WEAK_PASS_FILE_URL', "FOOBAR")
@patch('urllib.request.urlopen')
def test_remote_file_read_successful(mock_urlopen):
    cm = MagicMock()
    cm.read.return_value = b"fizz\nbuzz"
    cm.__enter__.return_value = cm
    mock_urlopen.return_value = cm
    result = get_common_passwords(None, True)

    assert mock_urlopen.call_args[0][0] == "FOOBAR"
    assert result == {"fizz", "buzz"}


def test_no_file_found():
    filename = "foo.bar"
    with patch.object(sys, "exit") as mock_exit:
        get_common_passwords(filename, False)
    assert mock_exit.call_args[0][0] == 1


def test_no_file_supplied_no_fetch_remote_no_error():
    get_common_passwords(None, False)


def test_common_passwords_file_read_ok():
    filename = "test/data/passwords.txt"
    f = get_common_passwords(filename, False)
    assert f == {"foo", "bar", "123"}
