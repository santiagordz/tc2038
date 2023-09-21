def buildSuffixArray(text):
    suffixes = [(text[i:], i) for i in range(len(text))]

    suffixes.sort()

    suffix = [suffix[0] for suffix in suffixes]
    print(suffix)

    suffix_array = [suffix[1] for suffix in suffixes]

    return suffix_array


# Example usage:
text = "banana"
suffix_array = buildSuffixArray(text)
print(suffix_array)  # Output: [5, 3, 1, 0, 4, 2]
