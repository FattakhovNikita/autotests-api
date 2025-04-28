from clients.users.users_schema import CreateUserRequestSchema, CreateUserResponseSchema, UserSchema, \
    GetUserResponseSchema
from tests.conftest import UserFixture
from tools.assertions.base import assert_equal


def assert_create_user_response(request: CreateUserRequestSchema, response: CreateUserResponseSchema):
    """
    Проверяет, что ответ на создание пользователя соответствует запросу.

    :param request: Исходный запрос на создание пользователя.
    :param response: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(response.user.email, request.email, "email")
    assert_equal(response.user.last_name, request.last_name, "last_name")
    assert_equal(response.user.first_name, request.first_name, "first_name")
    assert_equal(response.user.middle_name, request.middle_name, "middle_name")


def assert_user(actual: UserSchema, expected: UserSchema):
    """

    Проверяет, что ответ на получение данных пользователя соответствует запросу.

    :param actual: Исходный запрос на получение данных пользователя.
    :param expected: Ответ API с данными пользователя.
    :raises AssertionError: Если хотя бы одно поле не совпадает.
    """
    assert_equal(expected.user.id, actual.user.id, "id")
    assert_equal(expected.user.email, actual.user.email, "email")
    assert_equal(expected.user.last_name, actual.user.last_name, "last_name")
    assert_equal(expected.user.first_name, actual.user.first_name, "first_name")
    assert_equal(expected.user.middle_name, actual.user.middle_name, "middle_name")


def assert_get_user_response(get_user_response: GetUserResponseSchema, create_user_response: CreateUserResponseSchema):
    assert_user(get_user_response, create_user_response)
