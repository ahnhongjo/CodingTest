def sol():
    num = int(input())

    for _ in range(num):
        ans = []
        tree_len = int(input())
        bt_pre = list(map(int,input().split()))
        bt_in = list(map(int,input().split()))

        make_post(bt_pre,bt_in,ans)

        for i in ans:
            print(i,end=" ")
        print()

def make_post(bt_pre,bt_in,ans):

    if len(bt_in)==0:
        return
    if len(bt_in) == 1:
        ans.append(bt_in[0])
        return

    root = bt_pre[0]
    root_pos = bt_in.index(root)

    left_in = bt_in[:root_pos]
    right_in = bt_in[root_pos+1:]

    left_pre = bt_pre[1:1+root_pos]
    right_pre = bt_pre[1+root_pos:]

    make_post(left_pre,left_in,ans)
    make_post(right_pre,right_in,ans)
    ans.append(root)

    return


sol()