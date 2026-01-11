import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMP_DIR = os.path.join(BASE_DIR, "temp")

os.makedirs(TEMP_DIR, exist_ok=True)


from flask import Flask, render_template, request, send_file
import io
from huffman import calculate_compression_ratio

from utils import get_frequencies
from huffman import (
    build_huffman_tree,
    generate_codes,
    encode_text,
    decode_text,
    save_huff_file,
    load_huff_file
)
from shannon_fano import (
    sort_by_frequency,
    generate_shannon_fano_codes
)


app = Flask(__name__)

@app.route('/')
def index():
    return render_template(
        "index.html",
        huffman_ratio=None,
        shannon_ratio=None,
        show_download=False
    )
@app.route("/compress", methods=["POST"])
def compress():
    file = request.files.get("textfile")

    if not file or not file.filename.endswith(".txt"):
        return "Please upload a valid .txt file", 400

    text = file.read().decode("utf-8")

    freq = get_frequencies(text)
    root = build_huffman_tree(freq)

    codes = {}
    generate_codes(root, "", codes)

    encoded = encode_text(text, codes)

    huffman_ratio = calculate_compression_ratio(text, encoded)
    # Shannon–Fano compression ratio (analysis only)
    freq_sf = get_frequencies(text)
    items = sort_by_frequency(freq_sf)

    sf_codes = {}
    generate_shannon_fano_codes(items, "", sf_codes)

    sf_encoded = encode_text(text, sf_codes)
    shannon_ratio = calculate_compression_ratio(text, sf_encoded)

    huff_path = os.path.join(TEMP_DIR, "compressed.huff")
    save_huff_file(huff_path, freq, encoded)


    print("DEBUG Huffman ratio:", huffman_ratio)  # 👈 ADD THIS

    return render_template(
    "index.html",
    huffman_ratio=round(huffman_ratio, 4),
    shannon_ratio=round(shannon_ratio, 4),
    show_download=True
    )   



@app.route("/decompress", methods=["POST"])
def decompress():
    file = request.files.get("hufffile")

    if not file or not file.filename.endswith(".huff"):
        return "Please upload a valid .huff file", 400

    # Save uploaded .huff temporarily
    huff_filename = "uploaded.huff"
    file.save(huff_filename)

    # Load and decompress
    freq, encoded = load_huff_file(huff_filename)
    root = build_huffman_tree(freq)
    decoded_text = decode_text(encoded, root)

    # Return reconstructed original file
    return send_file(
        io.BytesIO(decoded_text.encode("utf-8")),
        as_attachment=True,
        download_name="original.txt"
    )

@app.route("/download")
def download():
    huff_path = os.path.join(TEMP_DIR, "compressed.huff")

    if not os.path.exists(huff_path):
        return "Compressed file not found. Please compress a file first.", 404

    return send_file(
        huff_path,
        as_attachment=True,
        download_name="compressed.huff"
    )

if __name__ == "__main__":
    app.run(debug=True)


