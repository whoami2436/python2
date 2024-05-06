# Task-1
# def squared(Coders):
#     kvadratlar = [x for x in Coders if x == 0 or (x > 0 and (int(x ** 0.5)) ** 2 == x)]
#     print("Listdən tapdığımız kvadrat ədədlər:")
#     for kvadrat in kvadratlar:
#         print(kvadrat)

# Coders = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# squared(Coders)

#######################################################################################################

# Task-2
# def x(daxil):
#     unrepeatable = []
#     for element in daxil:
#         if daxil.count(element) == 1:
#             unrepeatable.append(element)
#     return unrepeatable

# daxil = [-1, 1, 2, 2, 6, 7, 7, 'say']
# print("Tekrarlanmayan elementlər:", x(daxil))

##################################################################################################

# Task-3
# def x(input):
#     result = 1
#     for elements in input:
#         # isdigit() metodu, bir karakterin bir rakam olup olmadığını kontrol eder. Eğer karakter bir rakam ise True, değilse False döndürür(melumat).
#         if elements.isdigit():
#             result *= int(elements)
#     return result

# input = input("Rəqəmli inputu daxil edin: ")
# print("Inputdakı bütün rəqəmlərin bir birilərinə hasili: ", x(input))

#####################################################################################################

# Task-4
# def bolenler(num):
#     return [x for x in range(1, num + 1) if num % x == 0]

# num = int(input("Bölenləri tapılacaq ədədi daxil edin: "))
# print(f"{num} ədədin bölənləri:", bolenler(num))

######################################################################################################

# Task-5

# alfa = ['may', 'iyun', 'iyul']
# x = dict((i, len(i)) for i in alfa)
# print(x)

########################################################################################################

# Task-6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# def ilk(names):
#     # adlari secme
#     first_names = [name.split()[0].lower() for name in names]
#     return x
# x = ilk(names)
# print(x)

########################################################################################################

#  Task-7
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]
# results = [(nums1[i] + nums2[i]) / 2 for i in range(len(nums1))]
# print(results)


