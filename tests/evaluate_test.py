def calculate_wer(reference, hypothesis):
    """Calculate Word Error Rate (WER)"""
    ref_words = reference.split()
    hyp_words = hypothesis.split()
    
    # Create a matrix for dynamic programming
    d = [[0 for _ in range(len(hyp_words) + 1)] for _ in range(len(ref_words) + 1)]
    
    # Initialize matrix
    for i in range(len(ref_words) + 1):
        d[i][0] = i
    for j in range(len(hyp_words) + 1):
        d[0][j] = j
        
    # Fill the matrix
    for i in range(1, len(ref_words) + 1):
        for j in range(1, len(hyp_words) + 1):
            if ref_words[i - 1] == hyp_words[j - 1]:
                d[i][j] = d[i - 1][j - 1]  # No change
            else:
                d[i][j] = min(d[i - 1][j], d[i][j - 1], d[i - 1][j - 1]) + 1  # Edit needed
                
    # Compute WER
    wer_score = d[len(ref_words)][len(hyp_words)] / max(1, len(ref_words))
    return wer_score

if __name__ == "__main__":
    # Load reference text
    reference_text = "I will find you and I will kill you. I will find you"

    # Load transcribed text from file
    with open("tests/test_outputs/transcription.txt", "r", encoding="utf-8") as file:
        transcribed_text = file.read().strip()

    # Calculate WER
    wer_score = calculate_wer(reference_text, transcribed_text)

    print(f"Transcribed Text: {transcribed_text}")
    print(f"Reference Text: {reference_text}")
    print(f"Word Error Rate (WER): {wer_score:.2f}")
