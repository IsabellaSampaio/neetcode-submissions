class Solution {
    fun hasDuplicate(nums: IntArray): Boolean {
        if(nums.isEmpty()) return false 

        if(nums.size == 1) return false

        val isSet = nums.toSet() // temos o nosso set

        if(isSet.toList() == nums.toList()) return false else return true
    }
}
