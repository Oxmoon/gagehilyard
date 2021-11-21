import string
def encode (text, cipher):
    answer = ""
    for ch in text:
        if ch in string.ascii_lowercase:
            answer += cipher[ord(ch) - ord('a')]
        elif ch in string.ascii_uppercase:
            answer += cipher[ord(ch) - ord('a')].upper()
        else:
            answer += ch
    return answer

print(encode("Today is friday.", "bcdefghijklmnopqrstuvwxyza"))
