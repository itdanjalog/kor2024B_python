class Scores:
    def __init__(self, math=None, science=None, history=None):
        # 과목별 점수를 초기화
        self.math = math
        self.science = science
        self.history = history
    def get_average(self):
        # None이 있는 경우도 있으므로 None 아닌 과목의 점수만 계산
        scores = []
        for score in [self.math, self.science, self.history]:
            if score is not None:
                scores.append(score)
        if scores:
            return sum(scores) / len(scores)
        return 0
class Student:
    def __init__(self, student_id, name, age, scores):
        # 학생 정보 초기화
        self.student_id = student_id
        self.name = name
        self.age = age
        self.scores = scores
    def get_average_score(self):
        # 학생의 평균 성적 반환
        return self.scores.get_average()
# 학생 데이터를 객체로 변환하는 함수
def convert_to_student_objects(students_data):
    students = []
    for data in students_data:
        scores = Scores(
            math=data["scores"].get("math"),
            science=data["scores"].get("science"),
            history=data["scores"].get("history")
        )
        student = Student(
            student_id=data["id"],
            name=data["name"],
            age=data["age"],
            scores=scores
        )
        students.append(student)
    return students

# 학생 데이터를 객체로 변환
students_data = [
    {
        "id": 1,
        "name": "John",
        "age": 16,
        "scores": {
            "math": 85,
            "science": 90,
            "history": 78
        }
    },
    {
        "id": 2,
        "name": "Alice",
        "age": 17,
        "scores": {
            "math": 92,
            "science": 88,
            "history": 80
        }
    },
    {
        "id": 3,
        "name": "Bob",
        "age": 16,
        "scores": {
            "math": 70,
            "science": 75
        }
    }
]

# 객체로 변환
students = convert_to_student_objects(students_data)

# 각 학생의 평균 성적을 출력
for student in students:
    print(f"Student: {student.name}, Average Score: {student.get_average_score():.2f}")