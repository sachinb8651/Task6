Value = {
    "student": [
        {"name":"Sachin","scores":{"Python":85,"math": 90}},
        {"name":"Abhishek","scores":{"Python":78,"science":88}},
        {"name":"Raj","scores":{"python":58,"english":38}}
    ],
    "subjects":{"python","math","science","english"}
}

def get_path(d, path):
    keys=path.split(".")
    curr=d
    for key in keys[:-1]:
        if isinstance(curr, list):
            key=int(key)
        curr=curr[key]
    return curr,keys[-1]

def get_value(d,path):
    point, key =get_path(d, path)
    if isinstance(point, list):
        key=int(key)
    return point[key]

def set_value(d,path,value):
    point, key=get_path(d, path)
    if isinstance(point, list):
        key=int(key)
    point[key]=value
    return f"Updated-- Set {path} = {value}"

def del_value(d, path):
    point, key = get_path(d, path)
    if isinstance(point, list):
        key = int(key)
        point.pop(key)
    else:
        del point[key]
    return f"Deleted-- {path}"

def list_keys(d, path=""):
    p = get_value(d, path) if path else d
    if isinstance(p, dict):
        return list(p.keys())
    elif isinstance(p, list):
        return list(range(len(p)))
    elif isinstance(p, set):
        return list(p)
    else:
        return "Not iterable"

def main():
    print("Give the dot path syntax to fetch/modify data")
    while True:
        user_input = input("Enter: ").strip()
        if user_input.lower() in ("exit", "quit"):
            break
        parts = user_input.split(" ")
        if not parts:
            continue
        action = parts[0].lower()
        try:
            if action =="get":
                print(get_value(Value, parts[1]))

            elif action=="set":
                print(set_value(Value, parts[1], parts[2]))

            elif action=="del":
                print(del_value(Value, parts[1]))

            elif action=="list":
                path=parts[1]
                print(list_keys(Value, path))
            else:
                print("Invalid command") 
        except Exception:
            print(" Invalid path..Please provide the valid path .")
if __name__ == "__main__":
    main()

