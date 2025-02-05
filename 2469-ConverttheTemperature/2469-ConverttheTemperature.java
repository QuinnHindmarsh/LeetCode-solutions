class Solution {
    public double[] convertTemperature(double c) {
        double[] ans = new double[2];

        ans[0] = c + 273.15;
        ans[1] = c * 1.8 + 32;

        return ans;
    }
}