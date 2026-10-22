# p12_type_hint_run.py
def add(a:int,b:int) -> int:
    return a+b

def main():
    result = add(10,20)
    print(result)

    print(add("Hello"," World!"))
if __name__ == "__main__":
    main()