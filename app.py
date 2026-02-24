import streamlit as st
from Bio import Entrez, SeqIO
import pandas as pd

st.title("🧬 Genomic Data Visualizer")

accession = st.text_input("Enter NCBI Accession ID", "NM_001301717")

if st.button("Analyze"):
    Entrez.email = "hokole551@gmail.com"
    with Entrez.efetch(db="nucleotide", id=accession, rettype="fasta", retmode="text") as handle:
        record = SeqIO.read(handle, "fasta")
    
    st.subheader(f"Description: {record.description}")
    st.text(f"Sequence Length: {len(record.seq)} bp")
    
    # Simple Nucleotide Count Visualization
    counts = {"A": record.seq.count("A"), "T": record.seq.count("T"), 
              "G": record.seq.count("G"), "C": record.seq.count("C")}
    st.bar_chart(pd.DataFrame(counts.items(), columns=["Base", "Count"]).set_index("Base"))
