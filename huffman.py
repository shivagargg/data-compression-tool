import heapq

class Node:
    # Huffman Tree Node Constructor
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
    # Define less-than for priority queue
    def __lt__(self, other):
        return self.freq < other.freq
# merging nodes to build the hoffman tree
def build_huffman_tree(freq_dict):
    heap = []
    # Step 1: create nodes and push into heap
    for ch, freq in freq_dict.items():
        node = Node(ch, freq)
        heapq.heappush(heap, node)

    # Step 2: merge nodes until one remains
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)

        merged = Node(None, node1.freq + node2.freq)
        merged.left = node1
        merged.right = node2

        heapq.heappush(heap, merged)
    # Step 3: return root
    return heap[0]

# Generate Huffman Codes from the tree
def generate_codes(node, current_code, codes):
    if node is None:
        return

    # If this is a leaf node (actual character)
    if node.char is not None:
        codes[node.char] = current_code
        return

    # Traverse left (add '0')
    generate_codes(node.left, current_code + "0", codes)

    # Traverse right (add '1')
    generate_codes(node.right, current_code + "1", codes)
def encode_text(text, codes):
    encoded = ""

    for ch in text:
        encoded += codes[ch]

    return encoded
def calculate_compression_ratio(text, encoded_text):
    original_size = len(text) * 8
    compressed_size = len(encoded_text)
    return compressed_size / original_size
    
def decode_text(encoded_text, root):
    decoded = ""
    current = root

    for bit in encoded_text:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        # If leaf node
        if current.char is not None:
            decoded += current.char
            current = root

    return decoded
def save_huff_file(filename, freq_dict, encoded_text):
    with open(filename, 'w') as f:
        f.write("---HUFFMAN---\n")
        f.write("FREQ\n")
        f.write(str(freq_dict) + "\n")
        f.write("DATA\n")
        f.write(encoded_text)
def load_huff_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()

    # Basic validation
    if lines[0].strip() != "---HUFFMAN---":
        raise ValueError("Not a valid .huff file")

    freq_line_index = lines.index("FREQ\n") + 1
    data_line_index = lines.index("DATA\n") + 1

    freq_dict = eval(lines[freq_line_index].strip())
    encoded_text = lines[data_line_index].strip()

    return freq_dict, encoded_text
def calculate_compression_ratio(original_text, encoded_bits):
    original_bits = len(original_text) * 8
    compressed_bits = len(encoded_bits)
    return compressed_bits / original_bits
