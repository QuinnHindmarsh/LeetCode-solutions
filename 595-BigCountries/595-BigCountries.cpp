// Last updated: 17/07/2025, 13:54:27
class Solution {
public:
    int maxFreqSum(string s) {
        map<char, int> vowel_freq;
        map<char, int> const_freq; 
        set<char> vowels;
        int mx_vowel = 0;
        int mx_const = 0;
        
        vowels.insert('a');
        vowels.insert('e');
        vowels.insert('i');
        vowels.insert('o');
        vowels.insert('u');


        for (int i = 0; i < s.length(); i++){
            char l = s[i];

            if(vowels.find(l) != vowels.end()){
                if (vowel_freq.find(l) == vowel_freq.end()){
                    vowel_freq[l] =0;
                }
                
                vowel_freq[l]++;
            }else{
                if (const_freq.find(l) == const_freq.end()){
                    const_freq[l] =0;
                } 
                const_freq[l]++;
            }
        }


        for (auto itr = vowel_freq.begin(); itr != vowel_freq.end(); itr++){
            mx_vowel = max(mx_vowel, itr->second);
        }

        for (auto itr = const_freq.begin(); itr != const_freq.end(); itr++){
            mx_const = max(mx_const, itr->second);
        }

        return mx_vowel + mx_const;
    }
};