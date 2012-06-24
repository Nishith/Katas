"""
Finds the n largest files in a given directory
Args: <num of files> <directory>
"""

import heapq
import os, os.path
import sys
import operator

def file_sizes(directory):
    for path, _, filenames in os.walk(directory):
        for name in filenames:
            full_path = os.path.join(path, name)
            yield full_path, os.path.getsize(full_path)


if __name__ == '__main__':
    num_files, directory = sys.argv[1:]
    num_files = int(num_files)
    
    big_files = heapq.nlargest(
        num_files, file_sizes(directory), key=operator.itemgetter(1))

    print(*("{}\t{:>}".format(*b) for b in big_files))
