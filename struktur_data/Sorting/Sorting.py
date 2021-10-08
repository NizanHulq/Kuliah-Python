import sorting
import timeit
import sys

data = [1, 8, 3, 5, 6, 9, 2, 4,23,5,4,345,23,4,5,6,3,3,5,6,4,15]
# =============================================================================
# ,64,56,34,33,645,73,5,24,432,12,
#         2342,32,423,45,4,5,6,7,878,57656,74,56,546,54,678,4324,3,23,4,234,2,34,546,45,65,67,8,856,
#         54664,6756,754,56345,3,234,900,54,5,6,76,544,34,123,876,4,53,987,64,56765,3,45,24,323,4,546,
#         8,68,67,654,67,87874,53,432,547,42,4,3,45,64,67,567,567,5,87,100,2,32,209,2312,345,32,67,6,
#         323,4334,5435,2,34,56,457,467,4,34,52,34,45,67,435,2,34,7230,36,4,75,67,67,3445,24,456,34,5,
#         5,56,3,45,356,7,57,689,98,909,76,78,67897,4534,5675,678,3,23,4,234,6987,564,567,4,565,67,578,
#         8,89,8498,4,345,67,67,9,89,78,9,356,34,567,89,56,7843,35656,8,67,69,6384,689,789,7894,56234,
#         13454,6,57,567,578,35,234,3464,67,58,68,35,345,47,57,425,253,46,467,58,4,578
# =============================================================================

print("=======================")
startTime = timeit.default_timer()
res = sorting.bubble(data)
print('Bubble Sort      : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.bucket(data)
print('Bucket Sort      : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.comb(data)
print('Comb Sort        : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.counting(data)
print('Counting Sort    : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.maxheap(data)
print('Max Heap Sort    : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.minheap(data)
print('Min Heap Sort    : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.merge(data)
print('Merge Sort       : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.quick(data)
print('Quick Sort       : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.radix(data)
print('Radix Sort       : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.selection(data)
print('Selection Sort   : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))

print("=======================")
startTime = timeit.default_timer()
res = sorting.cycle(data)
print('Cycle Sort       : ')
print( res)
print("waktu : ",format(timeit.default_timer()-startTime))
print("Memori : ",sys.getsizeof(res))