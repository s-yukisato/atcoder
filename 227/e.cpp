#include <iostream>
#include <string>
#include <map>
#include <algorithm>
using namespace std;

int main() {
  int N;
  string S;
  cin >> S >> N;
  string mae = S.substr(0, N), ushi = S.substr(N, N);

  // 後ろ文字列たちから得られる反転ペアたちを作っておく
  map<pair<string,string>, long long > ma;
  for (int bit = 0; bit < (1<<N); ++bit) {
    string a = "", b = "";
    for (int i = 0; i < N; ++i) {
      if (bit & (1<<i)) a += ushi[i];
      else b += ushi[i];
    }
    reverse(a.begin(), a.end());
    reverse(b.begin(), b.end());
    auto p = make_pair(a, b);
    ++ma[p];
  }

  // 前半文字列から作られるペアが後ろにもあるかどうかを判定する
  long long res = 0;
  for (int bit = 0; bit < (1<<N); ++bit) {
    string a = "", b = "";
    for (int i = 0; i < N; ++i) {
      if (bit & (1<<i)) a += mae[i];
      else b += mae[i];
    }
    auto p = make_pair(a, b);
    res += ma[p];
  }

  cout << res << endl;
}