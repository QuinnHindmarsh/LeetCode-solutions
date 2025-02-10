class Solution {
    public char kthCharacter(int k) {
        int level = 0;
        // founds the multiple of 2 
        while ((1 << level) <= k) {  
            level++;
        }
        k--;
        
        char ch = 'a'; // Start with 'a'
        
        while (level > 0) {
            int mid = (1 << (level - 1)); // Find midpoint
            if (k >= mid) {
                k -= mid; // Move to second half
                ch = (ch != 'z') ? (char) (ch +1) : 'a';
            }
            level--;
        }
        
        return ch;
    }
}
