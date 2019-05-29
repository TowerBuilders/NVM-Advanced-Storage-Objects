MAXIMUM_ARRAY_LENGTH = 2

def Main(operation, args):
    if operation == 'PackedTest':
        return PackedTest()
    return False


def PackedTest():
    packed = PackedList()                               # []
    PackedAppend(packed, 1)                             # [1]
    PackedAppend(packed, 2)                             # [1, 2]
    PackedAppend(packed, 3)                             # [[1, 2], 3]
    itemCount = packed["items"]
    assert(itemCount == 3)

    PackedRemove(packed, 5)                             # [[1, 2], 3]
    PackedRemove(packed, 6)                             # [[1, 2], 3]
    PackedRemove(packed, 2)                             # [1, 3]
    PackedRemove(packed, 2)                             # [1, 3]
    itemCount = packed["items"]
    assert(itemCount == 2)
    assert(packed["array"][0] == 1)
    assert(packed["array"][1] == 3)

    PackedAppend(packed, 2)                             # [[1, 3], 2]
    itemCount = packed["items"]

    PackedAppend(packed, 4)                             # [[[1, 3], 2], 4]
    itemCount = packed["items"]

    PackedAppend(packed, 5)                             # [[[[1, 3], 2], 4], 5]
    itemCount = packed["items"]

    PackedAppend(packed, 6)                             # [[[[[1, 3], 2], 4], 5], 6]
    itemCount = packed["items"]

    PackedAppend(packed, 7)                             # [[[[[[1, 3], 2], 4], 5], 6], 7]
    itemCount = packed["items"]

    PackedAppend(packed, 8)                             # [[[[[[[1, 3], 2], 4], 5], 6], 7], 8]
    itemCount = packed["items"]

    PackedAppend(packed, 9)                             # [[[[[[[[1, 3], 2], 4], 5], 6], 7], 8], 9]
    itemCount = packed["items"]

    PackedRemove(packed, 2)                             # [[[[[[[1, 3], 9], 4], 5], 6], 7], 8]
    itemCount = packed["items"]

    PackedRemove(packed, 4)                             # [[[[[[1, 3], 9], 8], 5], 6], 7]
    itemCount = packed["items"]

    PackedRemove(packed, 5)                             # [[[[[1, 3], 9], 8], 7], 6]
    itemCount = packed["items"]

    PackedRemove(packed, 6)                             # [[[[1, 3], 9], 8], 7]
    itemCount = packed["items"]

    assert(itemCount == 5)
    return True


def PackedList():
    packed = {
        "array": [],
        "items": 0
    }
    return packed


def PackedAppend(packed, itm):
    array = packed["array"]
    length = len(array)
    if length == MAXIMUM_ARRAY_LENGTH:
        tmp = [array]
        tmp.append(itm)
        array = tmp
    else:
        array.append(itm)
    packed["array"] = array
    packed["items"] += 1


def PackedRemove(packed, itm):
    array = packed["array"]
    items = packed["items"]
    length = len(array)
    if length is 0:
        return

    swapped = do_swap(array, items, itm, length)
    if not swapped: # Item not found
        return
    if length == 2: # Peel off layer
        packed["array"] = array[0]
    else: # Remove last item
        packed["array"] = remove_last(array)
    packed["items"] -= 1


def remove_last(lst):
    length = len(lst)
    nLst = []
    for i in range(length - 1):
        nLst.append(lst[i])
    return nLst


def do_swap(array, items, itm, length):
    last = array[length - 1]
    if last is itm:
        return True
    layers = getLayers(items)
    found = do_find(array, length, layers, itm, last)
    if found:
        array[length - 1] = itm
        return True
    return False


def do_find(array, length, layers, itm, last):
    for i in range(length):
        item = array[i]
        if i == 0 and layers > 1:
            found = do_find(item, len(item), layers - 1, itm, last)
            if found:
                return True
        elif item is itm:
            array[i] = last
            return True
    return False


# Input             Layers      Items(n=2)      Items(n=3)          Items(n=4)

# 1   ... 1n-0      1           [1...2]         [1 ... 3]           [1 ... 4]
# 1n+1... 2n-1      2           [3]             [4 ... 5]           [5 ... 7]
# 2n-0... 3n-2      3           [4]             [6 ... 7]           [8 ... 10]
# 3n-1... 4n-3      4           [5]             [8 ... 9]           [11 ... 13]
# 4n-2... 5n-4      5           [6]             [10 ... 11]         [14 ... 16]

def getLayers(items):
    x = items
    x -= MAXIMUM_ARRAY_LENGTH
    layers = 1
    while x > 0:
        x -= (MAXIMUM_ARRAY_LENGTH - 1)
        layers += 1
    return layers
