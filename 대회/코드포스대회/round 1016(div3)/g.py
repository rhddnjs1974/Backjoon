import sys
input = sys.stdin.readline

class TrieNode:
    def __init__(self):
        self.children = [None, None]
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, x):
        node = self.root
        for i in reversed(range(31)):
            b = (x >> i) & 1
            if not node.children[b]:
                node.children[b] = TrieNode()
            node = node.children[b]
            node.count += 1

    def erase(self, x):
        node = self.root
        for i in reversed(range(31)):
            b = (x >> i) & 1
            node = node.children[b]
            node.count -= 1

    def max_xor(self, x):
        node = self.root
        res = 0
        for i in reversed(range(31)):
            b = (x >> i) & 1
            if node.children[1 - b] and node.children[1 - b].count > 0:
                res |= (1 << i)
                node = node.children[1 - b]
            elif node.children[b] and node.children[b].count > 0:
                node = node.children[b]
            else:
                break
        return res

def check(a, k, L):
    trie = Trie()
    for i in range(L):
        trie.insert(a[i])
    for i in range(L):
        if trie.max_xor(a[i]) >= k:
            return True
    for i in range(L, len(a)):
        trie.erase(a[i - L])
        trie.insert(a[i])
        if trie.max_xor(a[i]) >= k:
            return True
    return False

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    
    if k == 0:
        print(1)
    else:
        l, r = 2, n
        ans = -1
        while l <= r:
            mid = (l + r) // 2
            if check(a, k, mid):
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        print(ans)