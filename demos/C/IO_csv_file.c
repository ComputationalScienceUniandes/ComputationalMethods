#include <stdio.h>

int main(void)
{
    int sum = 0;
    int count = 0;
    int lineno = 0;
    char line[4096];
    while (fgets(line, sizeof(line), stdin) != 0)
    {
        int id;
        char first[80], last[80], addr[80];
        int age;
        lineno++;
        if (sscanf(line, "%d,%79[^,],%79[^,],%79[^,],%d", &id, first, last, addr, &age) != 5)
            fprintf(stderr, "Invalid data in line %d:\n%s", lineno, line);
        else
        {
            printf("id=%d first=%s last=%s addr=%s age=%d\n",
                   id, first, last, addr, age);
            sum += age;
            count++;
        }
    }

    printf("Average age is %f\n", (float)sum / count);

    return 0;
}


// #include <stdio.h>
// #include <sstream>
// #include <fstream>
// #include <vector>
// #include <string>

// using namespace std;

// int main ()
// {
// 	ifstream inFile ("csv.dat");
// 	string line;
// 	int linenum = 0;
// 	while (getline (inFile, line))
// 	{
// 		linenum++;
// 		cout << "\nLine #" << linenum << ":" << endl;
// 		istringstream linestream(line);
// 		string item;
// 		int itemnum 0;
// 		while (getline (linestream, item, ','))
// 		{
// 			itemnum++;
// 			cout << "Item #" << itemnum << ": " << item << endl;
// 		}
// 	}
// }



