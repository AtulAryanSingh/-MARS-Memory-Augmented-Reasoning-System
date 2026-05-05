from fastapi import FastAPI
from pydantic import BaseModel

from memory import get_memory, save_memory, apply_decay
from models import MemoryItem
from meaning import compute_importance, extract_relations
from graph_memory import add_relation, get_graph
from reasoning import answer_query

app = FastAPI()


class ChatRequest(BaseModel):
    user: str
    message: str


@app.get("/")
def home():
    return {"status": "MARS SYSTEM ACTIVE"}


# ---------------- CHAT ----------------
@app.post("/chat")
def chat(req: ChatRequest):

    memory = get_memory(req.user)

    importance = compute_importance(req.message)

    item = MemoryItem(
        text=req.message,
        importance=importance,
        user=req.user
    )

    save_memory(req.user, item)
    apply_decay(req.user)

    relations = extract_relations(req.user, req.message)

    for a, b in relations:
        add_relation(a, b)

    return {
        "user": req.user,
        "input": req.message,
        "importance": importance,
        "graph": get_graph(),
        "system": "GRAPH MEMORY ACTIVE"
    }


# ---------------- REASON ----------------
@app.post("/reason")
def reason(req: ChatRequest):

    result = answer_query(req.message)

    return {
        "query": req.message,
        "reasoning": result,
        "system": "GRAPH REASONING ACTIVE"
    }


# ---------------- DEBUG (IMPORTANT) ----------------
@app.get("/debug")
def debug():
    return get_graph()