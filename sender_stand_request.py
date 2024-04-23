import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)
def get_users_table():
        return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)


response = post_new_user(data.user_body)
response2 = get_users_table()
print(response.status_code)
print(response.json())