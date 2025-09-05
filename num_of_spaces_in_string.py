def remove_spaces(string):
    result = ""
    for char in string:
        if char != " ":
            result += char
    return result

print(remove_spaces("All I need is to remove all the empty spaces from the string"))