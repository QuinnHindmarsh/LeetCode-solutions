class RandomizedSet {


    private ArrayList<Integer> vals;
    private HashMap<Integer, Integer> map;
    private Random rand;    

    public RandomizedSet() {
        vals = new ArrayList<>();
        map = new HashMap<>();
        rand = new Random();
    }
    
    public boolean insert(int val) {
        if (!map.containsKey(val)){
            vals.add(val);
            map.put(val, vals.size() -1);
            return true;
        }
        return false;
    }
    
    public boolean remove(int val) {
        if (map.containsKey(val)){
            int idx = map.get(val);
            int lastVal = vals.get(vals.size() - 1);
            map.put(lastVal, idx);

            vals.set(idx, lastVal);
            
            vals.remove(vals.size() - 1);
            map.remove(val);

            return true;
        }
        return false;
    }
    
    public int getRandom() {
        int randIdx = rand.nextInt(vals.size());
        return vals.get(randIdx);
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */