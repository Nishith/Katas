# Used to generate random arrays for testing
from random import randrange

# Length of the heap inside the array
heap_len = 0

def heapify(Arr, curr):
    """
    Checks if the given node is larger than its children
    Swaps it if its not and then calls heapify on the
    swapped child.
    """
    left = i * 2 + 1
    right = i * 2 + 2
    if left > heap_len:
        return

    largest = curr
    if Arr[curr] < Arr[left]:
        if Arr[left] < Arr[right] and right < heap_len:
            largest = right
        else:
            largest = left
    elif Arr[curr] < Arr[right] and right <= heap_len:
        largest = right
    if largest != curr:
        Arr[curr], Arr[largest] = Arr[largest], Arr[curr]
        heapify(Arr, largest)


def build_heap(Arr):
    """
    Uses the heapify function on the non-leaf nodes to build a heap
    """
    for i in range(len(Arr)//2, 0, -1):
        heapify(Arr, i-1)


def heap_sort(Arr):
    """
    Iteratively builds a heap and then puts the max value at
    the end of the array and then builds a heap with the
    remaining elements until the complete array is sorted
    """
    global heap_len
    heap_len = len(Arr) - 1
    build_heap(Arr)
#    print (heap_len)
    for i in range(len(Arr)-1, 0, -1):
        Arr[0], Arr[heap_len] = Arr[heap_len], Arr[0]
        heap_len -= 1
        heapify(Arr, 0)

def randomList(N, max):
    """ Generates a random list
    """
    return [randrange(max) for x in xrange(N)]


if __name__ == '__main__':
    for i in range(0, 10):
        Arr = randomList(15, 100)
        print(Arr)
        heap_sort(Arr)
        print(Arr)
        if sorted(Arr) == Arr:
            print(i)
            print(": Passed")
        else:
            print(i)
            print(": Failed")
