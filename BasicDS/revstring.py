from pythonds.basic.stack import Stack

def revstring(mystr):
    s = Stack()
    res = []
    for l in mystr:
        s.push(l)
    while not s.isEmpty():
        res.append(s.pop())

    return ''.join(res)
