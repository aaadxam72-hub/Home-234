# 1 masala   >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# def majoritiy_el(lst:list):
#     return max(set(lst), key=lst.count)


# n = int(input("Nechta son kiritasiz? "))
# nums=[]
# for i in range(n):
#     nums.append(int(input()))

# print(majoritiy_el(nums))

# 2 masala  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
def search_by_genre(cinema: list, genre: str) -> list:
    natija = []
    for film in cinema:
        if film["genre"] == genre:
            natija.append(film)
    return natija

cinema = [
    {"title": "Avatar", "genre": "Fantastika", "price": 40000},
    {"title": "Sherlock", "genre": "Detektiv", "price": 30000},
    {"title": "Oq yo'l", "genre": "Drama", "price": 25000},
    {"title": "Dune", "genre": "Fantastika", "price": 35000}
]

print(search_by_genre(cinema, "Fantastika"))

print(search_by_genre([], "Drama"))
