def longest_repetition(dna_sequence):
    max_length = 0
    current_length = 0
    previous_char = ''

    for char in dna_sequence:
        if char == previous_char:
            current_length += 1
        else:
            current_length = 1
            previous_char = char
        max_length = max(max_length, current_length)
    
    return max_length
dna_sequence = input().strip()
print(longest_repetition(dna_sequence))