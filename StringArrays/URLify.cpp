#include <string>
#include <array>
#include <iostream>
#include <vector>
using namespace std;


void URLify(string word, int size){
    vector<int> spaceIndex;
    for (int i =0; i<size; ++i){
        if(word[i] == ' ')
        {
            spaceIndex.push_back(i);
        }
        
    }
    int numOfSpace = spaceIndex.size();
    int k = size - 1 +numOfSpace*2;
    for (int i =size-1; i>=0; --i){
        if (word[i] == ' '){
            word[k] = '%';
            word[k-1] = '2';
            word[k-2] = '0'; 
            k-=3;
        }
        else{
            word[k] = word[i]; 
            k--;
        }
    }
}