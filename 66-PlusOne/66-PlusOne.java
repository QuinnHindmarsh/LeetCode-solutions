class Solution {
    public int[] plusOne(int[] digits) {
        int i = digits.length -1;
        boolean changed = false;

        while (i >= 0){
            if (digits[i] == 9){
                digits[i] = 0;
                i--;
            }else{
                digits[i]++;
                changed = true;
                break;
            }
        }

        if (!changed){
           int[] newArr = new int[digits.length + 1];
           newArr[0] = 1;
           
           for (i=0; i < digits.length; i++){
            newArr[i+1] = digits[i];
           }
           return newArr;
        }

        return digits;


    }
}