// Last updated: 17/07/2025, 12:13:00
class Solution {
public:
    int largestInteger(int num) {
        vector<int> odd;
        vector<int> even;
        vector<bool> odd_mask; 
        long long n = 0; 

        while (num > 0){
            int digit = num % 10; 
            num /= 10; 

            if (digit & 1){ 
                odd.push_back(digit);
                odd_mask.push_back(true);
            } else{
                even.push_back(digit);
                odd_mask.push_back(false);
            }
        }

        make_heap(odd.begin(), odd.end()); 
        make_heap(even.begin(), even.end());

        for (int i = odd_mask.size() -1; i >= 0 ; i--){
            n *= 10; 
            int digit = 0; 

            if (odd_mask[i]){
                digit = odd.front();
                pop_heap(odd.begin(), odd.end());
                odd.pop_back();
            } else{
                digit = even.front();
                pop_heap(even.begin(), even.end());
                even.pop_back();
            }

            n += digit;

        }


        return n;

    }
};