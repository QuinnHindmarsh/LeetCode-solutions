class Solution {
    public int maxPoints(int[][] points) {
        int res = 0;

        for (int i = 0; i < points.length; i ++){
            res = Math.max(res, maxPointsFromFocalPoint(i, points));
        }

        return res;
    }

    public int maxPointsFromFocalPoint(int focal_point_index, int[][] points) {
        Map<String, Integer> slopes_map = new HashMap<>();
        int maxPoints = 0;

        for (int j = 0; j < points.length; j++) {
            if (j != focal_point_index) {
                int[] cur_slope = get_slope(points[focal_point_index], points[j]);
                String slopeKey = cur_slope[0] + "," + cur_slope[1];
                
                slopes_map.put(slopeKey, slopes_map.getOrDefault(slopeKey, 0) + 1);
                maxPoints = Math.max(maxPoints, slopes_map.get(slopeKey));
            }
        }

        return maxPoints + 1;
    }

    public int[] get_slope(int[] p1, int[] p2){
        int rise = p2[1] - p1[1];
        int run = p2[0] -p1[0];

        if (run == 0){
            return new int[]{1, 0};
        } 
        int gcd_val = gcd(rise, run);
        return new int[]{rise / gcd_val, run / gcd_val};

    }


    public int gcd(int a, int b) {
        while (b != 0) {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}