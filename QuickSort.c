#include <stdio.h>

// 배열을 피벗 기준으로 분할하고 피벗의 최종 위치를 반환
int partition(int arr[], int left, int right) {
    int pivot = arr[right];
    int i = left;
    for (int j = left; j < right; j++) {
        if (arr[j] < pivot) {  // 피벗보다 작은 요소는 왼쪽으로 이동
            int temp = arr[i]; 
            arr[i] = arr[j];
            arr[j] = temp;
            i++;
        }
    }
    // 피벗을 가운데로 이동하여 분할 완료
    int temp = arr[i];
    arr[i] = arr[right];
    arr[right] = temp;
    return i;  // 피벗 위치 반환
}

void quicksort(int arr[], int left, int right) {
    if (left < right) {
        int pivotIndex = partition(arr, left, right);
        // 피벗을 중심으로 좌우 부분 배열을 재귀적으로 정렬
        quicksort(arr, left, pivotIndex - 1);
        quicksort(arr, pivotIndex + 1, right);
    }
}
