import allure
import requests

class API_Actions:

    @allure.step("get posts")
    def get(url):
        response = requests.get(url)
        return response

    @allure.step("post one post")
    def post(url, payload):
        response = requests.post(url, json=payload, headers={'Content-Type': 'application/json'})
        return response

    @allure.step("delete post by ID")
    def delete(url, id):
        response = requests.delete(url + id)
        return response


