/*
 * @lc app=leetcode id=28 lang=golang
 *
 * [28] Implement strStr()
 */

// @lc code=start
func strStr(haystack string, needle string) int {
	if needle == "" {
		return 0
	}
	return strings.Index(haystack, needle)

	// // haystackの長さ
	// hl := len(haystack)
	// nl := len(needle)

	// for i := 0; i < (hl - nl + 1) i++ {

	// }

	// return -1
}

// @lc code=end

