#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int romanToInt(string s) {
        unordered_map<char,int> romanValue = {
            {'I',1},{'V',5},{'X',10},{'L',50},
            {'C',100},{'D',500},{'M',1000}
        };
        int result=0;
        for(int i=0;i<s.size();i++){
            if(i+1<s.size() && romanValue[s[i]]<romanValue[s[i+1]]) result-=romanValue[s[i]];
            else result+=romanValue[s[i]];
        }
        return result;
    }
};

int main(){
    Solution sol;
    cout<<sol.romanToInt("III")<<endl;
    return 0;
}

