class Solution {
    fun isAnagram(s: String, t: String): Boolean {
        val hashMapS = hashMapOf<Char, Int>()
        val hashMapT = hashMapOf<Char, Int>()

        if(s.isEmpty() || t.isEmpty()) return true
        if(s.length != t.length ) return false

        for (c in s) {
            var counterS = 0
            if(!hashMapS.containsKey(c)) {
                hashMapS[c] = counterS
            } else {
                counterS+=1
                hashMapS[c] = counterS
            }
        }

        for(c in t) {
            var counterT = 0
            if(!hashMapT.containsKey(c)) {
                hashMapT[c] = counterT
            } else {
                counterT+=1
                hashMapT[c] = counterT
            }
        }

        if(hashMapS == hashMapT) {
            println("is true $hashMapS $hashMapT")
            return true 
        } else {
            println("is false $hashMapS $hashMapT")
            return false
        }
    }
}
