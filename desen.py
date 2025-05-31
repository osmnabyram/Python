#include <iostream>
#include <ctime>
#include <stdlib.h>
#include <math.h>
#include <windows.h>

using namespace std;

void islem(int x)
{
	switch (x)
	{
	case 1:
		cout << "#" << " ";
		break;
	case 2:
		cout << "$" << " ";
		break;
	case 3:
		cout << "%" << " ";
		break;
	default:
		cout << "";
	}
}

void ses()
{
	Beep(330, 250);
	Beep(392, 250);
	Beep(440, 500);
	Beep(392, 500);
	Beep(0, 250);
	Beep(440, 250);
	Beep(494, 250);
	Beep(523, 500);
	Beep(0, 250);
}


int main()
{
	int bakiye, degerler;
	int koldeger;
	int istek;
	cout << "-SLOT HOSGELDINIZ-" << endl;
	ses();
	cout << endl;
	cout << "oynayabilmek icin coin giriniz" << endl;
a:	cin >> bakiye;
	if (bakiye < 1)
	{
		cout << "hatali giris" << endl;
		cout << "tekrar girin" << endl;
		goto a;
	}
	cout << "BASLAMAK ICIN LUTFEN KOLU CEKIN" << endl;
	cout << endl;
o:	cout << "    o" << endl;
	cout << "   /" << endl;
	cout << "  /       |" << endl;
	cout << " /        v (kolu cekmek icin 1 e basin" << endl;
	cout << endl;
	cin >> koldeger;
	cout << endl;
	switch (koldeger)
	{
	case 1:
		cout << '\\' << endl;
		cout << " \\" << endl;
		cout << "  \\" << endl;
		cout << "   o" << endl;
		cout << endl;
		srand(time(0) * 139);
		int degerler[3];
		for (int i = 0; i < 3; i++)
		{
			degerler[i] = 1 + (rand() % 3);
			islem(degerler[i]);
		}
		cout << endl;

		if (degerler[0] == degerler[1] && degerler[1] == degerler[2])
		{
			bakiye = bakiye + 1000;
			cout << "JACKPOT !" << endl;
		}
		else if (degerler[0] != degerler[1] && degerler[1] != degerler[2] && degerler[0] != degerler[2])
		{
			bakiye = bakiye - 500;
		}
		else
		{
			bakiye = bakiye + 500;
		}
		break;
	}

	cout << "Yeni bakiye: " << bakiye << endl;
	cout << endl;

	if (bakiye <= 0)
	{
		cout << "coin bitmistir" << endl;
		return 0;
	}
	else
	{
		goto o;
	}

	system("pause");
	return 0;
}