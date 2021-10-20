#include <bits/stdc++.h>
using namespace std;
 
int main(){
    int N, M;
    cin >> N >> M;
    vector<tuple<int, int, int>> pts;
    for(int i=0; i<M; i++){
        int x, y;
        cin >> x >> y;
        pts.emplace_back(x, 0, 0);
        pts.emplace_back(y, 1, 1);
    }
    // x座標でソート
    sort(pts.begin(), pts.end());
 
    // ペア待ち点のy座標の集合
    set<int> st;
    int ans = 0;
    for(auto& [x, y, c] : pts){
        if(c == 0){
            st.insert(y);
        }else{
            auto it = st.lower_bound(y);
            if(it != st.begin()){
                st.erase(prev(it));
                ans++;
            }
        }
    }
    cout << ans << endl;
    return 0;
}