# NVM Advanced Storage Objects

These are example implementations of the `PackedList` and `DynamicList` structures in Python.

- [PackedList](./packed.py)
- [DynamicList](./dynamic.py)

### Background

NVM prevents arrays from holding more than [1024 items](https://github.com/ontio/ontology/blob/e499b33d2383a0e8905a48146603e7aec90b8e90/vm/neovm/params.go#L26).

The `PackedList` is used to store more than 1024 items in a structure in NVM smart contracts.

The `PackedList` is limited that it can only hold 7 layers. That caps its storage at:
```
(1024 * 7 - 6)
```
or
```
7,162
```
total items.

A further implementation is the `DynamicList` storage object, that dynamically creates new `PackedList`'s as needed. It can store 1024 `PackedList` objects for a total storage of:
```
1024 * (1024 * 7 - 6)
```
or
```
7,333,888
```
total items.

### PackedList Implementation

The `PackedList` has the follow structure:

``` python
packed = {
  "array": [],
  "items": 0
}
```

Each time an item is added or removed from the array, the `items` count is changed.
When the `array` becomes full, it is wrapped in a new array.

For example, if the maximum array length was 2:

```
[]            // Starting
[1]           // Add 1
[1, 2]        // Add 2
[[1, 2], 3]   // Add 3
```

To remove an item, just swap it with the last item and remove the last item

```
[1, 3]        // Remove 2
```

### DynamicList Implementation

The `DynamicList` has the follow structure:

``` python
dynamic = {
  "packed": [],
  "items": 0
}
```

Each time an item is added or removed from the array, the `items` count is changed.
When all of the `PackedList` objects in the `packed` array become full, a new `PackedList` is allocated and added.
