
from dotenv import load_dotenv
load_dotenv()
from fastapi import FastAPI, WebSocket
from models import StateTree, GridWidget, TextWidget
from chain import call_chain

app = FastAPI()

connection = None


state = StateTree(
    root=GridWidget(
        id=0,
        columns=2,
        rows=1,
        widgets=[
            GridWidget(
                id=1,
                columns=1,
                rows=2,
                widgets=[
                    TextWidget(
                        id=2,
                        text="ToDo List"
                    ),
                    TextWidget(
                        id=3,
                        text="Do the dishes"
                    ),
                ]
            ),
            GridWidget(
                id=4,
                columns=1,
                rows=2,
                widgets=[
                    TextWidget(
                        id=5,
                        text="Done List"
                    ),
                    TextWidget(
                        id=6,
                        text="Do Laundry"
                    )
                ]
            
            )
        ]
    )
)

@app.get("/", response_model=StateTree)
async def read_root():
    return state

@app.put("/", response_model=StateTree)
async def update_state(new_state: StateTree):
    state.root = new_state.root
    if connection:
        await connection.send_json(state.dict())
    return state


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    global connection
    connection = websocket
    await websocket.accept()
    while True:
        await websocket.send_json(state.dict())
        data = await websocket.receive_json()
        print("Data received:")
        print(data)
        new_state = call_chain(data["message"], state)
        state.root = StateTree.parse_obj(new_state).root

