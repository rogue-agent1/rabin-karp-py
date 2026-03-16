"""Rabin-Karp — rolling hash string matching."""
def search(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    if m > n: return []
    h_pat = 0
    h_txt = 0
    power = 1
    for i in range(m - 1):
        power = (power * base) % mod
    for i in range(m):
        h_pat = (h_pat * base + ord(pattern[i])) % mod
        h_txt = (h_txt * base + ord(text[i])) % mod
    results = []
    for i in range(n - m + 1):
        if h_pat == h_txt and text[i:i+m] == pattern:
            results.append(i)
        if i < n - m:
            h_txt = ((h_txt - ord(text[i]) * power) * base + ord(text[i + m])) % mod
    return results

if __name__ == "__main__":
    text = "GEEKS FOR GEEKS"
    pattern = "GEEK"
    positions = search(text, pattern)
    print(f"Text: {text}")
    print(f"Pattern: {pattern}")
    print(f"Found at: {positions}")
    assert positions == [0, 10], f"Wrong: {positions}"
    assert search("aaaa", "aa") == [0, 1, 2]
    print("All tests passed!")
