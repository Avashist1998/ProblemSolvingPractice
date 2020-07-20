public class StringRotation {
    
    public static boolean isSubstring(String word1, String word2){
        boolean output = true;
        int index = 0;
        for (int i = 0; i<word1.length(); ++i){
            if(word1.charAt(i) == word2.charAt(0)) {index = i; break;}
        }
        for (int i = index; i<index+word2.length(); ++i){
            if (word2.charAt(i-index) != word1.charAt(i)) output = false;
        }
        return output;
    }
    
    public static String StringMaker (String word, int index){
        int size = word.length();
        String wordnew = Character.toString(word.charAt(index));
        for (int i = index+1; i< size; ++i){
            wordnew+= Character.toString(word.charAt(i));
        }
        for (int i = 0; i< index; ++i){
            wordnew+= Character.toString(word.charAt(i));
        }
        return wordnew;
    }
    public static boolean isStringRotated(String word1, String word2){
        boolean check = false;
        if (word1.length() == word2.length()){
            String wordnew = word1 + word1;
            return isSubstring(wordnew,word2);
        }
        return check;
    }

    public static void main(String[] args){
        String worda = "testforyou";
        String wordb = "youtestfor";
        String wordc = "youtestfou";
        System.out.println("The results of the \""+worda+"\" and \" "+wordb+" \" : "+ isStringRotated(worda, wordb));
        System.out.println("The results of the \""+worda+"\" and \" "+wordc+" \" : "+ isStringRotated(worda, wordc)); 
    }
}