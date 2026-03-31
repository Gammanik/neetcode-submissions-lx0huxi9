class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> mp = new HashMap<>();

        for (int i = 0; i < nums.length; i++) {
            int ti = target - nums[i];
            if (mp.containsKey(ti)) {
                return new int[] { mp.get(ti), i};
            }

            mp.put(nums[i], i);
        }

        return new int[] { -1, -1 };
    }
}
