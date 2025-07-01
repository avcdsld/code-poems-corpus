function shift(arr, index) {
    for (let i = index; i < arr.length; i++) {
        arr[i] = arr[i + 1];
    }
    delete arr[arr.length - 1];
    arr.length -= 1;
}