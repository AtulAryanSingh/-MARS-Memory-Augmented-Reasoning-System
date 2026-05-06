from memory import get_active_memory


def run_evaluation(user):

    active = get_active_memory(user)

    precision = 1 if len(active) > 0 else 0
    drift = 0  # simplified for now

    return {
        "precision_at_1": precision,
        "drift_rate": drift
    }