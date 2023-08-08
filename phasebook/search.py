from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    filtered_users = []
    
    for user in USERS:
        match = True
        
        if "name" in args and args["name"].lower() not in user.get("name").lower():
            match = False
        
        if "id" in args and args["id"] != user.get("id"):
            match = False
        
        if "age" in args and args["age"] != str(user.get("age")):
            match = False
        
        if "occupation" in args and count_substring(args["occupation"].lower(), user.get("occupation").lower()) == 0:
            match = False
        
        if match:
            filtered_users.append(user)
    
    return filtered_users

def count_substring(substring, string):
    return string.count(substring)
