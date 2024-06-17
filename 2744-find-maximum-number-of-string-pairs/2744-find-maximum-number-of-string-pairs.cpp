class Solution {
public:
    int maximumNumberOfStringPairs(vector<string>& words) {
        int c=0;
        unordered_map<string, int> mp;
        for(auto w: words){
            string r=w;
            reverse(r.begin(), r.end());
            if (mp[r]>0){
                c++;
                mp[r]--;
            }
            else mp[w]++;
        }
        return c;
    }
};