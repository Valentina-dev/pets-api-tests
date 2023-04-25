import requests.packages.urllib3

from test.test_pet.test_pet_negative import TestCreate, TestDelete, TestEdit  # noqa
from test.test_pet.test_pet_positive import TestEdit, TestDelete, TestCreate  # noqa

requests.packages.urllib3.disable_warnings()
