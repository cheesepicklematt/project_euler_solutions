#include <iostream>
#include <vector>
#include <algorithm>

int main() {
    std::vector<int> output3;
    for (int i=3; i<1000; i+=3){
        output3.push_back(i);
    }

    std::vector<int> output5;
    for (int i=5; i<1000; i+=5){
        output5.push_back(i);
    }

    std::vector<int> difference;
    std::set_difference(
        output3.begin(), output3.end(),
        output5.begin(), output5.end(),
        std::back_inserter(difference)
    );

    difference.insert(difference.end(), output5.begin(), output5.end());
    
    int sum = 0;
    std::cout<<"output list";
    for (int num: difference){
        sum += num;
    }
    
    std::cout << "sum: " << sum << std::endl;

    return 0;
}