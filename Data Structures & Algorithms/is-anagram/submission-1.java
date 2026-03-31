class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()) return false;

        HashMap<Character,Integer> mp1 = new HashMap<>();
        HashMap<Character,Integer> mp2 = new HashMap<>();

        for (char c : s.toCharArray()) {
            mp1.put(c, mp1.getOrDefault(c,0) + 1);
        }

        for (char c : t.toCharArray()) {
            mp2.put(c, mp2.getOrDefault(c,0) + 1);
        }


        return mp1.equals(mp2);
    }
}
