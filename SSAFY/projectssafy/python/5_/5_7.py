# main.py

# 아래 함수를 수정하시오.
# def find_min_max(lst):
#     return (min(lst), max(lst))
def find_min_max(lst):
    return (sorted(lst)[0], sorted(lst)[len(lst)-1])
    
result = find_min_max([3, 1, 7, 2, 5])
print(result) # (1, 7)
