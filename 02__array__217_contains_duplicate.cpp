#include <iostream>
#include<bits/stdc++.h>
#include <algorithm>

using namespace std;

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set <int> s;

        for(int num: nums)
        {
            if(s.find(num) != s.end())
            {
                return true;
            }
            s.insert(num);
        }

        return false;
    }
};

int main()
{
    Solution S;
    vector<int> nums = {1, 2, 7, 20, 5, 6, 7, 8};
    bool res = S.containsDuplicate(nums);
    cout << res;
    
    return 0;
}