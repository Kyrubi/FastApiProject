def user_entity(item) -> dict: 
    return {
        "id":item["id"],
        "name": item["name"], 
        "email": item["email"],
        "password": item["password"]
    }
def users_entity(entity) -> list:
    return [user_entity(item) for item in entity]