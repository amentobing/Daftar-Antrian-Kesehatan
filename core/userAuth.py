import json


def checkAccountFile(email, password):
    userAuth = open('userAuth.json', "r")
    data = json.load(userAuth)
    userAuth.close()

    result = False
    for i in range(len(data)):
        if data[i]['email'] == email and data[i]['password'] == password:
            result = True

    if not result:
        print(f"Wrong Email/Password ({email})")

    return result


def checkAccountEmail(email):
    userAuth = open('userAuth.json', "r")
    data = json.load(userAuth)
    userAuth.close()

    result = False
    for i in range(len(data)):
        if data[i]['email'] == email:
            result = True

    return result


def addAccount(email, password, name):
    try:
        userAuth = open('userAuth.json', "r")
        data = json.load(userAuth)
        userAuth.close()

        result = False
        data_result = {}
        for i in range(len(data)-1):
            if data[i]['password'] == password:
                data.remove(data[i])

        data.append({"email": email, "password": password, "name": name})

        userAuth = open('userAuth.json', "w")
        userAuth.write(f"{json.dumps(data, indent=4)}")

        print(f"Create Account: {email}")
        return True
    except:
        return False
