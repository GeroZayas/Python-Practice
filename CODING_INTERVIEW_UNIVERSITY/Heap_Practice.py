class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[self.parent(i)], self.heap[i] = (
                self.heap[i],
                self.heap[self.parent(i)],
            )
            i = self.parent(i)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root

    def heapify_down(self, i):
        left = 2 * i + 1
        right = 2 * i + 2
        smallest = i
        if left < len(self.heap) and self.heap[left] < self.heap[i]:
            smallest = left
        if right < len(self.heap) and self.heap[right] < self.heap(smallest):
            smallest = right
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heapify_down(smallest)


# Example usage:
heap = MinHeap()
heap.insert(3)
heap.insert(2)
heap.insert(1)
print(heap.extract_min())  # Output: 1
print(heap.extract_min())  # Output: 2
print(heap.extract_min())  # Output: 3
