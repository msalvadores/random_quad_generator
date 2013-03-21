import random

RESOURCE_SPACE = 50000
GRAPH_SPACE = 500
PREDICATE_SPACE = 500
LITERAL_LENGTH_MAX = 50

def get_random_graph():
    return "<http://foo.com/bar/graph/%s>"%random.randint(0,GRAPH_SPACE)
def get_random_res():
    return "<http://foo.com/bar/resource/%s>"%random.randint(0,RESOURCE_SPACE)
def get_random_pred():
    return "<http://foo.com/bar/predicate/%s>"%random.randint(0,PREDICATE_SPACE)
def get_random_lit():
    t = random.randint(0,5)
    if t < 3:
        length = random.randint(5,LITERAL_LENGTH_MAX)
        l = []
        for x in range(length):
            l.append(chr(random.randint(32,100)))
        return "\"%s\""%(''.join(l).replace('"','').replace("\\",'').replace("<",'').replace(">",''))
    if t < 5:
        i = random.randint(10,1000)
        return "\"%s\"^^<http://www.w3.org/2001/XMLSchema#integer>"%i
    if t < 6:
        date = "%s-%s-%sT00:00:00Z"%(random.randint(1999,2010),random.randint(1,12),random.randint(1,28))
        return "\"%s\"^^<http://www.w3.org/2001/XMLSchema#dateTime>"%date

def get_random_object():
    x = random.randint(0,1)
    if x < 1:
        return get_random_res()
    return get_random_lit()


for x in range(int(1e6)):
    quad = [  get_random_res(), get_random_pred() ,get_random_object() , get_random_graph(), "."]
    print " ".join(quad)


