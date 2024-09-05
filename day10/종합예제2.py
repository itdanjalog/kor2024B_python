class Task:
    def __init__(self, description, status):
        """할 일 객체 초기화"""
        self.description = description
        self.status = status

    def __str__(self):
        """할 일의 문자열 표현"""
        return f"{self.description} - 상태: {self.status}"

class TaskManager:
    def __init__(self):
        """할 일 리스트 초기화"""
        self.tasks = []

    def add_task(self, description, status):
        """새 할 일을 추가합니다."""
        task = Task(description, status)
        self.tasks.append(task)
        print("할 일이 추가되었습니다")

    def display_tasks(self):
        """모든 할 일을 출력합니다."""
        print("\n할 일 목록")
        for idx, task in enumerate(self.tasks, 1):
            print(f"{idx}. {task}")

    def delete_task(self, index):
        """지정한 인덱스의 할 일을 삭제합니다."""
        if 0 < index <= len(self.tasks):
            self.tasks.pop(index - 1)
            print("삭제 되었습니다.")
        else:
            print("잘못된 인덱스입니다.")

    def update_task(self, index, new_status):
        """지정한 인덱스의 할 일 상태를 업데이트합니다."""
        if 0 < index <= len(self.tasks):
            self.tasks[index - 1].status = new_status
            print("상태가 업데이트되었습니다")
        else:
            print("잘못된 인덱스입니다.")

def run_task_manager():
    """프로그램 실행"""
    manager = TaskManager()
    while True:
        print("\n할 일 관리 프로그램\n1. 할 일 추가\n2. 전체 목록 보기\n3. 할 일 삭제\n4. 할 일 상태 업데이트\n5. 종료")
        choice = input("선택하세요: ")

        if choice == "1":
            description = input("추가할 할 일을 입력하세요: ")
            manager.add_task(description, 'T')
        elif choice == "2":
            manager.display_tasks()
        elif choice == "3":
            manager.display_tasks()
            try:
                index = int(input("삭제할 할 일의 번호를 입력하세요: "))
                manager.delete_task(index)
            except ValueError:
                print("번호는 정수여야 합니다.")
        elif choice == "4":
            manager.display_tasks()
            try:
                index = int(input("상태를 업데이트할 할 일의 번호를 입력하세요: "))
                new_status = input("새 상태를 입력하세요: ")
                manager.update_task(index, new_status)
            except ValueError:
                print("번호는 정수여야 합니다.")
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

run_task_manager()