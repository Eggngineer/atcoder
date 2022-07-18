#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;
    vector<vector<long long>> data(N);

    for (int i = 0;i < N;i++) {
        int x, y, p;
        cin >> x >> y >> p;
        data[i] = { x,y,p };
    }

    vector<vector<long long>> dist(N, vector<long long>(N));
    for (int i = 0;i < N;i++)for (int j = 0;j < N;j++) {
        dist[i][j] = (abs(data[i][0] - data[j][0]) + abs(data[i][1] - data[j][1]) + data[i][2] - 1) / data[i][2];
    }

    for (int k = 0;k < N;k++)for (int i = 0;i < N;i++)for (int j = 0;j < N;j++)dist[i][j] = min(dist[i][j], max(dist[i][k], dist[k][j]));

    long long ans = 1e15;
    for (int i = 0;i < N;i++) {
        long long tans = 0;
        for (int j = 0;j < N;j++)tans = max(tans, dist[i][j]);
        ans = min(ans, tans);
    }
    cout << ans << endl;

    return 0;
}
