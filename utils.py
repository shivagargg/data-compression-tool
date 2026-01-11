def read_file(filepath):
    f = open(filepath, 'r', encoding='utf-8')
    text = f.read()
    f.close()
    return text
def get_frequencies(text):
    freq = {}

    for ch in text:
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

    return freq
