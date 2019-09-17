#!/usr/bin/node
// Prints a predetermined messages depending of the number of args
if (!process.argv[2]) {
  console.log('No argument');
} else if (process.argv[3]) {
  console.log('Arguments found');
} else {
  console.log('Argument found');
}
