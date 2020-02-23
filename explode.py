def explode (arr):
    sum = 0
    for element in arr:
        if str(element).isdigit(): sum += element
    if sum == 0: return "Void!"
    return [arr] * sum
