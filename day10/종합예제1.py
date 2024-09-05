# 할 일 리스트 초기화
todo_list = []

def add_task(task, status):
    """할 일을 리스트에 추가합니다."""
    todo_list.append({"task": task, "status": status})
    print("할 일이 추가되었습니다")

def display_tasks():
    """리스트의 모든 할 일을 출력합니다."""
    print("\n할 일 목록")
    index = 1
    for item in todo_list:
        print(f"{index}. {item['task']} - 상태: {item['status']}")
        index += 1

def delete_task(index):
    """지정한 인덱스의 할 일을 삭제합니다."""
    if 0 < index <= len(todo_list):
        todo_list.pop(index - 1)
        print("삭제 되었습니다.")
    else:
        print("잘못된 인덱스입니다.")

def update_task(index, new_status):
    """지정한 인덱스의 할 일 상태를 업데이트합니다."""
    if 0 < index <= len(todo_list):
        todo_list[index - 1]['status'] = new_status
        print("상태가 업데이트되었습니다")
    else:
        print("잘못된 인덱스입니다.")

def main():
    while True:
        print("\n할 일 관리 프로그램\n1. 할 일 추가\n2. 전체 목록 보기\n3. 할 일 삭제\n4. 할 일 상태 업데이트\n5. 종료")
        choice = input("선택하세요: ")

        if choice == "1":
            task = input("추가할 할 일을 입력하세요. : ")
            add_task(task, '미완료')
        elif choice == "2":
            display_tasks()
        elif choice == "3":
            display_tasks()
            index = int(input("삭제할 할 일의 번호를 입력하세요: "))
            delete_task(index)
        elif choice == "4":
            display_tasks()
            index = int(input("상태를 업데이트할 할 일의 번호를 입력하세요: "))
            new_status = input("새 상태를 입력하세요: ")
            update_task(index, new_status)
        elif choice == "5":
            print("프로그램을 종료합니다.")
            break
        else:
            print("잘못된 선택입니다. 다시 시도하세요.")

# 프로그램 실행
main()
