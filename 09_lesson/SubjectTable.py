from sqlalchemy import create_engine
from sqlalchemy.sql import text


class SubjectTable:
    __scripts = {
        "select_all": text("select * from subject"),
        "select_by_id": text("select * from subject where subject_id = :id"),
        "create_subject": text("insert into subject (subject_id, subject_title)"
                               " values (:id, :subject_title)"),
        "delete_subject": text("delete from subject where subject_id = :id"),
        "edit_subject": text("update subject set subject_title = :title "
                             "where subject_id = :subject_id")
    }

    def __init__(self, db_adress):
        self.db = create_engine(db_adress)

    def get_subjects(self):
        return self.db.execute(self.__scripts["select_all"]).fetchall()

    def create_subject(self, new_id, title):
        self.db.execute(self.__scripts["create_subject"], id=new_id,
                        subject_title=title)
        return print('Предмет успешно создан')

    def delete_subject(self, delete_id):
        self.db.execute(self.__scripts["delete_subject"], id=delete_id)
        return print('Предмет успешно удален')

    def edite_subject(self, id, edit_title):
        self.db.execute(self.__scripts["edit_subject"], subject_id=id,
                        title=edit_title)
        return print('Предмет успешно изменен')

    def get_subject_by_id(self, selected_id):
        return self.db.execute(self.__scripts["select_by_id"],
                               id=selected_id).fetchall()
