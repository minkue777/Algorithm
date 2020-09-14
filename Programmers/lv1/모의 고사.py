def scoring(answer):
    A1 = [1, 2, 3, 4, 5]
    A2 = [2, 1, 2, 3, 2, 4, 2, 5]
    A3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    A1_Score = 0
    A2_Score = 0
    A3_Score = 0

    for idx, ans in enumerate(answer):
        if ans == A1[idx % 5]:
            A1_Score += 1
        if ans == A2[idx % 8]:
            A2_Score += 1
        if ans == A3[idx % 10]:
            A3_Score += 1

    scores = [A1_Score, A2_Score, A3_Score]
    return scores

def solution(answer):
    scores = scoring(answer)
    max_score = max(scores)
    winner = []
    
    for idx, score in enumerate(scores):
        if score == max_score:
            winner.append(idx+1)
    
    return winner
