# p13_type_hint_run.py
def find_member(member_id:str) -> str| None:
		
		if member_id == 'user01':
			return "이상무"
			
		return None

def main():
	print(find_member("user01"))
	print(find_member("user99"))
 
if __name__ == "__main__":
    main()