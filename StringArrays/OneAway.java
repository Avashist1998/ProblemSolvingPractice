public class OneAway{
    OneAway(){

    }

    int absVal(int val){
        val = (val <0) ? -1*val : val;
        return val;
    }
    boolean Oneoff(char[] wordA, char[] wordB){
        int offCount = 0;
        for (int i =0; i<wordA.length;++i){
            if (wordA[i] != wordB[i]) offCount++;
            if (offCount > 1) return false;
        }
        return true;
    }
    boolean MissExtra(char[] wordA, char[] wordB){
        int offCount = 0;
        boolean output = false;
        int j =0;
        
        for (int i =0; i < wordA.length; ++i){
            if (wordA[i] != wordB[j]) {offCount++; j++;}
            output = (offCount<2)? true : false;
            ++j;
            if (j > wordB.length-1) j--;
            if (offCount>1) j--;
        }
        return output;

    }
    public boolean oneaway(String wordA, String wordB){
        boolean output = false;
        int sizeA = wordA.length();
        int sizeB = wordB.length();
        char[] wordAarray  = wordA.toCharArray();
        char[] wordBarray  = wordB.toCharArray();
        //System.out.println(wordAarray.length);
        //System.out.println(wordBarray.length);
        if (absVal(sizeA - sizeB) <= 1){
            if (sizeA == sizeB) output = Oneoff(wordAarray, wordBarray);
            else if (sizeA > sizeB) output = MissExtra(wordAarray, wordBarray);
            else  output = MissExtra(wordBarray, wordAarray);
            return output;
        }
        else return output;
    }
    public static void main(String[] args) {
        String Original = "original";
        String OneOff = "originat";
        String OneMiss = "origina";
        String OneExtra = "originals";
        String twoOff = "orignal";
        OneAway myObj = new OneAway();
        System.out.println("The results of "+Original+ " and "+OneOff+": "+myObj.oneaway(Original,OneOff));
        System.out.println("The results of "+Original+ " and "+OneMiss+": "+myObj.oneaway(Original,OneMiss));
        System.out.println("The results of "+Original+ " and "+OneExtra+": "+myObj.oneaway(Original,OneExtra));
        System.out.println("The results of "+Original+ " and "+twoOff+": "+myObj.oneaway(Original,twoOff));
    }
    
}