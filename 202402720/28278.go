package main

import "container/list"

type Stack struct {
	v *list.List
}

func NewStack() *Stack {
	return &Stack{list.New()}
}

func (q *Stack) Push(v interface{}) {
	q.v.PushBack(v)
}

func (q *Stack) Pop() interface{} {
	back := q.v.Back()
	if back == nil {
		return nil
	}

	return q.v.Remove(back)
}

func (q *Stack) Top() interface{} {
	return q.v.Back()
}

func main() {
}
