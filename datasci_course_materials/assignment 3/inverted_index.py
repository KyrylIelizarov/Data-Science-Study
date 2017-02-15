import MapReduce
import sys

"""
Inverted Index in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # docid: document identifier
    # text: document contents
    docid = record[0]
    text = record[1]
    words = text.split()
    for w in words:
        mr.emit_intermediate(w, docid)


def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    total = []
    for v in list_of_values:
        if v not in total:
            total.append(v)
    mr.emit((key, total))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
