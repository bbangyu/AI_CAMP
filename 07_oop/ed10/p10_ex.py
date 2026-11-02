from typing import Protocol, runtime_checkable


# 1. Protocol
@runtime_checkable
class Saveable(Protocol):
    def save(self) -> None:
        ...

# 2. FileStorage
class FileStorage:
    def save(self) -> None:
        print("파일에 데이터를 저장합니다.")

# 3. DatabaseStorage
class DatabaseStorage:
    def save(self) -> None:
        print("데이터베이스에 데이터를 저장합니다.")

# 4. Protocol을 사용하는 함수: save_data(storage:Saveable)
def save_data(storage: Saveable) -> None:
    storage.save()

def main():
    # file_storage = FileStorage()
    # database_storage = DatabaseStorage()

    # save_data(file_storage)
    # save_data(database_storage)


    storages: list[Saveable] = [
        FileStorage(),
        DatabaseStorage()
    ]

    for storage in storages:
        if isinstance(storage, Saveable):
            save_data(storage)

if __name__ == "__main__":
    main()