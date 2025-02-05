class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jewl = new HashSet<>();
        int ans = 0;

        for (int i = 0; i < jewels.length(); i++){
            jewl.add(jewels.charAt(i));
        }

        for (int i = 0; i < stones.length(); i++){
            if (jewl.contains(stones.charAt(i))){
                ans ++;
            }
        }
        return ans;

    }
}