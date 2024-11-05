from fastapi import APIRouter
from config.db import conn
from schemas.user import user_entity, users_entity
from models.user import User


user = APIRouter()

@user.get('/users')
def find_all_users():
    return users_entity(conn.local.user.find())


@user.post('/users')
def create_user(user: User):
    new_user = dict(user)
    id = conn.local.user.insert_one(new_user).inserted_id
    return id


@user.get('/users/{id}')
def find_user():
    return 'Hello World'


@user.put('/users/{id}')
def update_user():
    return 'Hello World'


@user.delete('/user/{id}')
def delete_user():
    return 'Hello World'
