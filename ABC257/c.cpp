#include<bits/stdc++.h>
using namespace std;

int main() {
    int n, x, ans;
    string s;
    vector<pair<int, int>> w;

    cin >> n;
    cin >> s;
    ans = 0;
    for (int i = 0;i < n;i++) {
        cin >> x;
        w.push_back({ x,s[i] });
        if (s[i] == '1')ans++;
    }

    sort(w.begin(), w.end());
    x = ans;
    for (int i = 0; i < n; i++) {
        if (w[i].second == '1')x--;
        else x++;

        if (i < n - 1) {
            if (w[i].first != w[i + 1].first) ans = max(ans, x);
        }
        else ans = max(ans, x);
    }

    cout << ans << endl;
    return 0;
}

