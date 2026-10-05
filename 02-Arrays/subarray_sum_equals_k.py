class Solution(object):
    def subarraySum(self, nums, k):
        prefix_sum_count = {0: 1}
        current_sum = 0
        count = 0

        for num in nums:
            current_sum += num

            needed = current_sum - k

            if needed in prefix_sum_count:
                count += prefix_sum_count[needed]

            prefix_sum_count[current_sum] = prefix_sum_count.get(current_sum, 0) + 1

        return count