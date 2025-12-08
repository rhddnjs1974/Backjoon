#include <bits/stdc++.h>
#include <windows.h>
#include <random>
#include <chrono>
#include <thread>
#define fastio cin.tie(NULL);cout.tie(NULL);ios::sync_with_stdio(false)
using namespace std;


void gotoxy(short x, short y)
{
    COORD Pos = { static_cast<SHORT>(x - 1), static_cast<SHORT>(y - 1) };
    SetConsoleCursorPosition(GetStdHandle(STD_OUTPUT_HANDLE), Pos);
}

struct Random {
    mt19937 rd;
    Random() : rd((unsigned)chrono::steady_clock::now().time_since_epoch().count()) {}
    Random(int seed) : rd(seed) {}
    short GetInt(short l = 0, short r = 32767) {
        return uniform_int_distribution<short>(l, r)(rd);
    }
    double GetDouble(double l = 0, double r = 1) {
        return uniform_real_distribution<double>(l, r)(rd);
    }
}Rand;


struct State {
    short v[8][14]{};

    State() {
        for (int i = 0; i < 8; i++) for (int j = 0; j < 14; j++)
            v[i][j] = Rand.GetInt(0, 9);
    }

    void SetState(string DB[]) {
        for (int i = 0; i < 8; i++) for (int j = 0; j < 14; j++)
            v[i][j] = DB[i][j] & 15;
    }
    void SetState(State& target) {
        for (int i = 0; i < 8; i++) for (int j = 0; j < 14; j++)
            v[i][j] = target.v[i][j];
    }

    bool Check(int n) const {
    	// 생략
        return 1;
    }

    int scoreModule1() {
        int ret = 1;
        for (; Check(ret); ret++);
        return ret;
    }
    int scoreModule2() {
        int ret = 9999;
        for (int i = 0; i <= 9999; i++) {
            if (!Check(i))ret--;
        }
        return ret;
    }
    pair<int, int> scoreModule3() {
        int A, B = 0;
        bool flag = true;
        for (int i = 0; i <= 9999; i++) {
            if (Check(i)) {
                if (flag)A = i;
                B++;
            }
            else {
                flag = false;
            }
        }
        return { A, B };
    }
    pair<int, int> GetScore(int type = 1) {
        pair<int, int> tmp = scoreModule3();
        return { tmp.first, tmp.first };
        return { tmp.second, tmp.first };
        //        return { tmp.first, tmp.first };
        if (type == 1) {
            return { tmp.first + tmp.second * 3, tmp.first };
        }
        else if (type == 2) {
            return { tmp.first * 1.5 + tmp.second, tmp.first };
        }
        else {
            return { tmp.second, tmp.first };
        }
    }
};
int score_type;

constexpr int SZ = 2;
State st[SZ];
int mx[SZ];
int lineNum = 1;
int totalModif = 0, perc = 1;
bool ended[SZ];
State cur[SZ];
//int modify_mode = 2;

constexpr int dbSZ = 50;
string DB[dbSZ][8] = {
{
        "82759812045682",
        "49508201534365",
        "61214267890179",
        "02345678901744",
        "53456139012302",
        "56789012645680",
        "20123457789152",
        "92012315391921"
    }
};



void StateModif(State& nxt) {
    // 변이함수 구현
}
int ThreadSA(int stateID, int lim = 10000, double T = 10.0, double d = 0.9999) {
    // Simulated Annealing 구현
}
void ThreadSAAlgorithm() {
    for (int i = 0; i < SZ; i++) {
        //State a;
        //st[i] = a;
        st[i].SetState(DB[i]);
        mx[i] = st[i].GetScore().first;
        cout << "Case #" << i + 1 << " Score : " << st[i].scoreModule1(); cout << "\n"; lineNum++;
    }

    /// adjustable values
    double T = 5.0, d = 0.9999;
    int lim = 20'000;
    double maxT = 300.0;
    int maxLim = 1000000;
    cout << "Input Temperature : ";
    cin >> T; lineNum++;
    if (cin.fail()) {
        T = 10.0;
    }
    cout << "Input TryCount : ";
    cin >> lim; lineNum++;
    if (cin.fail()) {
        lim = 20000;
    }
    cout << "T : " << T << " lim : " << lim; cout << "\n"; lineNum++;
    double orgT = T;
    int orglim = lim;

    for (int c = 0; ; c++) {
        score_type = c % 3 + 1;
        totalModif = 0, perc = 1;
        gotoxy(1, lineNum);
        cout << "cur_T : " << T << '\n'; lineNum++;
        cout << "cur_lim : " << lim << '\n'; lineNum++;
        gotoxy(45, lineNum - 2);
        printf("Depth : %d", c + 1);
        deque<thread> works;

        for (int i = 0; i < SZ; i++) {
            cur[i] = st[i];
            ended[i] = false;
            works.push_back(thread(ThreadSA, i, lim, T, d));
            if (works.size() >= 5 || i == SZ - 1) {
                for (auto& th : works) {
                    th.join();
                }
                works.clear();
            }
        }

        bool flag = false;
        do {
            flag = true;
            for (int i = 0; i < SZ; i++) {
                flag = flag && ended[i];
            }

        } while (!flag);
        gotoxy(1, lineNum);
        int progressed = 0;
        for (int idx = 0; idx < SZ; idx++) {
            pair<int, int> org_score = st[idx].GetScore(score_type);
            pair<int, int> score = cur[idx].GetScore(score_type);
            cout << "Case #" << idx + 1 << " Score : " << org_score.first << " -> " << score.first; cout << "\n"; lineNum++;
            if (org_score.first > score.first) {
                continue;
            }
            if (org_score.first < score.first)
                progressed++;
            if(org_score.first < score.first)
                st[idx].SetState(cur[idx]);
            else {
                if (org_score.second <= score.second)
                    st[idx].SetState(cur[idx]);
                else {
                    continue;
                }
            }
        }

        /// adjustable values
        // 변수 조정
        cout << "===================================================================\n"; lineNum++;
    }
}

int main() {
    ThreadSAAlgorithm();
}