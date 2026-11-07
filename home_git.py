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

# def merge_unique_ids(active_users: list, new_users: list) -> list:
#     result = []
#     new = set()
#     for i in active_users + new_users:
#         if i not in new:
#             new.add(i)
#             result.append(i)
#     return result

# active_users = ['U1001', 'U1002', 'U1003', 'U1004', 'U1001'] 
# new_users = ['U1003', 'U1005', 'U1006', 'U1002', 'U1007']

# print(merge_unique_ids(active_users,new_users))

# 4 masala >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# def sorted_by_price(products: list) -> list:
#     return sorted(products, key=lambda x: int(x[1]), reverse=True)

# products = [
#     ('Olma', '12000', '50'),
#     ('Banan', '8000', '100'),
#     ('Gilos', '15000', '70'),
#     ('Apelsin', '9000', '80'),
#     ('Anor', '30000', '20'),
#     ('Uzum', '20000', '40'),
#     ('Tarvuz', '25000', '15'),
#     ('Shaftoli', '18000', '60'),
#     ('Qovun', '40000', '25'),
#     ('Qulupnay', '35000', '10'),
# ]

# print(sorted_by_price(products))

# 5 masala >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

def are_numbers_ascending(txt:str) -> bool:
    new = []
    for soz in txt.split():
        if soz.isdigit():
            new.append(int(soz))

    for index in range(len(new[:-1])):
        if new[index] >= new[index+1]:
            return False
    else:
        return True

natija = are_numbers_ascending(input(">>> "))
print(natija)
