import pytest
from _pytest.fixtures import SubRequest

@pytest.mark.parametrize("number", [1, 2, 3, -1])
def test_numbers(number: int):
    assert number > 0


@pytest.mark.parametrize("number, expected", [(1, 1), (2, 4), (3, 9)])
def test_several_numbers(number: int, expected: int):
    assert number ** 2 == expected

@pytest.mark.parametrize("os", ["macos", "windows", "linux", "debian"])
@pytest.mark.parametrize("host",[
    "http",
    "ws",
    "grp",
])
def test_mult_numbers(os: str, host: str):
    assert len(os+host) > 0

@pytest.fixture(params=[
    "http",
    "ws",
    "grp",
])
def host(request: SubRequest) -> str:
    return request.param

def test_host(host: str):
    print(f"Running test on host:{host}")

@pytest.mark.parametrize("user", ["Alice, Zara"])
class TestOperations:
    def test_user_with_operation(self, user:str):
        print(f"User with operation {user}")
    def test_user_without_operation(self, user:str):
        print(f"User without operation {user}")

users = {
    "+790":  "User with money",
    "+324":  "User with money",
    "+332": "User with operations",
}

@pytest.mark.parametrize(
    "phone_number",
    users.keys(),
    ids=lambda phone_number: f"{phone_number}: {users[phone_number]}"
)
def test_identifiers(phone_number: str):
    pass