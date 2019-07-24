from typing import List

# 两数之和
# 使用字典模拟hash
# 在当前索引之前查询 target - curr是否存在
# 时间复杂度O(n)
class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        _dict = {}

        for i, v in enumerate(nums):
            j = _dict.get(target - v)
            if j :
                return [i, j]
            _dict[v] = i


def main():
    list1 = [123, 2, 4, 4]
    target = 6

    print(Solution().twoSum(list1, target))


if __name__ == '__main__':
    main()
