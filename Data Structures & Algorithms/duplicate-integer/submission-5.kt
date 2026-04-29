class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        if(nums.isEmpty()) return false 

        if(nums.size == 1) return false

        if(nums.toSet().toList() == nums.toList()) return false else return true
    }
}
