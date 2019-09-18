#!/usr/bin/node
// Cast the first argument received into a number, if is possible 
const num = Number.parseInt(process.argv[2]);
if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log('My number:', num);
}
