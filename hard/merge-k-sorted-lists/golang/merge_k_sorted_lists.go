package mergeksortedlists

import (
	"container/heap"
)

type MinHeap []int

func (h MinHeap) Len() int           { return len(h) }
func (h MinHeap) Less(i, j int) bool { return h[i] < h[j] }
func (h MinHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *MinHeap) Push(x interface{}) {
	*h = append(*h, x.(int))
}

func (h *MinHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func MergeKSortedLists(lists [][]int) []int {
	var result []int
	minHeap := &MinHeap{}
	heap.Init(minHeap)

	for _, list := range lists {
		for _, num := range list {
			heap.Push(minHeap, num)
		}
	}

	for minHeap.Len() > 0 {
		result = append(result, heap.Pop(minHeap).(int))
	}

	return result
}
