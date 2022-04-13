def matchingStrings(strings, queries):
    count = {}
    result = []
    for val in strings:
        count[val] = count[val] + 1 if val in count else 1
    for val in queries:
        toBeAppended = count[val] if val in count else 0
        result.append(toBeAppended)
    
    return result
    



strings = ['ab', 'ab', 'abc']
queries = ['ab', 'abc', 'bc']

print(matchingStrings(strings, queries))