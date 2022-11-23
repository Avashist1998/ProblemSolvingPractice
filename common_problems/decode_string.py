"""Deconding the string."""


def find_sub_string_length(string: str) -> int:
    """Finds lenght of the substring.
    Args:
        string: string contain a substring of which lenght is needed
    Returns:
        lenght of the substring
    """
    # Assume all s start with "["
    len_of_string = len(string)
    numbracket = 0
    for i in range(len_of_string):
        if string[i] == "[":
            numbracket += 1
        elif string[i] == "]":
            numbracket -= 1

        if numbracket == 0:
            return i + 1
    return len_of_string


def decode_string(string: str) -> str:
    """Decodes the incoded string.
    Args:
        string: encoded string.
    Returns:
        decoded string.
    """
    i = 0
    res = ""
    tmp_num = ""
    len_of_string = len(string)
    while i < len_of_string:

        if string[i].isdigit():
            tmp_num += string[i]
            i += 1

        elif string[i] == "[":
            print("This happend")
            # find the substring of the opposite bracket
            sub_string_length = find_sub_string_length(string[i:])
            # then process the substring
            sub_string = string[i + 1:i + sub_string_length - 1]
            decoder_substring = decode_string(sub_string)

            # Then properly update i and res
            for _ in range(int(tmp_num)):
                res += decoder_substring

            i += sub_string_length
            tmp_num = ""

        elif string[i].isalpha():
            res += string[i]
            i += 1
    return res


print(decode_string("3[2[nwi]12[asdfjaos]]"))
