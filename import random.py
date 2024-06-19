import random

#메뉴와 가격 리스트를 각각 만들고 출력하기
menus = ['떡볶이', '순대', '치킨', '주먹밥', '튀김', '라면']
prices = [2500, 3000, 5000, 1500, 2000, 2500]

print("메뉴판: \n")

for i in range(len(menus)):
​   ​print(menus[i], prices[i])

#메뉴 중에서 랜덤으로 3개 메뉴를 뽑기
my_menu = random.sample(menus, 3)
print('\n', my_menu)
