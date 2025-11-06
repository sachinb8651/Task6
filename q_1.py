Value = {
    "student": [
        {"name":"Sachin","scores":{"Python":85,"math": 90}},
        {"name":"Abhishek","scores":{"Python":78,"science":88}},
        {"name":"Raj","scores":{"python":58,"english":38}}
    ],
    "subjects":{"python","math","science","english"}
}

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
        # print(f"action---{action}")
        path = parts[1] if len(parts) > 1 else ""
        # print(f"path-----{path}")
        try:
            keys = path.split(".")
            curr = Value
            for key in keys[:-1]:
                if isinstance(curr, list):
                    key = int(key)
                curr = curr[key]
            last_key = keys[-1]
            if isinstance(curr, list):
                last_key = int(last_key)
            
            if action == "get":
                print(curr[last_key])
            
            elif action == "set":
                value = parts[2]
                if value.isdigit():
                    value = int(value)
                curr[last_key] = value
                print(f"Updated-- Set {path} = {value}")
            
            elif action == "del":
                if isinstance(curr, list):
                    curr.pop(last_key)
                else:
                    del curr[last_key]
                print(f"Deleted-- {path}")
            
            elif action == "list":
                target = curr[last_key] if path else Value
                if isinstance(target, dict):
                    print(list(target.keys()))
                elif isinstance(target, list):
                    print(list(range(len(target))))
                elif isinstance(target, set):
                    print(list(target))
                else:
                    print("Not iterable")
            
            else:
                print("Invalid command")
        
        except Exception:
            print("Invalid path..Please provide a valid path.")

main()
