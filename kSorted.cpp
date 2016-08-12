/**
Given an array of n elements, where each element is at most k away
from its target position, devise an algorithm that fully sorts the array, in
approximately O(n log k) time.

Examples
1. lf K is 2, an element at index 7 in the sorted array, can be at indexes
5, 6, 7, 8, 9 in the given array. The algorithm should put it back at
index 7.

2. if K is 2, then an element at index 3 can be at indices 1,2,3,4, or 5.
 The algorithm should put it back at index 3.
*/

#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;


// helper function for popping a queue and returning the element
int pop(priority_queue<int, vector<int>, greater<int> >* q) {
  int val = q->top();
  q->pop();
  return val;
}

// helper function for printing an array
void printArr(int* arr, int len) {
  for (int i = 0; i < len; ++i) {
    cout << arr[i] << " ";
  }
  cout << endl;
}

/**
Create a k-sorted array. i.e. an array in which any element
is atmost k-distance from it's position in the sorted version
 of the same array.

 It turns our that creating all permutations where each element is
  atmost k-distance away from original position, is a much harder problem
  than sorting the array. :-)
This solution is an approximation, good enough for testing.
*/
 void create_K_unsorted(int* arr, int len, int k) {
  sort(arr, arr+len);

  bool* moved = new bool[len]();

  for (int i = 0; i < len; ++i) {
    if (! moved[i]) {
      // random number between i-k to i+k, taking care of boundaries.
      int target = max(0, i-k) + rand() % ( min(i+k, len) - max(0, i-k) );

      // if neither source or target have been moved before, swap them.
      if (! moved[target]) {
        int tmp = arr[i];
        arr[i] = arr[target];
        arr[target] = tmp;
        moved[i] = moved[target] = true;
      }
    }
  }
}

/**

*/
void sortKsorted(int* arr, int len, int k, int* output) {
  if (k == 1)
    return;

  // allocate on heap to avoid growing stack too much in case array is big  
  auto minq = new priority_queue<int, vector<int>, greater<int> >();

  int cnt = 0;
  for (int i = 0; i < len; ++i) {
    minq->push(arr[i]);
    if (minq->size() > k) {
      output[cnt++] = pop(minq);
    }
  }
  while (cnt < len) {
    output[cnt++] = pop(minq);
  }
}

int main() {
  cout << "Test k sorted" << endl;

  int a[] = {1, 3, 4, 2, 5, 7, 6};
  int b[] = {0, 0, 0, 0, 0, 0, 0};

  // run several times with k=2 to k=5
  for (int i = 2; i < 6; ++i) {
    cout << endl << "------------" << endl;
    create_K_unsorted(a, 7, i);
    printArr(a, 7);
    sortKsorted(a, 7, i, b);
    printArr(b, 7);
    cout << endl << "--xx--" << endl;

    create_K_unsorted(b, 7, i);
    printArr(b, 7);
    sortKsorted(b, 7, i, a);
    printArr(a, 7);
    cout << endl << "------------" << endl;
  }
}
