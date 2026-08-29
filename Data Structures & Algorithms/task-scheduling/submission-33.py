class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = [0] * 26

        for t in tasks:
            freqs[ord(t) - ord('A')] -= 1

        heap = []
        for f in freqs:
            if f != 0:
                heapq.heappush(heap, [0, f])

        # key breakthru -> dont update ALL CDs each cycle fot each task
        # instead, store a static value.. whats this? the time the task can NEXT RUN
        cycle = 0
        cooldown = []
        while heap or cooldown:
            cycle += 1
            if cooldown and cooldown[0][0] <= cycle:
                task = heapq.heappop(cooldown)
                task[0] = 0
                heapq.heappush(heap, task)
            if heap:
                task = heapq.heappop(heap)
            else:
                task = heapq.heappop(cooldown)
            if task[0] > cycle: # All tasks on CD. Assign cycle to lowest CD element's next processing time
                cycle = task[0]

            task[0] = cycle + n + 1 # Next run
            task[1] += 1 # Process task, lower freq
            if task[1] != 0: # If task has freq = 0, we are done with it
                heapq.heappush(cooldown, task)

        return cycle


        