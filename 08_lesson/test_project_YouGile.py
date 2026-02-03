import requests
from project_YouGile import ProjectYouGile

users = {"https://ru.yougile.com/api-v2/": "admin"}
api = ProjectYouGile("https://ru.yougile.com/api-v2/")


def test_create_project():
    projects_before = api.get_project_list()
    len_before = len(projects_before)
    project_id = api.create_project("New_Project_Test", users)
    projects_after = api.get_project_list()
    len_after = len(projects_after)

    assert len_after - len_before == 0

    api.edit_project(project_id, True, "Delete_Project_Test")


def test_get_project_with_id():
    result = api.create_project("Get_Project_Test", users)
    project_id = result['id']
    new_project = api.get_project_with_id(project_id)

    assert new_project['title'] == "Get_Project_Test"
    assert new_project['users'] == users

    api.edit_project(project_id, True, "Delete_Project_Test")


def test_edit_project():
    result = api.create_project("Edit_Project_Test", users)
    project_id = result['id']
    api.edit_project(project_id, False, "Edit_Project_Test")
    edited = api.get_project_with_id(project_id)

    assert edited['title'] == "Edit_Project_Test"

    api.edit_project(project_id, True,"Edit_Project_Test")