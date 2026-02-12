text1 = "результат операции: 42"
text2 = "результат операции: 54"
text3 = "результат работы программы: 209"
text4 = "результат: 2"
text5 = "test for test так как Ната иногда tuple: 18"

def result_text (text):
    index_int = text.index(':') + 2
    int_text = int(text[index_int:])
    print(int_text + 10)

result_text(text1)
result_text(text2)
result_text(text3)
result_text(text4)
result_text(text5)
