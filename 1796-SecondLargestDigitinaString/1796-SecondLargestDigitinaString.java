class Solution {
    public int secondHighest(String s) {
        int max = -1;
        int max2  = -1;

        for (int i = 0; i < s.length(); i++){
            if (Character.isDigit(s.charAt(i))){
                int val = Character.getNumericValue(s.charAt(i));
                if (max < val){
                    max2 = max;
                    max = val;
                } else if (max2 < val && max != val){
                    max2 = val;
                }
            }
        }      
        return max2; 
    }
}