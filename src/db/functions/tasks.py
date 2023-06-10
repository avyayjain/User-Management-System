from src.db.database import Task
from src.db.errors import NoEntityFound, UserErrors
from src.db.sync_session import DBConnection
from src.common.utils.generate_logs import logging, generate_details
from fastapi import HTTPException


def get_task_db():
    try:
        with DBConnection(False) as session:
            tasks = session.query(Task).all()
            response = []
            for task in tasks:
                curr_task = {
                    'id': task.id,
                    'Title': task.title,
                    'desc': task.desc,
                    'due_date': task.due_date,
                    'status': task.status
                }
                response.append(curr_task)

        return response
    except Exception as e:
        error_msg = (
            f"Tasks having error {e}"
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)


def update_task_db(task_id, updated_task):
    try:
        with DBConnection(False) as session:
            task = session.query(Task).filter(Task.id == task_id).first()

            if task is None:
                raise NoEntityFound()

            task.title = updated_task.title
            task.desc = updated_task.desc
            task.due_date = updated_task.due_date
            task.status = updated_task.status

            session.add(task)
            session.commit()
    except UserErrors as e:
        error_msg = (
            f"Tasks id {task_id} having error {e.message}"
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)
    except Exception:
        error_msg = "editor_id :" + str(task_id) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)


def add_task_db(new_task):
    try:
        with DBConnection(False) as session:
            task = Task(title=new_task.title, desc=new_task.desc, due_date=new_task.due_date, status=new_task.status)
            session.add(task)
            session.commit()
            return task.id
    except UserErrors as e:
        error_msg = (
            f"Task {new_task} having error {e.message}"
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)
    except Exception:
        error_msg = "editor_id :" + str(new_task) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)


def delete_task_db(task_id):
    try:
        with DBConnection(False) as session:
            task = session.query(Task).filter(Task.id == task_id).first()

            if task is None:
                raise NoEntityFound()

            session.delete(task)
            session.commit()
    except UserErrors as e:
        error_msg = (
                f"Tasks id {task_id} having error {e.message}"
        )
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details(e.message, e.type)
        raise HTTPException(status_code=e.response_code, detail=details)
    except Exception:
        error_msg = "editor_id :" + str(task_id) + "\n"
        logging.warning(error_msg, exc_info=True)
        with open("error.log", "a") as f:
            f.write(
                "================================================================== \n"
            )
        details = generate_details("Internal Server Error", "InternalServerError")
        raise HTTPException(status_code=500, detail=details)
