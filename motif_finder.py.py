# Function to calculate mismatches between two strings
def hamming_distance(s1, s2):
    return sum(1 for a, b in zip(s1, s2) if a != b)

# Function to find pattern matches with mismatches allowed
def find_approx_matches(sequence, pattern, max_mismatches):
    matches = []
    k = len(pattern)
    for i in range(len(sequence) - k + 1):
        window = sequence[i:i+k]
        if hamming_distance(window, pattern) <= max_mismatches:
            matches.append((i, window))
    return matches

# Example use
dna = "ATCGTACGTACGTTACGT"
pattern = "TAC"
mismatches_allowed = 1

results = find_approx_matches(dna, pattern, mismatches_allowed)

print("Matches found:")
for pos, match in results:
    print(f"Position {pos}: {match}")
