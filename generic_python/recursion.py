#Simple recursion to unwrap an integer list elements
input_list = [[1],[2],[3,4,[5,6]],[[[[[[[[[[[[[7]]]]]],8]]]]]]]]


def unwrap(n):
    if type(n) == type(int()):
        return n
    if type(n) == type(list()):
        if len(n) == 1:
            unwraped_element = unwrap(n[0])
            unwraped_element = [unwraped_element] if type(unwraped_element) != type(list()) else unwraped_element
            return unwraped_element
        else:
            unwraped_element = unwrap(n[0])
            unwraped_element = [unwraped_element] if type(unwraped_element) != type(list()) else unwraped_element
            unwraped_remining = unwrap(n[1:])
            unwraped_element.extend(unwraped_remining)
            return unwraped_element

if __name__ == "__main__":
    print(unwrap(input_list))