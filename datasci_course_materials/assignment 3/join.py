import MapReduce
import sys

"""
Join in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()


# =============================
# Do not modify above this line

def mapper(record):
    # key: order_id
    # value: table contents
    key = record[1]
    value = record
    mr.emit_intermediate(key, value)


def reducer(key, list_of_values):
    # key: order_id
    # value: list of rows
    #total = 0
    #for v in list_of_values:
     #   total += v
    orders=[]
    line_items=[]
    for item in list_of_values:
        if item[0] == "order":
            orders.append(item)
        if item[0] == "line_item":
            line_items.append(item)
    for order in orders:
        for line_item in line_items:
            mr.emit(order + line_item)



# Do not modify below this line
# =============================
if __name__ == '__main__':
    inputdata = open(sys.argv[1])
    mr.execute(inputdata, mapper, reducer)
