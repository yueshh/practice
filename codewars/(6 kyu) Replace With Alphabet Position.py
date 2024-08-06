def alphabet_position(text):
    alp = "abcdefghijklmnopqrstuvwxyz"
    res = ""
    ' '.join(text)
    for c in text.lower():
        if c in alp:
            result = alp.find(c) + 1
            res += str(result) + ' '
    return res.rstrip() 
    
