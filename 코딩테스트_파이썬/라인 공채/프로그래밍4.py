def solution(data, word):
    answer = []
    data_tree=[["root"]]
    for node in data:
        tmp=list(map(str,node.split(" ")))
        if tmp[2]!="0":
            data_tree[int(tmp[2])][2]="NL"
        data_tree.append([tmp[1],int(tmp[2]),"L"])

    for node in data_tree:
        print(node)

    search_list=[]
    for i in range(len(data_tree)):
        if word in data_tree[i][0] and data_tree[i][2]=="L":
            node=data_tree[i]
            search_list.append((i,node[0],node[1]))

    print(search_list)

    if len(search_list)==0:
        return ["Your search for (SALLY) didn't return any results"]

    sorted_search_list=sorted(search_list,key=lambda x:(same(x[1],word),-1*search_num(x[1],word),search_key(x[1],word),x[0]))

    for node in sorted_search_list:
        tmp_answer=node[1]
        root=node[2]
        while root!=0:
            tmp_answer=data_tree[root][0]+"/"+tmp_answer
            root=data_tree[root][1]
        answer.append(tmp_answer)

    print(answer)
    return answer
def same(input_str,word):
    if input_str==word:
        return 0
    else:
        return 1
def search_num(input_str,word):
    res=0
    while word in input_str:
        input_str = input_str.replace(word, "", 1)
        res += 1
    return res

def search_key(input_str,word):
    result=""
    while word in input_str:
        result += str(input_str.find(word))
        input_str = input_str.replace(word, "", 1)
    return result




solution(["1 BROWN 0", "2 CONY 0", "3 DOLL 1", "4 DOLL 2", "5 LARGE-BROWN 3", "6 SMALL-BROWN 3", "7 BLACK-CONY 4", "8 BROWN-CONY 4"],"BROWN")

