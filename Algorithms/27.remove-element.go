/*
 * @lc app=leetcode id=27 lang=golang
 *
 * [27] Remove Element
 */

// @lc code=start
func removeElement(nums []int, val int) int {
	l := len(nums)
	if l == 0 {
		return 0
	}

	x := 0
	for i := 0; i < l; i++ {
		if nums[i] != val {
			nums[x] = nums[i]
			x++
		}
	}

	return x
}

// @lc code=end

