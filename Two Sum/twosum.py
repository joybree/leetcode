class Solution:

    """
    ##Bruce Force
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_sorted = sorted(nums)
        #print(nums_sorted)
        part1_list = list(filter(lambda x:x <  target/2, nums_sorted))
        part2_list = list(filter(lambda x:x >= target/2, nums_sorted))
        indices = []
        #print(part1_list)
        #print(part2_list)
        indices_equal = [indice for indice,value in enumerate(nums) if value == target/2]
        #print(indices_equal)
        if len(indices_equal) ==2:
            return indices_equal
        else:
            for item in part1_list:
                val1 = target - item
                if val1 in part2_list:
                    indices = [nums.index(item),nums.index(val1)]
                    return indices
    

    """
    ##Hash Function
    """
    def twoSum1(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i


if __name__ == "__main__":
    Solution1 = Solution()
    indices = Solution1.twoSum1([-3,-6,3,3,-90], 6)
    print(indices)