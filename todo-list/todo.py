import json

def readToDoList():
  with open("todo-list/todo.json", "r") as i:
    JSON_data = json.load(i)
  return JSON_data

def writeToDoList(JSON_data):
  with open("todo-list/todo.json", "w") as data:
    json.dump(JSON_data, data, indent=4)

def updateStatus(JSON_data,foundKey, newProgress):
  for item in JSON_data:
    if(item["taskName"] == foundKey):
      item["Status"] =  newProgress
      break
  return JSON_data

def checkifTaskExists(task, json_data):
  for item in json_data:
    if(item["taskName"].lower() == task.lower()):
      return 1
  return 0

def viewToDoList():
  print(readToDoList())
  return

def addToDoList(task):
  JSON_data = readToDoList()
  isexist = checkifTaskExists(task, JSON_data)
  if(isexist != 1):
    data = {"taskName": task, "Status": "Done"}
    JSON_data.append(data)
    writeToDoList(JSON_data)
    print("provided task is added in the list..!")
  else:
    print("provided task is not present in the json file..!")
  return

def updateToDoList(task):
  JSON_data = readToDoList()
  isexist = checkifTaskExists(task, JSON_data)
  if(isexist == 1):
    progress = input("Enter Task Progress to Update (0: Start, 1: Inprogress, 2: Completed) : ")
    match progress:
      case "0":
        updateStatus(JSON_data, task, "Start")
        writeToDoList(JSON_data)
        print("status: Start updated for task: " + task + "...!")
      case "1":
        updateStatus(JSON_data, task, "Inprogress")
        writeToDoList(JSON_data)
        print("status: Start updated for task: " + task + "...!")
      case "2":
        updateStatus(JSON_data, task, "Completed")
        writeToDoList(JSON_data)
        print("status: Start updated for task: " + task + "...!")
      case _:
        print("invalid status value provided...!")
  else:
    print("provided task is not present in the json file..!")
  return 0


def deleteToDoList(task):
  JSON_data = readToDoList()
  isexist = checkifTaskExists(task, JSON_data)
  if(isexist == 1):
    for item in JSON_data:
      if(item["taskName"].lower() == task.lower()):
        JSON_data.remove(item)
        break
    writeToDoList(JSON_data)
    print("provided task is deleted from the json file..!")
  else:
    print("provided task is not present in the json file..!")
  return

# begining of user input
action = input("please provide action for to do list? (1: view, 2: add, 3: update, 4: delete) ")

if(action == "1"):
  viewToDoList()
elif(action == "2"):
  task = input("Enter Task Name to Add: ")
  addToDoList(task)
elif(action == "3"):
  task = input("Enter Task Name to Update: ")
  updateToDoList(task)
elif(action == "4"):
  task = input("Enter Task Name to Delete: ")
  deleteToDoList(task)
else:
  print("invalid action type. Please provide valid action details...! (1: view, 2: add, 3: update, 4: delete)")
