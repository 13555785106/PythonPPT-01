def search(sequence, number, lower=0, upper=None):
    if (upper is None):
        upper = len(sequence) - 1
    if lower == upper:
        assert number == sequence[upper]
        return upper
    else:
        middle = (lower + upper) // 2
        if number > sequence[middle]:
            return search(sequence, number, middle + 1, upper)
        else:
            return search(sequence, number, lower, middle)
seq = [89, 34, 23, 56, 78, 90, 101, 12]
seq.sort()
print seq
print search(seq, 101)
