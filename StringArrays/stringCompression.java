public class stringCompression {
    stringCompression(){
    }
    public int getCount(String word, int index){
        int count = 1;
        int i = index +1;
        while(i < word.length() && word.charAt(i) == word.charAt(index) )
        {
            i++;
            count++;
        }
        return count;
    }
    String compress(String word){
        String compressWord = "";
        for (int i = 0; i<word.length(); ++i){
            compressWord+= word.charAt(i);
            int val = getCount(word, i);
            if (val > 1) {
                char[] count = ("" + val).toCharArray();
                for (char c : count){
                    compressWord += c;
                }
            }
            i+= val -1;
        }
        return compressWord;    
    }
    
    
    public static void main(String[] args) {
        String wordA = "aaabbbaac";
        String wordB = "abcdefgh";
        String wordC = "aaabccaabb";
        stringCompression myObj = new stringCompression();
        System.out.println("test");
        System.out.println("The string : " + wordA + " is compressed to : " + myObj.compress(wordA));
        System.out.println("The string : " + wordB + " is compressed to : " + myObj.compress(wordB));
        System.out.println("The string : " + wordC + " is compressed to : " + myObj.compress(wordC));
    }
}