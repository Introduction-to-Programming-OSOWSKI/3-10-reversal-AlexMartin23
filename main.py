def reversal(w):
    word = w[len(w)-1]
    for i in range(2,len(w)+1):
        word = word + w[len(w)-i]
    return word

print(reversal("alex"))
