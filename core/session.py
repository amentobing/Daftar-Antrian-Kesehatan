import json


def checkSessionFile(id, email):
    sessions = open('session.json', "r")
    data = json.load(sessions)
    sessions.close()

    result = False
    for i in range(len(data)):
        if data[i]['id'] == id and data[i]['email'] == email:
            result = True

    return result


def addSession(id, email):
    try:
        sessions = open('session.json', "r")
        data = json.load(sessions)
        sessions.close()

        result = False
        data_result = {}
        for i in range(len(data)):
            if data[i]['email'] == email:
                data.remove(data[i])

        data.append({"id": id, "email": email})

        sessions = open('session.json', "w")
        sessions.write(f"{json.dumps(data, indent=4)}")

        print(f"Create Session: {id}, {email}")
        return True
    except:
        print("error session")
        return False
