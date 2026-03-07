# Last updated: 07/03/2026, 14:07:08
1class Solution:
2    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
3        def format_line(maxWidth, current_line, running_count_of_charathers, is_last_line):
4            formatted_line = []
5            num_gaps = len(current_line) - 1  # gaps between words
6
7            if is_last_line or num_gaps == 0:
8                # Left-justified: single spaces between words, pad end
9                line = ' '.join(current_line)
10                formatted_line = line + ' ' * (maxWidth - len(line))
11            else:
12                total_spaces = maxWidth - running_count_of_charathers
13                space_per_gap = total_spaces // num_gaps
14                extra_spaces = total_spaces % num_gaps  # distributed left to right
15
16                for i, word in enumerate(current_line):
17                    formatted_line.append(word)
18                    if i < num_gaps:  # don't add spaces after the last word
19                        spaces = space_per_gap + (1 if i < extra_spaces else 0)
20                        formatted_line.append(' ' * spaces)
21
22                formatted_line = ''.join(formatted_line)
23
24            return formatted_line
25
26        current_line = []
27        running_count_of_chars = 0
28        current_output = []
29
30        for i, word in enumerate(words):
31            # +len(current_line) accounts for the minimum 1 space between words
32            if running_count_of_chars + len(current_line) + len(word) <= maxWidth:
33                running_count_of_chars += len(word)
34                current_line.append(word)
35            else:
36                current_output.append(format_line(maxWidth, current_line, running_count_of_chars, False))
37                running_count_of_chars = len(word)
38                current_line = [word]
39
40        # Last line
41        current_output.append(format_line(maxWidth, current_line, running_count_of_chars, True))
42
43        return current_output
44
45
46
47
48
49