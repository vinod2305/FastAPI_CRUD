from fastapi import FastAPI
app = FastAPI()


@app.get("/", tags=['ROOT'])
async def root() -> dict:
    return {"Ping": "Pong"}


@app.get('/todo', tags=['todos'])
async def get_todo() -> dict:
    return {"data": todos}

@app.post('/todo', tags=['todos'])
async def add_todo(todo:dict) -> dict:
    todos.append(todo)
    return {
        "data" : "A todo has been added"
    }

@app.put('/todo/{id}', tags=['todos'])
async def update_todo(id:int, body: dict) -> dict:
    for todo in todos:
        if int(todo['id']) == id:
            todo['Activity'] = body['Activity']
            return {
                "data": f"Todo with id {id} has been updated"
            }
        return {
            "data":f"Todo with this id number {id} was not found!"
        }

@app.delete("/todo/{id}", tags=["todos"])
async def delete_todo(id: int) -> dict:
    for todo in todos:
        if int(todo["id"]) == id:
            todos.remove(todo)
            return {
                "data" : f"todo with id {id} has been deleted"
            }
        return {
            "data": f"todo with this id number {id} was not found"
        }


todos = [
    {
        "id": "1",
        "Activity": "Jogging for 2 hours at 7:00 AM."
    },
    {
        "id": "2",
        "Activity": "Writing 3 pages of my new book at 2:00 PM."
    }
]