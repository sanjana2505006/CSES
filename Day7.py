using namespace std;

void solve() {
    int t;
    cin >> t;
    while (t--) {
        long long y, x;
        cin >> y >> x;

        long long layer = max(y, x);
        long long layer_start = (layer - 1) * (layer - 1);
        long long result;

        if (layer % 2 == 0) {
            if (x == layer) {
                result = layer_start + y;
            } else {
                result = layer * layer - (x - 1);
            }
        } else {
            if (y == layer) {
                result = layer_start + x;
            } else {
                result = layer * layer - (y - 1);
            }
        }

        cout << result << '\n';
    }
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}