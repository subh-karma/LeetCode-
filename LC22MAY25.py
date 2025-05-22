class Solution {
public:
    static bool cmp(vector<int>&a,vector<int>&b){
        return a[0]<b[0];
    }
    int maxRemoval(vector<int>& nums, vector<vector<int>>& q) {
        sort(q.begin(),q.end(),cmp);
        priority_queue<int>pq;
        int n=nums.size();
        vector<int>temparray(n+1,0);
        int ops=0;
        for(int i=0,j=0;i<n;i++){
            ops+=temparray[i];
            while(j<q.size() and q[j][0]==i){
                pq.push(q[j][1]);
                j++;
            }
            while(ops<nums[i] and !pq.empty() and pq.top()>=i){
                ops+=1;
                temparray[pq.top()+1]-=1;
                pq.pop();
            }
            if(ops<nums[i])return -1;
        }
        return pq.size();
    }
};
