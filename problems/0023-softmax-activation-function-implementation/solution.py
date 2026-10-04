import math

def softmax(scores: list[float]) -> list[float]:
    # Your code here
    if not scores:
        return []
    exp_scores = [math.exp(x - max(scores)) for x in scores]
    sum_exp_scores = sum(exp_scores)
    return [score / sum_exp_scores for score in exp_scores]