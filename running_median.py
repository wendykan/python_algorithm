
import heapq



def get_median(input_list):
    min_heap = [] # stores the upper half
    max_heap = [] # stores the lower half
    medians = []

    heapq.heappush(max_heap, min(input_list[0], input_list[1]))
    heapq.heappush(min_heap, max(input_list[0], input_list[1]))

    for item in input_list[2:]:
        if item > min_heap[0]: # if larger than root in min heap then just place it in min heap
            heapq.heappush(min_heap, item)
            # print(max_heap, min_heap)
        else:
            heapq.heappush(max_heap, item)
            # print(max_heap, min_heap)
        
        min_heap, max_heap = balance_heaps(min_heap, max_heap)
        medians.append(get_median_from_heaps(min_heap, max_heap))
    return medians

def get_median_from_heaps(min_heap, max_heap):
    len_max = len(max_heap)
    len_min = len(min_heap)
    if len_max == len_min:
        return (max_heap[0]+min_heap[0]) / 2
    elif len_max > len_min:
        return max_heap[0]
    else:
        return min_heap[0]


def balance_heaps(min_heap, max_heap):
    len_max = len(max_heap)
    len_min = len(min_heap)

    if len_max > len_min + 1:
        # move the extra item in min heap
        heapq.heappush(min_heap, heapq.heappop(max_heap))
    elif len_min > len_max + 1:
        heapq.heappush(max_heap, heapq.heappop(min_heap))
    heapq.heapify(min_heap)
    heapq._heapify_max(max_heap)
    return min_heap, max_heap

print(get_median([1,2,3,4,5,6,7]))

print(get_median([1,2,3,4,5,6]))