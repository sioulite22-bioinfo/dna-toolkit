# DNA Toolkit 🧬

A lightweight bioinformatics toolkit written in **pure Python** — no external libraries — that walks through the central dogma of molecular biology, from a raw DNA sequence to its translated protein.

Built from scratch as a learning project to understand what happens *under the hood* of the tools bioinformaticians use every day.

---

## Features

Given a DNA sequence, the toolkit computes:

- **Nucleotide counts** — tally of A, T, G, and C
- **Sequence length**
- **GC content** — percentage of G and C bases
- **Transcription** — DNA → RNA (T → U)
- **Complement** — base-by-base complementary strand
- **Reverse complement** — the complementary strand read 5'→3'
- **Translation** — DNA → protein, using the full 64-codon genetic code
- **Full amino acid names** — expands single-letter codes (e.g. `M → Methionine`) for readability

---

## Example

Input sequence:

```
ATGCGGTACGTTAGCACGT
```

Output:

```
A: 4
T: 5
G: 6
C: 4
Length: 19
GC content: 52.63 %
RNA: AUGCGGUACGUUAGCACGU
complement: TACGCCATGCAATCGTGCA
Reverse complement: ACGTGCTAACGTACCGCAT
Protein: MRYVST
Protein (full names):
   M -> Methionine
   R -> Arginine
   Y -> Tyrosine
   V -> Valine
   S -> Serine
   T -> Threonine
```

---

## Usage

Clone the repository and run the script:

```bash
git clone https://github.com/<your-username>/dna-toolkit.git
cd dna-toolkit
python toolkit.py
```

To analyze your own sequence, edit the `dna` variable at the top of `toolkit.py`.

**Requirements:** Python 3.x. No external packages needed.

---

## Concepts practiced

This project was a hands-on way to learn core Python fundamentals in a biological context:

| Concept | Where it's used |
|---|---|
| Strings & slicing | Reading codons (`dna[i:i+3]`), reversing (`[::-1]`) |
| Dictionaries | Complement map, 64-codon table, amino acid names |
| Loops (`for`, `range`) | Walking the sequence, stepping by 3 for codons |
| Methods vs functions | `.count()`, `.replace()` vs `len()`, `range()` |
| Debugging | Reading and fixing Python error messages |

---

## Roadmap

Planned improvements as the learning continues:

- [ ] Refactor each operation into reusable **functions**
- [ ] Add **input validation** for invalid characters
- [ ] Read sequences from **FASTA files** instead of hardcoding
- [ ] Support multi-sequence input

---

## About

Built by an early-career computational biologist learning Python one biological problem at a time. Feedback and suggestions welcome.
