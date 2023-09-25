#5_1
# 아래 함수를 수정하시오.
def reverse_string(word):
    word_list = list(word)
    word_list.reverse()
    answer = ''.join(word_list)
    return answer
    
    
result = reverse_string("Hello, World!")
print(result)