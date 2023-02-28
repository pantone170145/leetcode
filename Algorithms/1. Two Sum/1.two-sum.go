/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 */

// @lc code=start
func twoSum(nums []int, target int) []int {

	m := make(map[int]int)
	for i, v := range nums {
		answer := target - v
		if _, ok := m[answer]; ok {
			return []int{m[answer], i}
		}

		m[v] = i
	}

	return []int{}
}

// @lc code=end

