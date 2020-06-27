import java.util.Arrays;
public class UniqueString {

   public static boolean UniqueStringChecker(char[] words) {
      Boolean[] charSet = new Boolean[128];
      Arrays.fill(charSet, false);
      boolean checker = false;
      int charVal = 0;
      for (char word : words) {
         charVal = word;
         if (charSet[charVal]) {
            checker = true;
         }
         charSet[charVal] = true;
      }
      return checker;
   }

   public static void main(String[] args) {
      String str = "works";
      String str2 = "does not work";
      char[] strArray = str.toCharArray();
      char[] str2Array = str2.toCharArray();
      System.out.println("The result of the string 1 : " + UniqueStringChecker(strArray));
      System.out.println("The result of the string 2 : " + UniqueStringChecker(str2Array));
   }
}