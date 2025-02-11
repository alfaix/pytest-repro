To reproduce, run "pytest -vv".

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
top_level_test.py::test_top_level module fixture setup
PASSEDmodule fixture teardown
package fixture teardown


============================================================================================================== 2 passed in 0.01s ===============================================================================================================
```
While the expectation is for "package fixture teardown" to happen right after package_test.py is done, before top_level_test.py is invoked
