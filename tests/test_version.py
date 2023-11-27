from palgo import __version__


def test_version_exist():
    assert isinstance(__version__, str)
