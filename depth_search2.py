#深さ優先探索、帰りがけ順
tree = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12], [13, 14], [], [], [], [], [], [], [],[]]

def search(pos):
    for i in tree[pos]:
        search(i)
    print(pos, end=' ')

search(0)