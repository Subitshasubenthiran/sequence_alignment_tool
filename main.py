from needleman_wunsch import needleman_wunsch, traceback_global
from smith_waterman import smith_waterman
from utils import print_matrix , get_match_line, read_fasta,calculate_statistics, save_alignment_result

seq1 = read_fasta("human.fasta")
seq2 = read_fasta("mouse.fasta")

print("\n---Needleman-Wunsch Algorithm---")
nw_matrix , nw_pointers = needleman_wunsch(seq1, seq2)
print_matrix(nw_matrix)
print("Global Alignment Score:", nw_matrix[-1][-1])

aligned_seq1, aligned_seq2 = traceback_global(seq1, seq2, nw_pointers)
print("Global Alignment")
print(aligned_seq1)
print(get_match_line(aligned_seq1, aligned_seq2))
print(aligned_seq2)
matches, mismatches, gaps, identity = calculate_statistics(aligned_seq1, aligned_seq2)

print("\nAlignment Statistics")
print("Matches:", matches)
print("Mismatches:", mismatches)
print("Gaps:", gaps)
print("Identity:", round(identity, 2), "%")
match_line = get_match_line(aligned_seq1, aligned_seq2)

save_alignment_result(
    "alignment_result.txt",
    aligned_seq1,
    match_line,
    aligned_seq2,
    nw_matrix[-1][-1],
    matches,
    mismatches,
    gaps,
    identity
)

print("\nResult saved to alignment_result.txt")

print("\n---Smith-Waterman Algorithm---")
sw_matrix,max_score, max_position = smith_waterman(seq1, seq2)
print_matrix(sw_matrix)
print("Local Alignment Score:", max_score)
print("Best Local Alignment Position:", max_position)
