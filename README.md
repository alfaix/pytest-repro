To reproduce, run "pytest -vv --capture=no".

Output:
```
============================================================================================================= test session starts ==============================================================================================================
platform linux -- Python 3.10.11, pytest-8.3.4, pluggy-1.5.0 -- /home/akitov/.pyenv/versions/3.10.11/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/akitov/pytest-repro
plugins: anyio-4.3.0
collected 2 items

package/package_test.py::test_package package fixture set up
PASSED
top_level_test.py::test_top_level PASSEDpackage fixture teardown


============================================================================================================== 2 passed in 0.01s ===============================================================================================================
```

**If you do touch `package/__init__.py`**, the output changes:
```
============================================================================================================= test session starts ==============================================================================================================
platform linux -- Python 3.10.11, pytest-8.3.4, pluggy-1.5.0 -- /home/akitov/.pyenv/versions/3.10.11/bin/python3.10
cachedir: .pytest_cache
rootdir: /home/akitov/pytest-repro
plugins: anyio-4.3.0
collected 2 items

package/package_test.py::test_package package fixture set up
PASSEDpackage fixture teardown

top_level_test.py::test_top_level PASSED

============================================================================================================== 2 passed in 0.01s ===============================================================================================================
```

The expectation is that `__init__.py` should not define Python packages (it's not required as of Python3), or at least this behavior should be documented.
