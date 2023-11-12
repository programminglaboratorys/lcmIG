// my_c_library.cpp

#include <math.h>

extern "C" {
    __declspec(dllexport) long gcd(long long a, long long b) { 
        if (b == 0) 
            return a; 
        return gcd(b, a % b);  
    }  
    __declspec(dllexport) int lcm(int a, int b) {
        if (a == 0 || b == 0) {return 0;}
        return a * b / gcd(a,b);
    }

    __declspec(dllexport) int range_lcm(int start, int end) {
        int result = 1;
        for(int i = start; i <= end; i++) {
            result = lcm(result, i);
        }
        return result;
    }
}
