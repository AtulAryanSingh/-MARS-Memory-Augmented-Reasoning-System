from fastapi import FastAPI
from pydantic import BaseModel

# ✅ NEW GOVERNANCE MEMORY
from memory import (
    add_memory,
    read_memory,
    delete_memory,
    update_memory
)

# (Optional: keep your graph + reasoning if already working)
from graph_memory import add_relation, get_graph
from meaning import extract_relations
from reasoning import answer_query


app = FastAPI()


# ---------------- REQUEST MODEL ----------------
class ChatRequest(BaseModel):
    user: str
    message: str


# ---------------- ROOT ----------------
@app.get("/")
def home():
    return {"status": "MARS GOVERNANCE ACTIVE"}


# ---------------- CHAT (WRITE + UPDATE MEMORY) ----------------
@app.post("/chat")
def chat(req: ChatRequest):
    user = req.user
    message = req.message

    # 🔥 GOVERNANCE: update handles conflicts automatically
    memory = update_memory(user, message)

    # (Optional) update graph
    relations = extract_relations(user, message)
    for a, b in relations:
        add_relation(a, b)

    return {
        "user": user,
        "stored_memory": memory,
        "graph": get_graph(),
        "system": "MARS GOVERNANCE ACTIVE"
    }


# ---------------- READ MEMORY ----------------
@app.get("/memory/{user}")
def get_memory_endpoint(user: str):
    return {
        "user": user,
        "memory": read_memory(user)
    }


# ---------------- DELETE MEMORY ----------------
@app.delete("/memory")
def delete_memory_endpoint(req: ChatRequest):
    return delete_memory(req.user, req.message)


# ---------------- REASONING ----------------
@app.post("/reason")
def reason(req: ChatRequest):
    result = answer_query(req.message)

    return {
        "query": req.message,
        "reasoning": result,
        "system": "GRAPH REASONING ACTIVE"
    }


# ---------------- DEBUG GRAPH ----------------
@app.get("/debug")
def debug():
    return get_graph()
