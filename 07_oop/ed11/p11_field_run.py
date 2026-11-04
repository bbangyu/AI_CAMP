
from dataclasses import dataclass, field

@dataclass
class Account:
    user_id: str
    password: str = field(repr=False,compare=True)

account1 = Account("user01","pw123")
account2 = Account("user01","different")

print(account1)
print(account1==account2)