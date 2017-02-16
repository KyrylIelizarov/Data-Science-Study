import MapReduce
import sys

"""
Friend Count in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # key: Person Name
    # value: Friend Name
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, 1)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = 0
    for v in list_of_values:
        total += v
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
