text1 = "результат операции: 42"
text2 = "результат операции: 514"
text3 ="результат работы программы: 9"
index_int1 = text1.index(':') + 2
int_text1 = int(text1[index_int1:])
print(int_text1 + 10)

index_int2 = text2.index(':') + 2
int_text2 = int(text2[index_int2:])
print(int_text2 + 10)

index_int3 = text3.index(':') + 2
int_text3 = int(text3[index_int3:])
print(int_text3 + 10)