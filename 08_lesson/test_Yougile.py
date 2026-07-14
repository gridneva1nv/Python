from YougileApi import YougileAPI
import config


api = YougileAPI(config.BASE_URL)
api_key = api.get_token()
projects_id = []


def test_create_project_positive():
    project_list = api.get_project_list(api_key)
    project_list_json = project_list.json()
    projects_before = project_list_json["paging"]["count"]
    new_title = "New Project positive"
    users = {
        config.USER_ID: "admin"
    }
    result = api.create_project(api_key, new_title, users)
    print(result.json())
    # запишем для финальной чистки базы
    projects_id.append(result.json()["id"])

    project_list = api.get_project_list(api_key)
    projects_after = project_list.json()["paging"]["count"]

    # статус код = 201
    assert result.status_code == 201
    assert projects_after - projects_before == 1, (
        print('Количество проектов не увеличилось'))
    assert project_list.json()["content"][-1]["title"] == new_title


def test_create_project_negative():
    project_list = api.get_project_list(api_key)
    projects_before = project_list.json()["paging"]["count"]
    title = ""
    users = {
        config.USER_ID: "admin"
    }
    result = api.create_project(api_key, title, users)
    project_list = api.get_project_list(api_key)
    projects_after = project_list.json()["paging"]["count"]

    assert result.status_code > 299
    print(f'Ошибка: {result.json()["error"]} - {result.json()["message"]}')
    assert projects_after - projects_before == 0


def test_get_project_positive():
    # создать проект
    title = "Geted project positive"
    users = {
        config.USER_ID: "worker"
    }
    project = api.create_project(api_key, title, users)
    new_id = project.json()["id"]
    projects_id.append(new_id)  # запишем для финальной чистки базы

    result = api.get_project(api_key, new_id)

    assert result.status_code == 200
    assert result.json()["title"] == title
    assert result.json()["users"] == users


def test_get_project_negative():
    # создать проект
    title = "Geted project negative"
    users = {
        config.USER_ID: "worker"
    }
    project = api.create_project(api_key, title, users)
    new_id = project.json()["id"]
    projects_id.append(new_id)
    negative_id = "1"

    result = api.get_project(api_key, negative_id)

    assert result.status_code > 299
    print(f'Ошибка: {result.json()["error"]} - {result.json()["message"]}')


def test_edit_project_positive():
    # создать проект
    title = "Edited project positive"
    users = {
        config.USER_ID: "worker"
    }
    project = api.create_project(api_key, title, users)
    new_id = project.json()["id"]
    projects_id.append(new_id)

    # редактировать проект
    new_title = "Измененное название"
    edited = api.edit_project(api_key, new_id, new_title)
    result = api.get_project(api_key, new_id)

    assert edited.status_code == 200
    assert result.json()["title"] == new_title


def test_edit_project_negative():
    # создать проект
    title = "Edited project negative"
    users = {
        config.USER_ID: "worker"
    }
    project = api.create_project(api_key, title, users)
    print(project.json())
    new_id = project.json()["id"]

    # редактировать проект
    new_title = ""
    edited = api.edit_project(api_key, new_id, new_title)
    print(edited.json())
    project = api.get_project(api_key, new_id)

    assert edited.status_code > 299
    print(f'Ошибка: {edited.json()["error"]} - {edited.json()["message"]}')
    assert project.json()["title"] == title
    assert project.json()["users"] == users


def test_delete_project_positive():
    count_id = len(projects_id)
    project_list = api.get_project_list(api_key)
    projects_before = project_list.json()["paging"]["count"]
    for id in projects_id:
        api.edit_project(api_key, id, "delete", True)
    project_list = api.get_project_list(api_key)
    projects_after = project_list.json()["paging"]["count"]

    assert projects_before - projects_after == count_id
