#include <iostream>
#include <string>

using namespace std;

int substrA(string s)
{
    string str = "";
    int count = 0;

    for (int i = 0; i < s.length(); i++)
    {
        int position = str.find(s[i]);

        if (position == string::npos)
        {
            str += s[i];
        }
        else
        {
            str = str.substr(position + 1);
            str += s[i];
        }
        if (str.length() > count)
        {
            count = str.length();
        }

        cout << "Current string: " << str << endl;
    }

    return count;
}

int main()
{
    string st = "abcabcbb";

    cout << "Longest length: " << substrA(st);
    if (st.find('x') == string::npos)
    {
        cout << "x was not found";
    }
    return 0;
}
