// Last updated: 24/03/2026, 12:34:57
1class Solution {
2public:
3    int countStudents(vector<int>& students, vector<int>& sandwiches) {
4        queue<int> q;
5        for (int pref : students) {
6            q.push(pref);
7        }
8
9        int top = 0;
10        int rotations = 0;
11
12        while (!q.empty() && rotations < static_cast<int>(q.size())) {
13            if (q.front() == sandwiches[top]) {
14                q.pop();
15                top++;
16                rotations = 0;
17            } else {
18                q.push(q.front());
19                q.pop();
20                rotations++;
21            }
22        }
23
24        return static_cast<int>(q.size());
25    }
26};