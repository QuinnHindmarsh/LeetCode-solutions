class Solution {
    public double[] convertTemperature(double c) {
        double[] ans = new double[] {c + 273.15, c * 1.80 + 32.00};

        return ans;
    }
}