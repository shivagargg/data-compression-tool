def sort_by_frequency(freq_dict):
    items = list(freq_dict.items())
    items.sort(key=lambda x: x[1], reverse=True)
    return items

def split_items(items):
    total = sum(freq for _, freq in items)
    left_sum = 0
    best_index = 0
    min_diff = float('inf')

    for i in range(len(items)):
        left_sum += items[i][1]
        right_sum = total - left_sum
        diff = abs(left_sum - right_sum)

        if diff < min_diff:
            min_diff = diff
            best_index = i

    left = items[:best_index + 1]
    right = items[best_index + 1:]

    return left, right

def generate_shannon_fano_codes(items, prefix, codes):
    # Base case: only one symbol left
    if len(items) == 1:
        char = items[0][0]
        codes[char] = prefix
        return

    # Split into two balanced groups
    left, right = split_items(items)

    # Recurse on left group (add '0')
    generate_shannon_fano_codes(left, prefix + "0", codes)

    # Recurse on right group (add '1')
    generate_shannon_fano_codes(right, prefix + "1", codes)
    
def decode_shannon_fano(encoded_text, codes):
    # Reverse the code dictionary
    reverse_codes = {}
    for char, code in codes.items():
        reverse_codes[code] = char

    decoded = ""
    buffer = ""

    for bit in encoded_text:
        buffer += bit

        if buffer in reverse_codes:
            decoded += reverse_codes[buffer]
            buffer = ""

    return decoded
