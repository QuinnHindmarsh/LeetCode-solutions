// Last updated: 08/07/2025, 16:28:51
class Solution {
public:
    bool hasGroupsSizeX(vector<int>& deck) {
        map <int, int> mp;
        int ans; 
        vector<int> newArr;

        for (int i = 0; i < deck.size(); i++){
            int val = deck[i];
            if (mp.find(val) == mp.end()){
                mp[val] = 0;
            }

            mp[val]++;
  
        }

        for (auto itr = mp.begin(); itr != mp.end(); itr++ ){
            newArr.push_back(itr->second);

        }

        if (newArr.size() == 1){
            return (newArr[0] != 1) ? true : false;
        }

        ans = __gcd(newArr[0], newArr[1]);

        for (int i = 2; i < newArr.size(); i++){
            ans = __gcd(ans, newArr[i]);
        }

        return (ans > 1) ? true : false;

        
    }
};