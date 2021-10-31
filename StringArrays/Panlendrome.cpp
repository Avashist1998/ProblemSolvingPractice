#include <string>
#include <array>
#include <iostream>
using namespace std;


bool Panlendrome(string word){

    int map[26] = {0};
    int spaceCounter = 0;
    for (int i =0; i < word.length(); ++i){
        int index = (int)word[i];
        if (word[i] != ' '){
            if (index < (int)'Z' && index > (int)'A'){
                index += 32;
            }
            map[index - 97]++;
        }
        else if (word[i] == 'i'){
            spaceCounter++;
        }
    }
    if (word.length()+spaceCounter%2 == 0){
        // ever case
        for(int i = 0; i <26; ++i){
            if(map[i]%2 == 1){
                return false;
            }
        }
        return true;
    }
    else{
        //odd case
        bool odd1 = false;
        for(int i = 0; i <26; ++i){
            if(map[i]%2 == 1)
            {
                if (odd1){
                    return false;
                }
                odd1 = true;
            }
        }
        return true;
    }
         
}
