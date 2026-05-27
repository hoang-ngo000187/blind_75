#include <iostream>
#include<bits/stdc++.h>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> mp;
        int sub = 0;
        
        for(int i = 0; i < nums.size(); i++)
        {
            // Nếu phần bù đã có trong map, ta tìm thấy cặp số
            sub = target - nums[i];
            if (mp.find(sub) != mp.end())
            {
                return {mp[sub], i};
            } 

            // Lưu giá trị hiện tại và chỉ số của nó vào map
            mp[nums[i]] = i;
        }
        return {};
    }
};

int main()
{
    Solution S;
    vector<int> nums = {2,7,11,15};
    int target = 9;
    vector<int> res = S.twoSum(nums, target);
    for (int x : res)
    {
        cout << x << " ";
    }
    cout << endl;
    return 0;
}