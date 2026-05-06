# 🧠 MARS — Memory Augmented Reasoning System

MARS is a **deterministic LLM memory + governance engine** that stores, updates, and reasons over user preferences with **conflict resolution, provenance, and evaluation metrics**.

This project focuses on solving a real problem in AI systems:

> ❗ LLMs forget, contradict themselves, and drift over time.

MARS addresses this by introducing **structured memory + reasoning + evaluation**, instead of relying on raw prompt history.

---

# 🚀 Features

### 🧠 Memory System
- Stores structured memory objects (`MemoryItem`)
- Tracks:
  - text
  - timestamp
  - importance
  - confidence
  - source + reason
- Supports:
  - memory updates
  - reinforcement
  - decay

---

### ⚖️ Governance Layer
- Conflict detection (e.g. "like" vs "don't like")
- Automatic override of outdated beliefs
- Confidence adjustment on contradictions
- Memory activation / deactivation

---

### 🔗 Graph Memory
- Extracts relationships from user input
- Builds entity graph (user → relation → object)
- Enables future multi-hop reasoning

---

### 🧠 Reasoning Engine
- Deterministic (not LLM guessing)
- Entity-based preference resolution
- Handles:
  - multiple preferences
  - noise inputs
  - conflict updates

---

### 🧪 Evaluation Harness (KEY DIFFERENTIATOR)
- Custom test dataset with multi-step conversations
- Automated test runner
- Metrics:
  - ✅ Precision@1
  - ⚠️ Drift detection
- Current accuracy:

```bash
TOTAL: 7
PASSED: 6
ACCURACY: 0.857
