import java.util.*;

class Solution {
    public int solution(String str1, String str2) {
        str1 = str1.toLowerCase();
        str2 = str2.toLowerCase();
        
        ArrayList<String> lst1 = new ArrayList<>();
        ArrayList<String> lst2 = new ArrayList<>();
        
        ArrayList<String> intersection = new ArrayList<>();
        ArrayList<String> union = new ArrayList<>();
        
        for(int i = 0; i < str1.length() - 1; i++){
            char a = str1.charAt(i);
            char b = str1.charAt(i+1);
            
            if (Character.isLetter(a) && Character.isLetter(b)) {
                lst1.add(a + "" + b);
            }
        }
        
        for(int i = 0; i < str2.length() - 1; i++){
            char a = str2.charAt(i);
            char b = str2.charAt(i+1);
            
            if(Character.isLetter(a) && Character.isLetter(b)){
                lst2.add(a + "" + b);
            }
        }
        
        Collections.sort(lst1);
        Collections.sort(lst2);
        
        for(String s : lst1){
            if(lst2.remove(s)){
                intersection.add(s);
            }
            union.add(s);
        }
        
        for(String s : lst2) {
            union.add(s);
        }
        
        double answer = 0;
        if(union.size() == 0){
            answer = 65536;
        } else {
            answer = (double)intersection.size() / (double)union.size() * 65536;
        }
        
        return (int)answer;
    }
}