# WAP to check a given text (number or string) is pallindrome or not

A = 121
B = 'RADAR'
C = 'Arvind'

def pallindromeChk(in_text):
    AList = list(str(in_text))
    AList.reverse()
    print(in_text)
    out_text = ''.join([str(item) for item in AList])
    if str(in_text) == str(out_text):
        print("Thi item is pallindrome.")
    else:
        print("This item is not pallindrome.")

pallindromeChk(A)
pallindromeChk(B)
pallindromeChk(C)