import pytest


@pytest.fixture(scope="package")
def package_fixture():
    print("package fixture set up")
    yield
    print("package fixture teardown")
