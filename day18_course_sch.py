class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        dependency = defaultdict(list)
        child = defaultdict(list)

        order = deque()
        oSet = set()

        for a, b in prerequisites:
            dependency[a].append(b)
            child[b].append(a)

        root = []
        for i in range(numCourses):
            if dependency[i] == []:
                root.append(i)

        print(dependency)
        print(child)

        queue = deque(root)
        queueSet = set(root)
        end = 0
        count = 10
        while queue and end == 0 and count:
            # print('Loop',list(queue))
            # count -= 1
            head = queue[0]
            if head not in oSet:
                if dependency[head] == [] or all([i in oSet for i in dependency[head]]):
                    print(f'all {head}', all(
                        [i in oSet for i in dependency[head]]))

                    oSet.add(head)
                    order.append(head)

                    queue.popleft()
                    queueSet.remove(head)
                    for i in child[head]:
                        if i not in queueSet:
                            queue.append(i)
                            queueSet.add(i)
                    if len(oSet) == numCourses:
                        end = 1
                else:
                    queue.popleft()
                    queueSet.remove(head)
            else:
                print('hit')
                queue.popleft()
                queueSet.remove(head)
        if len(order) != numCourses:
            return []
        return list(order)
