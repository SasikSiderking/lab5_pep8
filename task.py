import math, sys  # несколько импортов в одной строке (E401)
def  bad_spacing ():  # два пробела перед именем функции, пробел перед скобкой (E211,E302)
   x=5   # отсутствие пробелов вокруг оператора (E225)
   y = 10
   result=x+y   # нет пробелов (E225)
   print("Result:",result)  # нет пробела после запятой (E231)
   if result>10:  
        print("Greater")
   else:
        print("Smaller")

def long_line():
    # очень длинная строка >79 символов (E501)
    s = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    return s

def missing_docstring():  
    pass

class MyClass:
    def __init__(self,val):
        self.val=val  # E225
    def get_val(self):return self.val  # E704 (multiple statements on one line)

if __name__=="__main__":  # E225 (пробелы вокруг ==)
    bad_spacing()
    print(long_line())
    obj=MyClass(42)  # E225
    print(obj.get_val())
