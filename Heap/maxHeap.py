class Maxheap:
    def __init__(self) -> None:
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self.__swim(len(self.heap) - 1)

    def extrack_max(self):
        value = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self.__sink(0)
        return value

    def __sink(self, k):
        while (2*k + 1 < len(self.heap)):
            j = 2*k + 1
            if (2*k + 2 < len(self.heap) and self.heap[2*k + 2] > self.heap[2*k + 1]):
                j = 2*k + 2
            if self.heap[j] > self.heap[k]:
                self.__swap(j, k)
            k = j

    def __swim(self, k):
        while k > 0 and self.heap[(k - 1)//2] < self.heap[k]:
            self.__swap((k - 1) // 2, k)
            k = (k - 1) // 2

    def __swap(self, j, k):
        tmp = self.heap[j]
        self.heap[j] = self.heap[k]
        self.heap[k] = tmp


if __name__ == '__main__':
    hp = Maxheap()
    hp.insert(1)
    hp.insert(2)
    hp.insert(3)
    hp.insert(4)
    hp.insert(5)
    print(hp.heap)
    hp.extrack_max()
    print(hp.heap)
