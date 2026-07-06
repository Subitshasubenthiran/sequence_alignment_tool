def get_score(a,b):
    if a==b:
        return 1
    else:
        return -1
    
def print_matrix(matrix):
    for row in matrix:
        print(row)

def get_match_line(aligned_seq1, aligned_seq2):
    match_line = ""
    
    for a, b in zip(aligned_seq1, aligned_seq2):
        if a == b:
            match_line += "|"
        else:
            match_line += " "
    
    return match_line

def read_fasta(filename):
    sequence = ""

    with open(filename,'r') as file:
        for line in file:
            line = line.strip()

            if line.startswith(">"):
                continue

            sequence += line

    return sequence

def calculate_statistics(aligned_seq1, aligned_seq2):
    matches = 0
    mismatches = 0
    gaps = 0

    for a, b in zip(aligned_seq1, aligned_seq2):
        if a == "-" or b == "-":
            gaps += 1
        elif a == b:
            matches += 1
        else:
            mismatches += 1

    total_length = len(aligned_seq1)
    identify = (matches / total_length) * 100 if total_length > 0 else 0

    return matches, mismatches, gaps, identify

def save_alignment_result(filename, aligned_seq1, match_line, aligned_seq2, score, matches, mismatches, gaps, identity):
    with open(filename, "w") as file:
        file.write("Sequence Alignment Result\n")
        file.write("=========================\n\n")

        file.write("Global Alignment\n")
        file.write(aligned_seq1 + "\n")
        file.write(match_line + "\n")
        file.write(aligned_seq2 + "\n\n")

        file.write("Alignment Score: " + str(score) + "\n\n")

        file.write("Alignment Statistics\n")
        file.write("Matches: " + str(matches) + "\n")
        file.write("Mismatches: " + str(mismatches) + "\n")
        file.write("Gaps: " + str(gaps) + "\n")
        file.write("Identity: " + str(round(identity, 2)) + "%\n")