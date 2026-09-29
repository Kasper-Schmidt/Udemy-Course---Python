def password_controller(custompassword):
    if len(custompassword) >= 8:
        return True
    else:
        return False


print(password_controller("ThisIsATest"))