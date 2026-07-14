import requests
import config


class YougileAPI:
    def __init__(self, url):
        self.url = url

    def get_token(self):
        body = {
            "login": config.LOGIN,
            "password": config.PASSWORD,
            "companyId": config.COMPANY_ID
        }
        resp = requests.post(self.url + '/api-v2/auth/keys', json=body)
        print(resp.json())
        key = resp.json()["key"]
        return key


    def create_project(self, api_key, project_title, project_users):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        body = {
            "title": project_title,
            "users": project_users
        }
        resp = requests.post(self.url + "/api-v2/projects", json = body, headers = headers)
        return resp

    def get_project(self, api_key, project_id):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        resp = requests.get(self.url + f'/api-v2/projects/{project_id}', headers=headers)
        return resp

    def edit_project(self, api_key, project_id, new_title, deleted = False):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        data = {
            "deleted": deleted,
            "title": new_title
        }
        resp = requests.put(self.url + f'/api-v2/projects/{project_id}', json = data, headers = headers)
        return resp

    def get_project_list(self, api_key):
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + api_key
        }
        resp = requests.get(self.url +'/api-v2/projects', headers=headers)
        return resp

