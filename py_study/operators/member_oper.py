valid_users=['db_user','ora_admin','db_admin']
random_user='db_user'
if random_user not in valid_users:
    print("Yes , this user has full permissions")
else:
    print("this user doesn't have permissions")
    
