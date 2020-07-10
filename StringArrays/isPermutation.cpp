#include <string>
#include <array>
#include <iostream>
using namespace std;


bool isPremutation(string word1, string word2){
    if (word1.length() == word2.length()){
        int set1[128] = {0};
        int set2[128] = {0};
        for(int i =0; i<word1.length();++i){
            set1[(int)word1[i]]++;
            set2[(int)word2[i]]++;
        }
        for (int i =0; i<128; ++i){
            if (set1[i] != set2[i]){
                return false;
            }
        }
        return true;
    }
    else {
        return false;
    }  
}