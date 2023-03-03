class Solution:

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        self.cache = {}
        result = []

        # i番目の要素を除いたリストを作成し、
        # そのリストの要素の積を計算する
        for i, n in enumerate(nums):
            nums_without_i = nums[:i] + nums[i + 1:]
            result.append( self.memoize(nums_without_i))

        return result

    def memoize(self, nums: List[int]) -> int:
        # convert list to string
        str_nums = [str(n) for n in nums]

        # concatenate strings with '-' nums
        key = '-'.join(str_nums)
        print(f'key: {key}')

        # キャッシュにkeyが存在するか
        if key in self.cache:
            return self.cache[key]

        # numsが>=2の場合、計算しキャッシュに保持する
        if len(nums) >= 2:
            self.cache[key] = self.memoize(nums[1:]) * nums[0]
            return self.cache[key]

        # numsが1の場合、キャッシュに保持する
        self.cache[key] = nums[0]
        return self.cache[key]
