class Solution {
    public int reverse(int n) {
        int reversed_n = 0;

        while (n != 0){
            int digit = n % 10;
            n = n / 10;

            if (reversed_n > (int) Integer.MAX_VALUE / 10 || reversed_n < (int) Integer.MIN_VALUE /10){
                return 0;
            }
            reversed_n = reversed_n * 10 + digit;
        }
        return reversed_n;
    }
}