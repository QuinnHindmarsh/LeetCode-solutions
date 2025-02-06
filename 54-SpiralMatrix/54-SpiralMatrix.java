class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        List<Integer> result = new ArrayList<>();
        int top = 0, bottom = matrix.length - 1;
        int left = 0, right = matrix[0].length - 1;
        int i = 0;


        if (matrix == null || matrix.length == 0){
            return result;
        }

        while (top <= bottom && left <= right){
            for (i = left; i < right+1; i++){
                result.add(matrix[top][i]);
            }
            top ++;
            
            for (i=top;i < bottom +1; i ++){
                result.add(matrix[i][right]);
            }
            right --;

            if (top <= bottom){
                for (i = right; i > left -1; i--){
                    result.add(matrix[bottom][i]);
                }
                bottom --;
            }

            if (left <= right){
                for (i=bottom; i > top -1; i--){
                    result.add(matrix[i][left]);
                }
                left ++;
            }
        }

        return result;
    }
}