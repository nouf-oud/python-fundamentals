#طباعة جدول من 5 اعمده و 3 سطورsearch
for i in range(1,4):
    for j in range(1,6):
        print(j, end=' ')
    print()

#نمط المثلث
print("___triangle___")
for i in range(1,6):
    for j in range(i):
        print(j, end=' ')
    print()

#البحث باستخدام break
print("\n___search with break___")
fruits = ["apple", "banana", "cherry", "date"]
search_fruit = "cherry"
for fruit in fruits:
    if fruit == search_fruit:
        print(f"{search_fruit}: found!")
        break
    else:
        print(f"{search_fruit}: not found!")