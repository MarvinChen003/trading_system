### Python 测试
***
KEY WORD

Mocking - python unittest.mock (built-in)
- mock
- return_value
- side_effect
- MagicMock 
	
Patch
- use as decorator
- use as context manager

pytest
- fixture
- conftext

botocore
 - stub
boto3

***

**Mocking:** Create a fake object that represents the "real' object

- unnitest.mock (mock object library)
	- Provides the Mock class
	- Provides the patch() method

**Patch:** Replaces the real objects in your code with Mock instances.  
- example
	```
	>>> from unittest.mock import Mock
	>>> mock = Mock()
	>>> mock
	# Patch the json library
	>>> import json
	>>> json = mock
	```

- Lazy Attributes and Methods  

	```
	# mock id are different
	>>> json.dumps()
	>>> json.whatever()
	```
- Assertions and Inspection  

	```
	>>> dir(json)
	>>> dir(mock)
	# new terminal
	>>> from unittest.mock import Mock
	>>> mock = Mock()
	>>> dir(mock)
	```
	
**Managing a Mock’s Return Value**
忽略行为，关注输出

	```
	def say_hello(word):
	    return f"hello {word}"
	
	>>> say_hello("China")
	'hello China'
	
	>>> say_hello = mock
	>>> mock.return_value = "PYTHON GO"
	'PYTHON GO'
	
	# Notice object id
	>>> say_hello.whatever()
	```
	
**Managing a Mock’s Side Effects**  

You can control your code’s **behavior** by specifying a mocked function’s side effects.
改变行为

```
import unittest
from unittest.mock import Mock
# 注意这个包，前方高能
from requests.exceptions import Timeout

# Mock requests to control its behavior
requests = Mock()

# 如何测 requeset 超时了？改request的返回值没啥用。
def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        # 用 side_effect 改变程序行为，模拟超时
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_holidays()

if __name__ == '__main__':
    unittest.main()
```
改变程序行为，装饰器，切面编程
```
import requests
import unittest
from unittest.mock import Mock

# Mock requests to control its behavior
requests = Mock()

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None

class TestCalendar(unittest.TestCase):
    def log_request(self, url):
        # Log a fake request for test output purposes
        print(f'Making a request to {url}.')
        print('Request received!')

        # Create a new Mock to imitate a Response
        response_mock = Mock()
        response_mock.status_code = 200
        response_mock.json.return_value = {
            '12/25': 'Christmas',
            '7/4': 'Independence Day',
        }
        return response_mock

    def test_get_holidays_logging(self):
        # Test a successful, logged request
        requests.get.side_effect = self.log_request
        assert get_holidays()['12/25'] == 'Christmas'

if __name__ == '__main__':
    unittest.main()
```
改变程序行为还是有点危险，用不好，容易给自己带跑偏，core-stack的例子 （MOCK site effect STUBBER）

**Configuring Your Mock**
```
>>> mock = Mock(name='Real Python Mock')
>>> mock.name
<Mock name='Real Python Mock.name' id='4434041544'>

>>> mock = Mock()
>>> mock.name = 'Real Python Mock'
>>> mock.name
'Real Python Mock'
```
**patch()**
unittest.mock provides a powerful mechanism for mocking objects, called patch(), which looks up an object in a given module and replaces that object with a Mock.

Usually, you use patch() as a decorator or a context manager to provide a scope in which you will mock the target object.

my_calendar.py
```
import requests
from datetime import datetime

def is_weekday():
    today = datetime.today()
    # Python's datetime library treats Monday as 0 and Sunday as 6
    return (0 <= today.weekday() < 5)

def get_holidays():
    r = requests.get('http://localhost/api/holidays')
    if r.status_code == 200:
        return r.json()
    return None
```
test codes
```
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    @patch('my_calendar.requests')
    def test_get_holidays_timeout(self, mock_requests):
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```
**patch() as a Context Manager**
Sometimes, you’ll want to use patch() as a context manager rather than a decorator. Some reasons why you might prefer a context manager include the following:

You only want to mock an object for a part of the test scope.
You are already using too many decorators or parameters, which hurts your test’s readability.
```
import unittest
from my_calendar import get_holidays
from requests.exceptions import Timeout
from unittest.mock import patch

class TestCalendar(unittest.TestCase):
    def test_get_holidays_timeout(self):
        with patch('my_calendar.requests') as mock_requests:
            mock_requests.get.side_effect = Timeout
            with self.assertRaises(Timeout):
                get_holidays()
                mock_requests.get.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```
**Patching an Object’s Attributes**
**Where to Patch - target location** 这个test能一步引到的包

**MagicMock**
a subclass of Mock with default implementations of most of the magic methods.
```
#__setitem__:每当属性被赋值的时候都会调用该方法
#__getitem__:当访问不存在的属性时会调用该方法
from unittest.mock import MagicMock
mock = MagicMock()
mock[3] = 'fish'
mock.__setitem__.assert_called_with(3, 'fish')
#AssertionError
mock.__setitem__.assert_called_with(6, 'fish')
mock.__getitem__.return_value = 'result'
mock[2]
'result'
```

```
from unittest.mock import Mock, MagicMock
dir(Mock)
dir(MagicMock)
```
***
**pytest**
pytest is one of the best tools you can use to boost your testing productivity. pytest is a feature-rich, plugin-based ecosystem for testing your Python code.

**pytest fixtures** 
offer dramatic improvements over the classic xUnit style of setup/teardown functions:

When a setUp() method is defined, the test runner will run that method prior to each test. Likewise, if a tearDown() method is defined, the test runner will invoke that method after each test.

**In general you add all prerequisite steps to setUp and all clean-up steps to tearDown.**

```
import pytest

@pytest.fixture
def input_value():
   input = 39
   return input

def test_divisible_by_3(input_value):
   assert input_value % 3 == 0
```

- test_db_func_first_version.py
- test_db_func_setup_teardown.py
- test_db_func_fixture.py

fixture will automatically called when the starting and finishing of your code

The yield statement suspends function’s execution and sends a value back to the caller, but retains enough state to enable function to resume where it is left off. When resumed, the function continues execution immediately after the last yield run. This allows its code to produce a series of values over time, rather than computing them at once and sending them back like a list. 

把 fixture 定义到 conftest.py 中，可以跨脚本生效

***
**botocore**
Botocore is a low-level interface to a growing number of **Amazon Web Services**. Botocore serves as the foundation for the AWS-CLI command line utilities. It will also play an important role in the boto3.x project.

The boto package is the hand-coded Python library that has been around since 2006. It is very popular and is fully supported by AWS but because it is hand-coded and there are so many services available (with more appearing all the time) it is difficult to maintain.

So, boto3 is a new version of the boto library based on botocore. All of the low-level interfaces to AWS are driven from JSON service descriptions that are generated automatically from the canonical descriptions of the services. So, the interfaces are always correct and always up to date. There is a resource layer on top of the client-layer that provides a nicer, more Pythonic interface.

The boto3 library is being actively developed by AWS and is the one I would recommend people use if they are starting new development.

值得注意的是 boto3 并不能全面取代 botocore，比如 aws resource，再比如 stub

**botocore.stub**
class botocore.stub.Stubber(client)
**This class will allow you to stub out requests so you don't have to hit an endpoint to write tests**. Responses are returned first in, first out. If operations are called out of order, or are called with no remaining queued responses, an error will be raised.

**what core-stack does to associate mock with stub**
conftest
- boto_client_stub (boto3)
- several fixtures
	- e.g. ec2_client_stub (Stubber)
- mock_session (boto3 + mock)

e.g. test_moogsoft_alerting.py
