import allure
from extensions.api_actions import API_Actions


@allure.step("get_request")
def get_request(url):
    response = API_Actions.get(url)
    return response

@allure.step("post_request")
def post_request(url, payload):
    response = API_Actions.post(url, payload)
    return response


@allure.step("delete_request")
def delete_request(url, id):
    response = API_Actions.delete(url, id)
    return response
