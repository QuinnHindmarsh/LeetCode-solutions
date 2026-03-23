// Last updated: 23/03/2026, 20:15:05
1class Solution {
2public:
3    string sortSentence(string s) {
4        vector<string> arr;
5        stringstream ss(s);
6        string word;
7        while (ss >> word) arr.push_back(word);
8
9        vector<string> result(arr.size());
10        for (const auto& w : arr) {
11            int pos = w.back() - '1';
12            result[pos] = w.substr(0, w.size() - 1);
13        }
14
15        string out;
16        for (int i = 0; i < result.size(); i++) {
17            if (i) out += ' ';
18            out += result[i];
19        }
20        return out;
21    }
22};