# Selection

for i -> n
    min = i
    for j:i++ -> n
        if arr:j < arr:min
            min = j

    swap min & i

# Insertion

for i:1 -> n
    key = arr:i
    j = i--

    while j > -1 & arr:j > key
        arr:j++ = arr:j
        j--

    arr:j++ = key

# Bubble

for i -> n--
    for j -> n - i--
        if arr:j > arr:j++
            swap j & j++

# Merge

    if l < r then
    
    m = l + (r-l)/2

    sort(l, m)
    sort(m++, r)

    merge(l, m, r)
     
# Quick

if (l < h) then

p = partition(l, h)

sort(l, p--)
sort(p++, h)

# Partition
p //from some source random/high/low
i = l--

for j:l -> h--
    if arr:j < p
        i++
        swap j & i

swap i++ & h

ret i++
