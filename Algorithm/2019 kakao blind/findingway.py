def solution(nodeinfo):
    import sys
    sys.setrecursionlimit(2000)

    class Node(object):
        def __init__(self, data):
            self.n = data[1]
            self.x = data[0][0]
            self.y = data[0][1]
            self.l = self.r = None
    
    def build(node, child):
        lchild = []
        rchild = []
        for c in child:
            if c[0][0] < node.x: lchild.append(c)
            elif c[0][0] > node.x: rchild.append(c)
        if lchild != []:
            node.l = Node(lchild[0])
            build(node.l, lchild)
        if rchild != []:
            node.r = Node(rchild[0])
            build(node.r, rchild)
    
    def pre(node):
        ret = [node.n]
        if node.l != None: ret += pre(node.l)
        if node.r != None: ret += pre(node.r)
        return ret

    def post(node):
        ret = []
        if node.l != None: ret += post(node.l)
        if node.r != None: ret += post(node.r)
        ret += [node.n]
        return ret

    nodeinfo = [(nodeinfo[i], i+1) for i in range(len(nodeinfo))]
    nodeinfo.sort(key=lambda x:(-x[0][1], x[0][0]))
    tree = Node(nodeinfo[0])
    build(tree, nodeinfo)

    return [pre(tree), post(tree)]
    
a = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

if __name__=='__main__':
    print(solution(a))