# TMscoring: Protein Structure Comparison Tool

TMscoring is a Python-based tool for comparing protein structures by calculating the **TM-score** and **RMSD** (Root Mean Square Deviation) values. It also provides functionalities for aligning protein structures and outputting aligned PDB files.
the code has been developed by following [TM_SCORE](https://zhanglab.comp.nus.edu.sg/TM-score/)  in Zhanglab.
## Features

- **Calculate **TM-score****: A measure of structural similarity between two protein structures.
- **Calculate **RMSD****: A metric for the deviation between two aligned protein structures.
- **Batch Processing**: Process multiple structure files in specified directories.
- **CSV Output**: Save results (TM-score and RMSD) to a CSV file for easy analysis.
- **Summary Statistics**: Compute average TM-score and RMSD across all processed structures.



## Requirements

- Python 3.7 or higher
- Required libraries:
  - `numpy`
  - `scipy`
  - `biopython`

To install the required packages, use:
```bash
pip install -r requirements.txt
```
## Installation
Clone the Repository:

```bash
git clone https://github.com/farz1995/Tm_score.git
cd TM_score

python main.py
``` 
## Usage 
Example: Batch Processing with main.py
This example compares protein structures in batch mode. The real structures are stored in ```real_structures/```, and the predicted structures are in ```predicted_structures/```.

Directory Structure
```real_structures/```: Contains real protein structure files (e.g., 1a1b.pdb).
```predicted_structures/```: Contains predicted protein structure files prefixed with structure_ (e.g., structure_1a1b.pdb).

## Expected Output
CSV File: A file named result.csv containing the TM-score and RMSD for each protein pair.
Summary Statistics: The average TM-score and RMSD are printed in the terminal.

## Customization
You can edit the paths for real and predicted structure directories in main.py:
```
real_dir = "path/to/real_structures/"
pred_dir = "path/to/predicted_structures/"
output_csv = "result.csv"
```