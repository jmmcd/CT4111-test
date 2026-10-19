def is_sorted(items):
    for i in range(len(items)-1):
        if items[i] > items[i + 1]:
            return False
    return True
