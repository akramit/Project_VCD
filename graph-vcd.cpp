#include "functions.h"

int main() {

    return 0;
}

int computeVCDimension(vector<int> universe, vector<vector<int>> family) {
    int vcDimension = 0;
    int d_max = (int)log( universe.size()) + 1;
    for(int d = 1 ; i<=d_max ; i++) {
        int shatteredFlag = 0;
        vector<vector<int>> subsetsOfSizeD = getSubsetsOfSizeK(universe.size(), d);
        for ( int i = 0 ; i< subsetsOfSizeD.size() ; i++) {
            vector<int> shatter = subsetsOfSizeD[i];
            if (isSetShattered(shatter, family)) {
                vcDimension = d;
                shatteredFlag  = 1;
                break;
            }
        }
        if (shatteredFlag == 0 ) { // No set of size d got shattered. Then d - 1 is vcd
            break;
        }
    }
    return vcDimension;
}

// Function to generate all subsets of size k
void generateSubsets(int n, int k, int start, vector<int>& current, vector<vector<int>>& result) {
    // If the current combination has size k, add it to the result
    if (current.size() == k) {
        result.push_back(current);
        return;
    }

    // Try to add elements starting from 'start' to form combinations of size k
    for (int i = start; i <= n; ++i) {
        current.push_back(i);  // Add element i
        generateSubsets(n, k, i + 1, current, result);  // Recur for the next element
        current.pop_back();  // Backtrack to remove element i
    }
}

// Wrapper function to initialize and return the result
vector<vector<int>> getSubsetsOfSizeK(int n, int k) {
    vector<vector<int>> result;  // This will store all the subsets of size k
    vector<int> current;  // This will store the current subset being formed
    generateSubsets(n, k, 1, current, result);  // Start from element 1
    return result;
}

bool isSetShattered(vector<int> shatter, vector<vector<int>> & family) {
    
}
