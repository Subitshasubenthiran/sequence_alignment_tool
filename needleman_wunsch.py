from utils import get_score


def needleman_wunsch(seq1, seq2):
    gap = -2

    rows = len(seq1) + 1
    cols = len(seq2) + 1

    score_matrix = [[0 for _ in range(cols)] for _ in range(rows)]
    pointer_matrix = [["" for _ in range(cols)] for _ in range(rows)]

    for i in range(1, rows):
        score_matrix[i][0] = score_matrix[i - 1][0] + gap
        pointer_matrix[i][0] = "U"

    for j in range(1, cols):
        score_matrix[0][j] = score_matrix[0][j - 1] + gap
        pointer_matrix[0][j] = "L"

    for i in range(1, rows):
        for j in range(1, cols):
            diagonal = score_matrix[i - 1][j - 1] + get_score(seq1[i - 1], seq2[j - 1])
            up = score_matrix[i - 1][j] + gap
            left = score_matrix[i][j - 1] + gap

            best_score = max(diagonal, up, left)
            score_matrix[i][j] = best_score

            if best_score == diagonal:
                pointer_matrix[i][j] = "D"
            elif best_score == up:
                pointer_matrix[i][j] = "U"
            else:
                pointer_matrix[i][j] = "L"

    return score_matrix, pointer_matrix

def traceback_global(seq1, seq2, pointer_matrix):
    aligned_seq1 = ""
    aligned_seq2 = ""

    i = len(seq1)
    j = len(seq2)

    while i > 0 or j > 0:
         direction = pointer_matrix[i][j]

         if direction == "D":   
             aligned_seq1 = seq1[i - 1] + aligned_seq1
             aligned_seq2 = seq2[j - 1] + aligned_seq2
             i -= 1
             j -= 1

         elif direction == "U":
            aligned_seq1 = seq1[i - 1] + aligned_seq1
            aligned_seq2 = "-" + aligned_seq2
            i -= 1

         elif direction == "L":
            aligned_seq1 = "-" + aligned_seq1
            aligned_seq2 = seq2[j - 1] + aligned_seq2
            j -= 1

    return aligned_seq1, aligned_seq2
         