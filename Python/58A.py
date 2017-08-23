def isSubstringPresent(substr, strng):
    if substr == "":
        return True
    if substr[0] in strng:
        return isSubstringPresent(substr[1:], strng[(strng.find(substr[0]) + 1):])
    return False


print("YES" if isSubstringPresent("hello", input()) else "NO")