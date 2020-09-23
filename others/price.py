import time
import random
from collections import deque
import copy

def solution(prices):
    answer = []
    N = len(prices)
    d = deque(prices)
    while True:
        count = 0
        present = d.popleft()
        if not d:
            answer.append(0)
            break
        for q_value in d:
            count += 1
            if q_value < present:
                break
        answer.append(count)
    return answer

