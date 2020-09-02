import collections
import functools
import re
import sys
from typing import *

logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
## 영문자 / 숫자를 나눈다.
## 스플릿을 통해서
def reorderLogFiles(logs: List[str]) -> List[str]:
    letter , digit = [],[]

    for log in logs:
        print(log.split()[1:])
        if log.split()[1].isdigit():
            digit.append(log)

        else:
            letter.append(log)

    letter.sort(key=lambda x:(x.split()[1:], x.split()[0]))

    return letter + digit


print(reorderLogFiles(logs))

str = "A man, a plan, a canal: Panama"
def isPalindrome(s: str) -> bool:
    que : Deque = collections.deque()
    for char in s :
        if char.isalnum():
            que.append(char.lower())

    while len(que) > 1 :
        if que.popleft() != que.pop():
            return False


    return  True


def isPalindrome2(s: str) -> bool:
    str = s.lower()

    str = re.sub('[^a-z0-9]', '',str)

    return str == str[::-1]

print(isPalindrome2("a race"))


## 대소문자 구분x
## 영문자 및 소문자만
strs = ["eat","tea","tan","ate","nat","bat"]
## Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

nums_map = {}
nums = [1,2,3,4,5,6,7]
nums_map[7] = 1
target = 7
for i, v in enumerate(nums):
    if 9-2 in nums_map:
        print(nums_map)
        print("True!!")
        break

nums = [3,2,4]
target : int = 6
##-> List[int]
def twoSum(nums: List[int], target: int):
    nums_map = {}

    for index, num in enumerate(nums):
        print(target, num)
        if target - num in nums_map:
            print("target - num -- > ", target - num)
            print('nums_map -> ',nums_map)
            print('nums_map ',nums_map[target-num] ,'   index -> ', index)
        nums_map[num] = index



print(twoSum(nums,target))




##최대이익 구하기
prices = [7,1,5,3,6,4]

def maxProfit(prices:List[int]) -> int:
    profit = 0
    min_price = 100

    for price in prices:
        min_price = min(price, min_price)
        profit = max(profit, price-min_price)
        print(min_price-price)
        print('profit - > ',profit)

    return profit


print(maxProfit(prices))


#n개의 페어를이용한 min(a, b) 의 ㅎ바으로 만들수 있는 가장큰수를 만들어라
# [1,4,3,2]
# 출력 4
# n 은 2가되며 , 최대합은 4   min(1,2) + min (3,4) = 4 \
nums = [1,4,3,2]


def arrayPairSum(nums: List[int]) -> int:
    return sum(sorted(nums[::2]))

print(arrayPairSum(nums))

completion = ["leo", "kiki", "eden"]
participant = ["eden", "kiki"]
completion.sort()
participant.sort()
print(completion)
print(participant)


def solution(completion, participant) ->str :
    return list(collections.Counter(completion) - collections.Counter(participant))[0]


print(solution(completion,participant))

phone_book2 = ["123","456","789"]
phone_book = ["119", "97674223", "1195524421"] ## false 나와야함
a = len(phone_book)
deque = collections.deque()
deque = phone_book
print("ddd",deque)




##2 너무 어렵게 생각햇다.. 담부턴 쉽게 생각하자
def solution1(phone_book):
    first_number_len = len(phone_book[0])

    while len(phone_book) > 1:
        if phone_book[0] in phone_book.pop()[0:first_number_len]:
            return False
    return True

##방법3 정말.. 모든건 기본으로..
def solution2(phone_book):
    phone_book.sort()
    for a in range(len(phone_book)-1):
        if phone_book[a] in phone_book[a+1] :
            return False
    return True

##방법4 와 이런 방법이 있었다니..  zip / startswitch 를 알게됫다.
def solution3(phone_book):
    for p1, p2 in zip(phone_book, phone_book[1:]):
        if p2.startswith(p1):
            return False
    return True


print(solution3(phone_book))

##def solution(phone_book):


    ##for index, value in enumerate(phone_book):
        ##if phone_book[0] in phone_book[index+1].split():















