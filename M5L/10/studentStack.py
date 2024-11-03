from student import Student

class StudentStack:
    def __init__(self, head = None, tail = None) -> None:
        self.head = head
        self.tail = tail
        self.studentAmount = 1


    def isEmpty(self):
        return self.head == None

    def push(self, studentName):
        newStudent = Student(studentName, self.studentAmount)
        if self.isEmpty():
            self.head = newStudent
            self.tail = newStudent
        else:
            newStudent.next = self.head
            self.head = newStudent

        self.studentAmount += 1