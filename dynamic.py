#### Dynamic/PackedList ####

MAXIMUM_ARRAY_LENGTH = 1024

def DynamicList():
    '''
    Creates a new DynamicList
    '''

    dynamic = {
        "packed": [],
        "items": 0
    }
    return dynamic


def DynamicAppend(dynamic, itm):
    '''
    Appends an item to a packed list or creates a new one.

    :param packed: The DynamicList
    :param itm: The item to add to the DynamicList
    '''
    packedArr = dynamic["packed"]
    maximum = MAXIMUM_ARRAY_LENGTH * 7 - 6

    length = len(packedArr)
    for i in range(length):
        packed = packedArr[i]
        if packed["items"] < maximum:
            PackedAppend(packed, itm)
            dynamic["packed"][i] = packed
            dynamic["items"] += 1
            return True

    if length < MAXIMUM_ARRAY_LENGTH:
        packed = PackedList()
        PackedAppend(packed, itm)
        packedArr.append(packed)
        dynamic["items"] += 1
        return True
    return False


def DynamicRemove(dynamic, itm):
    '''
    Removes an item from the DynamicList.

    :param packed: The DynamicList
    :param itm: The item to remove from the DynamicList
    '''

    packedArr = dynamic["packed"]
    length = len(packedArr)
    for i in range(length):
        packed = packedArr[i]
        if PackedRemove(packed, itm):
            dynamic["packed"][i] = packed
            dynamic["items"] -= 1
            return True
    return False


def PackedList():
    '''
    Creates a new PackedList
    '''

    packed = {
        "array": [],
        "items": 0
    }
    return packed


def PackedAppend(packed, itm):
    '''
    Appends an item to the PackedList.array or wraps it in a new layer if full.
    Increments the PackedList.items count.

    :param packed: The PackedList
    :param itm: The item to add to the PackedList
    '''

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
    '''
    Removes an item from the PackedList.array.

    :param packed: The PackedList
    :param itm: The item to remove from the PackedList
    '''

    if not do_swap(packed, itm): # Item not found
        return False

    if len(packed["array"]) == 2: # Peel off layer
        peel(packed)
    else: # Remove last item
        remove_last(packed["array"])
    packed["items"] -= 1
    return True


def peel(packed):
    '''
    Peels a layer off of the PackedList.

    :param packed: The PackedList
    '''

    packed["array"] = packed["array"][0]


def remove_last(lst):
    '''
    Removes the last item from a list.

    :param lst: The list to remove the item from
    '''

    length = len(lst)
    nLst = []
    for i in range(length - 1):
        nLst.append(lst[i])
    lst = nLst


def do_swap(packed, itm):
    '''
    Swaps the last item in the PackedList.array with the item.

    :param packed: The PackedList
    :param itm: The item to swap
    '''

    array = packed["array"]
    items = packed["items"]
    length = len(array)
    if length is 0:
        return False

    last = array[length - 1]
    if last is itm:
        return True

    layers = get_layers(items)
    if do_find(array, length, layers, itm, last):
        array[length - 1] = itm
        return True
    return False


def do_find(array, length, layers, itm, last):
    '''
    Finds the item in the array and swaps it with the last item

    :param array: The PackedList.array
    :param length: The length of the PackedList.array
    :param layers: The amount of layers in the PackedList.array
    :param itm: The item to swap
    :param last: The last item in the PackedList.array
    '''

    for i in range(length):
        item = array[i]
        if i == 0 and layers > 1:
            if do_find(item, len(item), layers - 1, itm, last):
                return True
        elif item is itm:
            array[i] = last
            return True
    return False


def get_layers(items):
    '''
    Calculated the amount of layers in the PackedList

    :param items: The amount of items in the PackedList
    '''

    x = items
    x -= MAXIMUM_ARRAY_LENGTH
    layers = 1
    while x > 0:
        x -= (MAXIMUM_ARRAY_LENGTH - 1)
        layers += 1
    return layers
