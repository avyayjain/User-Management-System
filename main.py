import uvicorn
from fastapi import FastAPI
# from dotenv import load_dotenv
from fastapi.exceptions import RequestValidationError

# load_dotenv()

from src.resources import (

    task_router,

)
from src.db.errors import DataBaseErrors
from src.resources.errors import FileErrors
from src.common.error_handlers import (
    database_error_handler,
    global_exception_handler,
    validation_error_handler,
    file_error_handler
)

app = FastAPI()

app.include_router(task_router, prefix='/task')

# Exception Handling
app.add_exception_handler(DataBaseErrors, database_error_handler)
app.add_exception_handler(FileErrors, file_error_handler)
app.add_exception_handler(RequestValidationError, validation_error_handler)
app.middleware('http')(global_exception_handler)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
