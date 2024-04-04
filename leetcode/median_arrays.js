let array1 = [1, 24, 3, 7, 2, 5];
let position = array1.length / 2;
array1.sort((a, b) => a - b)
array1.length % 2 !== 0 ? median = array1[Math.floor(position)] : median = (array1[position - 1] + array1[position]) / 2 ;
console.log(median)