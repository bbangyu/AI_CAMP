print("="*50)
print("3. API 요청 횟수 제한하기")
print("="*50)

def create_rate_limiter(limit):
    count = 0

    def request():
        nonlocal count

        if count >= limit:
            return '요청 횟수 초과'

        count += 1 
        #요청 성공 (1/3)
        return f'요청 성공 ({count}/{limit})'       
        

    return request


api_request=create_rate_limiter(3)

print(api_request())
print(api_request())
print(api_request())
print(api_request())
print(api_request())
