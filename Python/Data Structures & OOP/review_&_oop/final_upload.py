#q1
def q1_sum(list):
    even = []
    for each in list:
        i = 0
        for num in each:
            if num % 2 == 0 and str(num).isnumeric():
                even.append(num)
            i = i + 1
    return sum(even)

print(q1_sum([[1, 0, 2],
        [5, 5, 7],
        [9, 4, 3]]))

#q2
vowels = ["A", "E", "I", "O", "U", "a", "e", "i", "o", "u"]

def move_vow(string):
    str_vow = []
    for each in string:
        if each in vowels:
            string = string.replace(each, "")
            str_vow.append(each)
    return "{}{}".format("".join(str_vow), string)
            

print(move_vow("This is DCU!"))

#q3
class Memories:
    
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)
    
    def remember(self, other):
        if hasattr(self, other):
            return getattr(self, other)
        else:
            return False

person1 = Memories(name="Tom", age=32, salary=50000)
print(person1.remember("salary"))
print(person1.remember("email"))
print(person1.remember("name"))

#q4
class Test:

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            if k == "passing_mark":
                setattr(self, k, int(v[:-1]))
            else:
                setattr(self, k, v)

class Student(Test):

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def take_test(self, other, student_answers):
        self.student_answers = student_answers
        num_correct_ans = len(other.correct_answers)
        for ans in self.student_answers:
            if ans in other.correct_answers:
                other.correct_answers.remove(ans)
        correct = (num_correct_ans - len(other.correct_answers))
        grade = (correct / num_correct_ans) * 100
        if grade >= other.passing_mark:
            return "{} passed the {} test with a mark of {}%".format(getattr(self, "name"), getattr(other, "subject_name"), grade)
        else:
            return "{} failed the {} test".format(getattr(self, "name"), getattr(other, "subject_name"))


paper1 = Test(subject_name="Maths", correct_answers=["1A", "2C", "3D", "4A", "5A"], passing_mark="60%")
paper2 = Test(subject_name="Chemistry", correct_answers=["1A", "2C"], passing_mark="50%")
stu1 = Student(name="John")
print(stu1.take_test(paper2, ["1A", "2C"]))

#Student(Test) means Student has access to all of Test. Inherits. Therefore i can use paper1's attributes

#q5
def histogram(list, shape):
    i = 0
    while i < len(list):
        print(list[i] * shape)
        i = i + 1
   
histogram([6, 2, 15, 3, 20, 5], "=")

#q6
def filter_star(dict, num):
    dict2 = {}
    for k, v in dict.items():
        if len(v) == num:
            dict2[k] = v
    print(dict2)

filter_star({"Luxury Chocolates" : "*****",
             "Tasty Chocolates" : "****",
             "Big Chocolates" : "*****",
             "Generic Chocolates" : "***"},
             4)
