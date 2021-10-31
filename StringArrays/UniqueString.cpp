#include <string>
#include <array>
#include <iostream>
using namespace std;

bool isUnique(string word){
    bool set[128] = {false};
    for (int i = 0; i<word.length(); ++i){
        int index = (int)word[i];
        if(set[index]){
            return false;
        }
        set[index] = true;

    }
    return true;
}

int main(){
    string str = "works";
    string str2 = "does not work";
    cout<<"The result of the \""<<str<<"\" : "<< isUnique(str)<<endl;
    cout<<"The result of the \""<<str2<<"\" : "<< isUnique(str2)<<endl;
}