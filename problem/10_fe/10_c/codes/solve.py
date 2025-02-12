import math
from decimal import Decimal

def calc_cosine_similarity(vector1, vector2):
    temp = 0
    numerator = 0

    for i in range(len(vector1)):
        numerator = numerator + vector1[i] * vector2[i]
    
    for i in range(len(vector1)):
        temp = temp + vector1[i]**2
    denominator = math.sqrt(temp)

    temp = 0
    for i in range(len(vector2)):
        temp = temp + vector2[i]**2
    denominator = denominator * math.sqrt(temp)

    similarity = float(numerator) / denominator
    return similarity


if __name__ == "__main__":
    N = int(input())
    A = list(map(Decimal, input().split()))
    B = list(map(Decimal, input().split()))
    print(calc_cosine_similarity(A, B))