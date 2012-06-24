from random import randrange
from bisect import bisect_left


def random_list(N, max):
    return [randrange(max) for x in range(0, N)]

def subsequence(seq):
    """Returns the longest subsequence (non-contiguous) of seq that is
    strictly increasing.
    """
    # head[j] = index in 'seq' of the final member of the best subsequence
    # of length 'j + 1' yet found
    head = [0]
    # predecessor[j] = linked list of indices of best subsequence ending
    # at seq[j], in reverse order
    predecessor = [-1]
    for i in range(1, len(seq)):
        ## Find j such that:  seq[head[j - 1]] < seq[i] <= seq[head[j]]
        ## seq[head[j]] is increasing, so use binary search.
        j = bisect_left([seq[head[idx]] for idx in range(len(head))], seq[i])

        if j == len(head):
            head.append(i)
        if seq[i] < seq[head[j]]:
            head[j] = i

        predecessor.append(head[j - 1] if j > 0 else -1)

    ## trace subsequence back to output
    result = []
    trace_idx = head[-1]
    while (trace_idx >= 0):
        result.append(seq[trace_idx])
        trace_idx = predecessor[trace_idx]

    return result[::-1]


if __name__ == '__main__':
    l1 = random_list(15, 100)
    print(l1)
    print(subsequence(l1))
