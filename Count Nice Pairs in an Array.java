import java.util.HashMap;
import java.util.Map;

class Solution {
    public int countNicePairs(int[] nums) {
        final int MOD = 1000000007;
        int count = 0;

        // Map to store the frequency of the difference between each element and its reverse
        Map<Integer, Integer> freqMap = new HashMap<>();

        for (int num : nums) {
            int diff = num - reverse(num);
            freqMap.put(diff, freqMap.getOrDefault(diff, 0) + 1);
        }

        for (int freq : freqMap.values()) {
            // If there are 'n' occurrences of a difference, there are n*(n-1)/2 nice pairs with that difference
            count = (int) ((count + (long) freq * (freq - 1) / 2) % MOD);
        }

        return count;
    }

    // Helper function to reverse an integer
    private int reverse(int num) {
        int rev = 0;
        while (num > 0) {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        return rev;
    }
}
