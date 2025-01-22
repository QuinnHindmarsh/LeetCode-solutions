class Solution:
    def minimumEffort(self, tasks: List[List[int]]) -> int:
        # Creates a 3rd element in each inner array which represents the difference between the inital energy and cost
        for item in tasks:
            item.append(item[1] - item[0])
        # Sorts by difference
        tasks.sort(key=self.sort_key)

        # Making a prefix array of minimum cost to start from the current point
        tasks[0].append(tasks[0][1])
        for i in range(1, len(tasks)):
            # If the start cost of the current task > cumulitive start cost for previous tasks
            if tasks[i][1] > tasks[i-1][3]:
                tasks[i].append(tasks[i][1])
                # If the start cost for this minus the cost to complete < min start cost for previous 
                if tasks[i][1] - tasks[i][0] < tasks[i-1][3]:
                    # Min cost to start current = min cost to start previous + cost to complete this
                    tasks[i][3] = tasks[i-1][3] + tasks[i][0]
            else:
                # The min cost to start current = min cost to start previous + cost to complete current
                tasks[i].append(tasks[i-1][3])
                tasks[i][3] += tasks[i][0]

        return tasks[-1][3]

    def sort_key(self, e):
        return e[2]
