#A program to recursively unwrap a list with any number of nesting
def unwrap(lst):
    # Recursive method to unwrap a list
    #Parameters:
    # lst: A list that is unwrapped
    #Returns:
    # A list of elemts that is unwrapped from lst
    if isinstance(lst,list):
        if len(lst) == 1:
            return unwrap(lst[0]) if isinstance(lst[0],list) else lst
        else:
            first_list =  unwrap(lst[:1])
            second_list =unwrap(lst[1:])
            first_list.extend(second_list)
            return first_list
    else:
        return [lst]

if __name__ == "__main__":
    print(unwrap([1, 2, 3, [4, [[[[[[5]]]]]]], [[6, 7], 8], 9]))
    #Output:[1, 2, 3, 4, 5, 6, 7, 8, 9]
