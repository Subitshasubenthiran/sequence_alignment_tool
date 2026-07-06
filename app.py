import streamlit as st

from needleman_wunsch import needleman_wunsch, traceback_global
from utils import get_match_line, calculate_statistics

st.set_page_config(page_title="Sequence Alignment Tool")

st.title("Sequence Alignment Tool")

st.write("Needleman-Wunsch and Smith-Waterman algorithms")

seq1_file = st.file_uploader("Upload first FASTA file", type=["fasta", "fa", "txt"])
seq2_file = st.file_uploader("Upload second FASTA file", type=["fasta", "fa", "txt"])

if seq1_file is not None and seq2_file is not None:
    seq1 = ""
    seq2 = ""

    for line in seq1_file:
        line = line.decode("utf-8").strip()
        if not line.startswith(">"):
            seq1 += line

    for line in seq2_file:
        line = line.decode("utf-8").strip()
        if not line.startswith(">"):
            seq2 += line

    st.success("Sequences loaded successfully!")

    st.write("Sequence 1:", seq1)
    st.write("Sequence 2:", seq2)

    if st.button("Align Sequences"):
        nw_matrix, nw_pointer = needleman_wunsch(seq1, seq2)

        aligned_seq1, aligned_seq2 = traceback_global(seq1, seq2, nw_pointer)

        match_line = get_match_line(aligned_seq1, aligned_seq2)

        matches, mismatches, gaps, identity = calculate_statistics(aligned_seq1, aligned_seq2)

        st.subheader("Global Alignment")
        st.text(aligned_seq1)
        st.text(match_line)
        st.text(aligned_seq2)

        st.write("Alignment Score:", nw_matrix[-1][-1])
        st.write("Matches:", matches)
        st.write("Mismatches:", mismatches)
        st.write("Gaps:", gaps)
        st.write("Identity:", round(identity, 2), "%")

        result_text = f"""
Sequence Alignment Result
=========================

Global Alignment
{aligned_seq1}
{match_line}
{aligned_seq2}

Alignment Score: {nw_matrix[-1][-1]}

Alignment Statistics
Matches: {matches}
Mismatches: {mismatches}
Gaps: {gaps}
Identity: {round(identity, 2)}%
"""

        st.download_button(
           label="Download Result",
           data=result_text,
           file_name="alignment_result.txt",
           mime="text/plain"
        )
    