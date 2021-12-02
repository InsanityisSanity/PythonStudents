shopping_list = ['milk', 'pasta', 'spam', 'bread', 'rice']

# for item in shopping_list:
#     if item != 'spam':
#         print('Buy ' + item)

# for item in shopping_list:
#     if item == 'spam':
#         continue # continues from the beginning of the loop, terminating at that point basically

#     print('Buy ' + item)

for item in shopping_list:
    if item == 'spam':
        break  # stops the loop completly when it finds what it is lookign for
    print('Buy ' + item)
