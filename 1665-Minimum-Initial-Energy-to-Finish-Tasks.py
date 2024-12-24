"""
1665. Minimum Initial Energy to Finish Tasks
https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/description/

You are given an array tasks where tasks[i] = [actuali, minimumi]:

actuali is the actual amount of energy you spend to finish the ith task.
minimumi is the minimum amount of energy you require to begin the ith task.
For example, if the task is [10, 12] and your current energy is 11, you cannot start this task. However, if your current energy is 13, you can complete this task, and your energy will be 3 after finishing it.

You can finish the tasks in any order you like.

Return the minimum initial amount of energy you will need to finish all the tasks.

"""


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


# My solution
# https://leetcode.com/problems/minimum-initial-energy-to-finish-tasks/solutions/6179555/dp-greedy-sort-by-quinnhindmarsh-52h1/
"""
Complexity
Time complexity:
O(nlogn)

itterate over the array O(n)
sorting O(n log n)
itterate over the array again O(n)
Space complexity:
O(n)
a constant amount of data is being stored for each element O(n)
"""
