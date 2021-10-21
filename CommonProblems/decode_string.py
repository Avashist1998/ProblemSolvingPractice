def subStringLengthFinder(s:str) -> int:

    # Assume all s start with "["
    n = len(s)
    numbracket = 0
    for i in range(n):
        if s[i] == "[":
            numbracket += 1
        elif s[i] == "]":
            numbracket -= 1
        
        if numbracket == 0:
            return i+1 
    return n
def stringDecoder(s:str)->str:
    n = len(s)
    res = ""
    i = 0
    tmp_num = ""
    while i < n:
        
        if s[i].isdigit():
            "They did catch a number"
            tmp_num += s[i]
            i+=1

        elif s[i] == "[":
            print("This happend")
            # find the substring of the opposite bracket
            subStringLength = subStringLengthFinder(s[i:])
            # then process the substring
            subString = s[i+1:i+subStringLength-1]
            decoderSubstring = stringDecoder(subString)

            # Then properly update i and res 
            for _ in range(int(tmp_num)):
                res += decoderSubstring

            i += subStringLength
            tmp_num = ""

        elif s[i].isalpha():
            print("this is alpha")
            res += s[i]
            i+=1
    return res



print(stringDecoder("3[2[nwi]12[asdfjaos]]"))