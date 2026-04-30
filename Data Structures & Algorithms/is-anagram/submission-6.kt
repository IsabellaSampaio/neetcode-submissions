class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        if(s.isEmpty() || t.isEmpty()) return true
        if(s.length != t.length ) return false

        val hashMapS = hashMapOf<Char, Int>()
        val hashMapT = hashMapOf<Char, Int>()

        for (c in s) {
            if(!hashMapS.containsKey(c)) {
                hashMapS[c] = 0
            } else {
                hashMapS[c] = 1
            }
        }

        for(c in t) {
            if(!hashMapT.containsKey(c)) {
                hashMapT[c] = 0
            } else {
                hashMapT[c] = 1
            }
        }

        if(hashMapS == hashMapT) return true else return false
    }
}
