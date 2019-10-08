#!/usr/bin/node
// Function that adds two integers

let num1 = process.argv[2];
let num2 = process.argv[3];

if (process.argv <= 2) {
  console.log(NaN);
} else if (isNaN(num1) || isNaN(num2)) {
  console.log(NaN);
} else {
  num1 = parseInt(num1);
  num2 = parseInt(num2);

  const result = num1 + num2;
  console.log(result);
}
