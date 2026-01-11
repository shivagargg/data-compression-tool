# from utils import get_frequencies
# from huffman import (
#     build_huffman_tree,
#     generate_codes,
#     encode_text,
#     calculate_compression_ratio,
#     decode_text
# )

# text = "aaabbc"

# freq = get_frequencies(text)
# root = build_huffman_tree(freq)

# codes = {}
# generate_codes(root, "", codes)

# encoded = encode_text(text, codes)
# ratio = calculate_compression_ratio(text, encoded)

# print("Text:", text)
# print("Codes:", codes)
# print("Encoded:", encoded)
# print("Original size (bits):", len(text) * 8)
# print("Compressed size (bits):", len(encoded))
# print("Compression ratio:", ratio)
# decoded = decode_text(encoded, root)
# print("Decoded :", decoded)

# SHANNON-FANO IMPLEMENTATION IS DEPRECATED AND REMOVED
# from utils import get_frequencies
# from shannon_fano import (
#     sort_by_frequency,
#     generate_shannon_fano_codes,
#     decode_shannon_fano
# )
# from huffman import encode_text

# text = "aaabbc"

# freq = get_frequencies(text)
# items = sort_by_frequency(freq)

# codes = {}
# generate_shannon_fano_codes(items, "", codes)

# encoded = encode_text(text, codes)
# decoded = decode_shannon_fano(encoded, codes)

# print("Original:", text)
# print("Codes   :", codes)
# print("Encoded :", encoded)
# print("Decoded :", decoded)


# FINAL TESTING SCRIPT
from utils import read_file, get_frequencies
# from huffman import (
#     build_huffman_tree,
#     generate_codes,
#     encode_text,
#     calculate_compression_ratio
# )
# from shannon_fano import (
#     sort_by_frequency,
#     generate_shannon_fano_codes
# )


# def test_huffman(text):
#     freq = get_frequencies(text)
#     root = build_huffman_tree(freq)

#     codes = {}
#     generate_codes(root, "", codes)

#     encoded = encode_text(text, codes)
#     ratio = calculate_compression_ratio(text, encoded)

#     return ratio


# def test_shannon_fano(text):
#     freq = get_frequencies(text)
#     items = sort_by_frequency(freq)

#     codes = {}
#     generate_shannon_fano_codes(items, "", codes)

#     encoded = encode_text(text, codes)
#     ratio = calculate_compression_ratio(text, encoded)

#     return ratio
literature = read_file("test_files/literature.txt")
# random_text = read_file("test_files/random.txt")

# print("=== LITERATURE TEXT ===")
# print("Huffman ratio:", test_huffman(literature))
# print("Shannon-Fano ratio:", test_shannon_fano(literature))

# print("\n=== RANDOM TEXT ===")
# print("Huffman ratio:", test_huffman(random_text))
# print("Shannon-Fano ratio:", test_shannon_fano(random_text))



from utils import get_frequencies
from huffman import (
    build_huffman_tree,
    generate_codes,
    encode_text,
    decode_text,
    save_huff_file,
    load_huff_file
)

# Original text
# text = "aaabbc"

#  Compress
freq = get_frequencies(literature)
root = build_huffman_tree(freq)

codes = {}
generate_codes(root, "", codes)

encoded = encode_text(literature, codes)
save_huff_file("test_files/compressed.huff", freq, encoded)

print("Compressed file saved.")

# Decompress
loaded_freq, loaded_encoded = load_huff_file("test_files/compressed.huff")
new_root = build_huffman_tree(loaded_freq)
decoded_text = decode_text(loaded_encoded, new_root)

# SAVE ORIGINAL FILE HERE
with open("test_files/original.txt", "w", encoding="utf-8") as f:
    f.write(decoded_text)

print("Original file restored as original.txt")
