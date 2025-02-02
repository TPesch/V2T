import csv

def calculate_wer(reference, hypothesis):
    """Calculate Word Error Rate"""
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    d = [[0 for _ in range(len(hyp_words) + 1)] for _ in range(len(ref_words) + 1)]
    
    for i in range(len(ref_words) + 1):
        d[i][0] = i
    for j in range(len(hyp_words) + 1):
        d[0][j] = j
        
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i-1] == hyp_words[j-1]:
                d[i][j] = d[i-1][j-1]
            else:
                d[i][j] = min(d[i-1][j], d[i][j-1], d[i-1][j-1]) + 1
                
    return d[len(ref_words)][len(hyp_words)] / max(1, len(ref_words))

def save_results_to_csv(filename, reference, transcription, wer):
    """Save evaluation results to a CSV file"""
    with open("Raw_Data/Text/Wer/transcription_results.csv", mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([filename, reference, transcription, f"{wer:.2f}"])

if __name__ == "__main__":
    num_samples = 20  # Number of samples to evaluate
    for i in range(1, num_samples + 1):
        filename = f"Raw_Data/Voices/sample{i}.wav"
        transcript_filename = f"Raw_Data/Text/Predicted/transcription_sample{i}.txt"
        reference_filename = f"Raw_Data/Text/Original/reference{i}.txt"

        with open(transcript_filename, "r", encoding="utf-8") as file:
            transcription = file.read().strip()
        
        with open(reference_filename, "r", encoding="utf-8") as file:
            reference_text = file.read().strip()
        
        print(f"Evaluating {filename}...")
        
        wer_score = calculate_wer(reference_text, transcription)
        print(f"Word Error Rate (WER) for {filename}: {wer_score:.2f}")
        
        # Save results
        save_results_to_csv(filename, reference_text, transcription, wer_score)
        print(f"Results saved to transcription_results.csv")