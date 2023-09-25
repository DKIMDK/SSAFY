# hw_7_2.py

# 아래 클래스를 수정하시오.
class StringRepeater:
   def __init__(self):
      pass
   
   def repeat_string(self, n, string):
      for _ in range(n):
         print(string)

repeater1 = StringRepeater()
repeater1.repeat_string(3, "Hello")
