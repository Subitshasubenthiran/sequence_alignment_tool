from utils import get_score

def smith_waterman(seq1, seq2):
    gap = -2

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    max_score = 0
    max_position = (0, 0)

    for i in range(1, rows):
        for j in range(1, cols):
            diagonal = matrix[i - 1][j - 1] + get_score(seq1[i - 1], seq2[j - 1])
            up = matrix[i - 1][j] + gap
            left = matrix[i][j - 1] + gap

            matrix[i][j] = max(0, diagonal, up, left)

            if matrix[i][j] > max_score:
                max_score = matrix[i][j]
                max_position = (i, j)

    return matrix, max_score, max_position
