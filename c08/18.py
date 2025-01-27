def count_sort(arr, target):
    hashtable = [0] * (target+1)
    for num in arr:
        if num <= target:
            hashtable[num] = 1
    return hashtable

def solution(arr, target):
    hashtable = count_sort(arr, target)

    for num in arr:
        complement = target - num

        if (complement != num and complement >= 0 and complement <= target and hashtable[complement] == 1):
            return True
        return False

# TEST 코드 입니다. 주석을 풀고 실행시켜보세요
# print(solution([1, 2, 3, 4, 8], 6)) # 반환값 : True
# print(solution([2, 3, 5, 9], 10)) # 반환값 : False
