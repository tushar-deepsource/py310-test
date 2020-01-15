from http import HTTPStatus


def get_status(code):
    return HTTPStatus(code)


get_status(200)
