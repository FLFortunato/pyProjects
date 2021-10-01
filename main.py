

from typing import Optional
from fastapi import FastAPI


from tortoise.contrib.fastapi import register_tortoise
from Routes import userRoutes

app = FastAPI()
app.include_router(userRoutes.router)


register_tortoise(
    app,
    db_url='postgres://postgres:postgres@localhost:5432/db',
    modules={'models': ['Models.userModel']},
    generate_schemas=True,
    add_exception_handlers=True
)

