from dao import db_ucheck, db_insert, user_credentials, update_password


def check_user(a1, a2): # check_use(data['eid'], data['userid'])
    res = db_ucheck(a1, a2)
    return res

def add_user(*args):
    res = db_insert(*args)
    return res

def check_user_credential(e_id, e_pass):
    resp = user_credentials(e_id, e_pass)
    return resp

def update_user_password(e_id, e_new_pass):
    resp = update_password(e_id, e_new_pass)
    return resp