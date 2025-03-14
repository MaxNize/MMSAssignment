from db import db

def logger(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        db.logAction(result)
        
    return wrapper