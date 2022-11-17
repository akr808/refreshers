#Simple recursion to unwrap an integer list elements
a = [[1],[2],[3,4,[5,6]],[[[[[[[[[[[[[7]]]]]],8]]]]]]]]


def unwrap(n):
    if type(n) == type(int()):
        return n
    if type(n) == type(list()):
        if len(n) == 1:
            a = unwrap(n[0])
            a = [a] if type(a) != type(list()) else a
            return a
        else:
            a = unwrap(n[0])
            a = [a] if type(a) != type(list()) else a
            b = unwrap(n[1:])
            a.extend(b)
            return a

print(unwrap(a))