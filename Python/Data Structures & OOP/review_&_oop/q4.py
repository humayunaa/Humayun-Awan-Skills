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