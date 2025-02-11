import pytest


@pytest.fixture(scope="module")
def module_fixture():
    print("module fixture setup")
    yield
    print("module fixture teardown")


def test_top_level(module_fixture):
    pass
