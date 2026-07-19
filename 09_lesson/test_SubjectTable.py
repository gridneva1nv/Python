import config
from SubjectTable import SubjectTable

db_connection = f'postgresql://{config.MYUSER}:{config.MYPASSWORD}@localhost:5432/QA'
db = SubjectTable(db_connection)


def test_add_subject():
    subjects_list = db.get_subjects()
    before = len(subjects_list)
    # создаем новый предмет
    new_id = before + 1
    new_title = "Создаваемый предмет"
    db.create_subject(new_id, new_title)
    new_subject = db.get_subject_by_id(new_id)

    subjects_list = db.get_subjects()
    after = len(subjects_list)
    # удаляем созданный предмет
    db.delete_subject(new_id)

    assert after - before == 1, '! Строка не добавлена'
    assert new_subject[0]["subject_title"] == new_title, \
        '! Наименование не добавлено'


def test_delete_subject():
    subjects_list = db.get_subjects()
    new_id = len(subjects_list) + 1
    new_title = "Удаляемый предмет"
    db.create_subject(new_id, new_title)
    subjects_list = db.get_subjects()
    before = len(subjects_list)

    db.delete_subject(new_id)
    subjects_list = db.get_subjects()
    after = len(subjects_list)

    find = False
    for subject in subjects_list:
        if subject["subject_title"] != new_title:
            find = True

    subject = db.get_subject_by_id(new_id)

    assert before - after == 1, '! Строка не удалена'
    assert find, '! Наименование все еще присутствует в списке'
    assert len(subject) == 0, '! ID не удален'


def test_edit_subject():
    subjects_list = db.get_subjects()
    id = len(subjects_list) + 1
    new_title = "Изменяемый предмет"
    db.create_subject(id, new_title)
    before = len(subjects_list)

    edit_title = "Название изменили"
    db.edite_subject(id, edit_title)
    subject = db.get_subject_by_id(id)
    after = len(subjects_list)

    db.delete_subject(id)

    assert subject[0]["subject_title"] == edit_title, \
        '! Наименование не изменено'
    assert before == after, '! Количество строк изменилось'
