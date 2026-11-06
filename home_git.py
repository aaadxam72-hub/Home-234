# 1 masala   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def majoritiy_el(lst:list):
#     return max(set(lst), key=lst.count)


# n = int(input("Nechta son kiritasiz? "))
# nums=[]
# for i in range(n):
#     nums.append(int(input()))

# print(majoritiy_el(nums))

# 2 masala  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def search_by_genre(cinema: list, genre: str) -> list:
#     natija = []
#     for film in cinema:
#         if film["genre"] == genre:
#             natija.append(film)
#     return natija

# cinema = [
#     {"title": "Avatar", "genre": "Fantastika", "price": 40000},
#     {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
#     {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
#     {"title": "Dune", "genre": "Fantastika", "price": 35000}
# ]

# print(search_by_genre(cinema, "Fantastika"))

# print(search_by_genre([], "Drama"))

# 3 masala __________________________________________

def merge_unique_ids(active_users: list, new_users: list) -> list:
    result = []
    new = set()
    for i in active_users + new_users:
        if i not in new:
            new.add(i)
            result.append(i)
    return result

active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']

print(merge_unique_ids(active_users,new_users))

