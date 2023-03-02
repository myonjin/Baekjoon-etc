#include <iostream>
using namespace std;

int main()
{
    int N, A;
    int cnt = 0;	// 사이클을 계산하는 변수. 초기에 0으로 초기화

    cin >> N;		//N을 입력 받는다.
    
    //나중에 if문으로 같은지 비교하기 위해
    //while문 내의 계산을 하기 위한 변수 A에 N의 값을 저장한다.
    A = N;			

    while (true) {
        cnt = cnt + 1;	//사이클 수 1 증가
        A = (A % 10) * 10 + (A / 10 + A % 10) % 10; 
        if (N == A) { 	//원래 수와 새로운 수가 같은지 비교
            break;
        }
    }
    cout << cnt; 		//사이클 수를 출력
    
    return 0;
}