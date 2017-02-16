import MapReduce
import sys

"""
Matrix Multiply in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line


L = 5
M = 5
N = 5

def mapper(record):
    # key: (matrix name, i , j , value_ij)
    # value: document contents
    key = record[0:3]
    value = record[3]
    if key[0] == 'a':
        for k in range(N):
            mr.emit_intermediate((key[1],k), record)
    if key[0] == 'b':
        for i in range(L):
            mr.emit_intermediate((i,key[2]), record)

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for j in range(M):
        a = 0
        b = 0
        for element in list_of_values:
            if element[0] == 'a' and element[2] == j:
                a = element[3]
            if element[0] == 'b' and element[1] == j:
                b = element[3]
        total += a*b
    if total != 0:
        mr.emit((key[0], key[1], total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
