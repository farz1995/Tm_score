import os
from tmscore import TMscoring
import csv

def calculate_tm_rmsd(real_dir, pred_dir, output_csv):
    results = []
    tm_scores = []
    rmsd_values = []

    # Iterate over the predicted files
    for pred_file in os.listdir(pred_dir):
        # Remove 'structure_' prefix to find corresponding real structure
        real_filename = pred_file.replace('structure_', '')
        real_file = os.path.join(real_dir, real_filename)
        pred_file = os.path.join(pred_dir, pred_file)

        # Ensure the corresponding real structure exists
        if not os.path.isfile(real_file):
            print(f"Real structure for {pred_file} not found. Skipping.")
            continue

        # Calculate TM-score and RMSD
        alignment = TMscoring(real_file, pred_file)
        alignment.optimise()

        tm_score = alignment.tmscore(**alignment.get_current_values())
        rmsd_value = alignment.rmsd(**alignment.get_current_values())

        # Append to results
        results.append({
            "id_real": real_filename,
            "id_pred": pred_file,
            "tm-score": tm_score,
            "rmsd": rmsd_value
        })

        tm_scores.append(tm_score)
        rmsd_values.append(rmsd_value)

        # print(f"Processed: {real_filename} and {pred_file}")
        # print(f"TM-score: {tm_score}")
        # print(f"RMSD: {rmsd_value}")

    # Calculate averages
    avg_tm_score = sum(tm_scores) / len(tm_scores) if tm_scores else 0
    avg_rmsd = sum(rmsd_values) / len(rmsd_values) if rmsd_values else 0

    # Save results to CSV
    with open(output_csv, mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["id_real", "id_pred", "tm-score", "rmsd"])
        writer.writeheader()
        writer.writerows(results)

    # Print averages
    print("\nSummary:")
    print(f"Average TM-score: {avg_tm_score}")
    print(f"Average RMSD: {avg_rmsd}")

    return avg_tm_score, avg_rmsd

if __name__ == "__main__":
    real_dir = "../../../cameo/raw_targets-1-year.public/real_structures/"
    pred_dir = "../../perplexity-11_62/perplexity-11_62/2025-01-21__17-13-30/pdb/structures/"
    output_csv='result.csv'

    calculate_tm_rmsd(real_dir, pred_dir, output_csv)
