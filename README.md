# Genomic Data Visualizer

This project is a simple web application built with Streamlit and Biopython for visualizing genomic data retrieved from NCBI given an accession number.

## Features

- Enter an NCBI nucleotide accession ID and retrieve its FASTA sequence.
- View description and sequence length.
- Visualize nucleotide composition in a bar chart.

## Installation

Install the required dependencies:

```bash
pip install biopython streamlit pandas
```

## Usage

Start the app with:

```bash
streamlit run app.py
```

Then enter an NCBI accession ID in the app UI and click "Analyze" to view results.

## Requirements

- Python 3.7+
- biopython
- streamlit
- pandas

## License

MIT License