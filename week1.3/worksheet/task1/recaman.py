# Worksheet 1.3: Task 1

L = int(input("Length of sequence: ")) # Only one input


# Start the sequence with the first term
sequence = [0]

# Generate the remaining terms
for k in range(1, L):

    # Try subtracting k from the previous term
    candidate = sequence[-1] - k

    # Use the subtraction result if:
    # It is positive
    # It is not already in the sequence
    if candidate > 0 and candidate not in sequence:
        sequence.append(candidate)

    # Otherwise use addition
    else:
        sequence.append(sequence[-1] + k)

# Print each term of the sequence on a new line
[print(item) for item in sequence]