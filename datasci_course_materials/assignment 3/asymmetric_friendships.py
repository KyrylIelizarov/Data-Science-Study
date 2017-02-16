import MapReduce
import sys

"""
Asymmetric Frienships in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # key: person name
    # value: friend name
    key = record[0]
    value = record[1]
    mr.emit_intermediate(key, ['friend', value])
    mr.emit_intermediate(value, ['person', key])

def reducer(key, list_of_values):
    # key: name
    # list_of_values: list of friends and person to who is friend
    friends = []
    persons = []
    for item in list_of_values:
        if item[0] == 'friend':
            friends.append(item[1])
        elif item[0] == 'person':
            persons.append(item[1])

    for friend in friends:
        if friend not in persons:
            mr.emit((key, friend))
    for person in persons:
        if person not in friends:
                mr.emit((key,person))


# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
