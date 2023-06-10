from fastapi import APIRouter

from src.resources.pydantic_schemas.tasks import Task as task_basemodel
from src.db.functions.tasks import update_task_db, add_task_db, delete_task_db, \
    get_task_db
task_router = APIRouter()


@task_router.get('/list')
async def get_all_tasks():
    return {'data': get_task_db()}


@task_router.post('/add')
def add_task(task: task_basemodel):
    task_id = add_task_db(task)

    return {'detail': 'task Created Successfully', 'task_id': task_id}


@task_router.put('/update')
async def update_task(task_id: int, task: task_basemodel):
    update_task_db(task_id, task)

    return {
        'detail': "task Updated Successfully."
    }


@task_router.delete('/delete')
def delete_task(task_id: int):
    delete_task_db(task_id)

    return {
        'detail': "task Deleted Successfully."
    }
