from test_dataset import TEST_CASES
from models import MemoryItem
from memory import update_memory, reset_memory
from meaning import compute_importance
from reasoning import answer_query


def normalize(x):
    return x.lower().strip()


def run_test_case(test):

    user = "test_user"

    # RESET memory before each test
    reset_memory(user)

    # -------- APPLY STEPS --------
    for step in test["steps"]:
        importance = compute_importance(step)

        item = MemoryItem(
            text=step,
            importance=importance,
            user=user
        )

        update_memory(user, item)

    # -------- RUN QUERY THROUGH REASONING --------
    answer = answer_query(test["query"], user)

    # -------- STABILITY TEST --------
    if "repeat" in test:
        answers = []

        for _ in range(test["repeat"]):
            ans = answer_query(test["query"], user)
            answers.append(ans)

        drift = len(set(answers)) > 1

        return not drift, f"drift={drift}"

    # -------- NORMAL CHECK (FIXED) --------
    return normalize(answer) == normalize(test["expected"]), answer


def run_all_tests():

    total = len(TEST_CASES)
    passed = 0

    for test in TEST_CASES:

        ok, output = run_test_case(test)

        if ok:
            passed += 1
            print(f"✅ {test['name']}")
        else:
            print(f"❌ {test['name']} → got: {output}")

    accuracy = passed / total

    print("\n===================")
    print(f"TOTAL: {total}")
    print(f"PASSED: {passed}")
    print(f"ACCURACY: {round(accuracy, 3)}")


if __name__ == "__main__":
    run_all_tests()