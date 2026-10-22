print("="*50)
print("1. 함수 실행 전·후 로그 출력")
print("="*50)


def execution_log(func):
    def wrapper():
        print("함수 실행 시작")

        func()

        print("함수 실행 종료")

    return wrapper


@execution_log
def hello():
    print("Hello Python")

@execution_log
def goodbye():
    print("Goodbye Python")

hello()
print("-"*50)
goodbye()