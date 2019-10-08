#!/usr/bin/node
// Function that adds two integers

const a = process.argv[2];
const b = process.argv[3];

function add (a, b) {
  if (process.argv[3]) {
    return (parseInt(a)) + (parseInt(b));
  } else {
    return NaN;
  }
}

console.log(add(a, b));
