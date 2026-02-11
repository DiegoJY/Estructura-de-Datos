ArrayUni = [1,2,4,5,7,9,11,11,13,14,15,16,16]
i = 1
while i < len(ArrayUni):
    if ArrayUni[i] == ArrayUni[i - 1]:
        ArrayUni.pop(i)
    else:
        i += 1
print(ArrayUni)