# PackedList

This is an example implementation of the `PackedList` structure in Python.

### Background

In Ontology, the neovm prevents arrays from holding more than [1024 items](https://github.com/ontio/ontology/blob/e499b33d2383a0e8905a48146603e7aec90b8e90/vm/neovm/params.go#L26).

The `PackedList` is used to store more than 1024 items in a structure in Ontology smart contracts.

### Example Implementation

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

[]            // Starting
[1]           // Add 1
[1, 2]        // Add 2
[[1, 2], 3]   // Add 3

To remove an item, just swap it with the last item and remove the last item

[1, 3]        // Remove 2
