function sumOfNum(array) {
  if (array.length == 1) {
    return array[0];
  } else {
    return array.pop() + sumOfNum(array);
  }
}