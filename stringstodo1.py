# Remove Blanks
# Create a function that, given a string, returns all of that string’s contents, but without blanks. 

# If given the string " Pl ayTha tF u nkyM usi c ", return "PlayThatFunkyMusic".

def removeBlanks():
    string = 'Pl ayTha tF u nkyM usi c'
    print(string.replace(" ",""))
    return(string.replace(" ",""))

removeBlanks()


# Get Digits
# Create a JavaScript function that given a string, returns the integer made from the string’s digits. Given "0s1a3y5w7h9a2t4?6!8?0", the function should return the number 1357924680.

def onlyNumbers(str):
    num = ""
    for i in range(len(str)):
        if (str[i].isdigit()):
            num = num+ str[i]
    print(num)

onlyNumbers('0s1a3y5w7h9a2t4?6!8?0')



# Acronyms
# Create a function that, given a string, returns the string’s acronym (first letters only, capitalized). 

# Given " there's no free lunch - gotta pay yer way. ", return "TNFL-GPYW". 

# Given "Live from New York, it's Saturday Night!", return "LFNYISN".

def onlyCaps(str):
    caps = str[0]
    for i in range(len(str)):
        if str[i-1] == ' ':
            caps += str[i]
    caps = caps.upper()
    print(caps)

onlyCaps("there's no free lunch - gotta pay yer way.")



# Zip Arrays into Map
# Associative arrays are sometimes called maps because a key (string) maps to a value. Given two arrays, create an associative array (map) containing keys of the first, and values of the second. For arr1 = ["abc", 3, "yo"] and arr2 = [42, "wassup", true], return {"abc": 42, 3: "wassup", "yo": true}.

def zipMap():
    arr1  = ["abc", 3, "yo"]
    arr2 = [42, "wassup", True]
    map = {}
    for i  in arr1:
        for x in arr2:
            map[i] = x
            arr2.remove(x)
            break
    print(map)
zipMap()

# Invert Hash
# Associative arrays are also called hashes (we’ll learn why later). Build invertHash(assocArr) to convert hash keys to values, and values to keys. 

# Example: given {"name": "Zaphod", "charm": "high", "morals": "dicey"}, return object {"Zaphod": "name", "high":"charm", "dicey": "morals"}.

def invertHash():
    hash  = {"name": "Zaphod", "charm": "high", "morals": "dicey"}
    new_hash = {}
    for key, value  in hash.items():
        if value in new_hash:
            new_hash[value].append(key)
        else:
            new_hash[value] = key
    print(new_hash)
invertHash()