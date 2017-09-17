def countEachCharacterIn (inputString, length):
    dict = {}
    default = 1
    for i in inputString:
        if not dict.has_key(i):
            dict[i] = default
        else:
            dict[i] = default + 1

    print dict

inputString = "aabbccddeeffgghtuos"

countEachCharacterIn(inputString, len(inputString)-1)
