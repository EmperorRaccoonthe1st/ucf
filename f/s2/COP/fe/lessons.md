# Lessons-Learned

- _Slow Down_, make sure you read the question carefully!

## DMA
- Make sure question uses `typedef struct StructName`, otherwise you use `struct StructName` when referencing a struct.
- If deallocating from an array of structs, use `arr[i].` not `arr[i]->`
- "Heap Space" really means an array of structs.

## Linked Lists
- If deleting, make sure to check if 'head' is being deleted

## Summations
- When doing a \Sigma I summation, take the 1/2 out after.

## Heaps
- For heaps ensure idx is greater than zero and less than size.
- To restore heap property you must heapify up and down.
- When deleting a node within the heap, change size first and then restore heap property.
- When deleting node within heap, replace it with last element.

## Tries
- You should return the value of `is_word` when counting words in a trie.

## Hashmaps
- The clumps within a hash table are called "Primary Clustering".
