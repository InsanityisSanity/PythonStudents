shopping_list = ['milk', 'eggs', 'pasta', 'spam', 'bread', 'rice']

item_to_find = 'rice'
found_at = None  # a constant to set no value as default, like Null

for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
if found_at is not None:
    print(f'Item found at position {found_at}')
else:
    print(f'{item_to_find} was not found!')
