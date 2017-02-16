import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence id
    # value: nucleotides
    key = record[0]
    value = record[1]
    cut_dna = value[:-10]
    mr.emit_intermediate(cut_dna, 1)


def reducer(key, list_of_values):
    # key: cut dna
    # value: smth
    mr.emit(key)


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
