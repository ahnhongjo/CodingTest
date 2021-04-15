def solution(a, edges):
    if sum(a)!=0:
        return -1
    if all_zero(a):
        return 0

    tree=[[]for i in range(len(a))]
    parent=[False for i in range(len(a))]

    for i in edges:
        tree[i[0]].append(i[1])
        tree[i[1]].append(i[0])

    queue=[0]
    breadth=[]
    num=0

    while len(queue)!=0:
        tmp_node=queue.pop()
        parent[tmp_node]=True
        next_node=tree[tmp_node]

        for i in next_node:
            if not parent[i]:
                breadth.append((tmp_node,i))
                queue.append(i)

    for i in range(len(breadth)-1,-1,-1):
        pa=breadth[i][0]
        child=breadth[i][1]
        num+=abs(a[child])
        a[pa]+=a[child]
        a[child]=0

    return num

def all_zero(a):
    for i in a:
        if a!=0:
            return False
    return True


solution([-5,0,2,1,2],	[[0,1],[3,4],[2,3],[0,3]])