from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi

from app.db.models import User
from app.users.schemas import UserCreate, UserRead, UserUpdate
from app.users.user_manager import auth_backend, current_active_user, fastapi_users


def my_schema():
    # Cache the Documentation Object
    if app.openapi_schema:
        return app.openapi_schema

    tags_metadata = [
        {
            "name": "users",
            "description": "Read, Update and Delete already existing users.",
        },
        {
            "name": "auth",
            "description": "Operations associated with passwords, ie. login, create new user, reset password.",
        },
        {
            "name": "shoppingList",
            "description": "Manage shopping list. Create, Read, Update, Delete",
        },
        {
            "name": "default",
            "description": "Miscellaneous stuff, exists due to quick PoC development.",
        },
    ]
    openapi_schema = get_openapi(
        title="Zakupy API",
        version="0.1a",
        description="Backend API used by mobile app for home resource management.",
        routes=app.routes,
        tags=tags_metadata,
    )
    app.openapi_schema = openapi_schema

    return app.openapi_schema


app = FastAPI()
app.openapi = my_schema

# TODO: tmp
origins = ["*"]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# app.include_router(users.router)
@app.get("/hello")
async def hello_world():
    return "Hello, World!"


app.include_router(
    fastapi_users.get_auth_router(auth_backend), prefix="/auth/jwt", tags=["auth"]
)
app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_reset_password_router(),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_verify_router(UserRead),
    prefix="/auth",
    tags=["auth"],
)
app.include_router(
    fastapi_users.get_users_router(UserRead, UserUpdate),
    prefix="/users",
    tags=["users"],
)


@app.get("/authenticated-route")
async def authenticated_route(user: User = Depends(current_active_user)):
    return {"message": f"Hello {user.email}!"}
