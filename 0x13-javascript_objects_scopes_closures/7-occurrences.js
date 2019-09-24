#!/usr/bin/node
// Function that returns the number of occurrences in a list

exports.nbOccurences = function (list, searchElement) {
  let counter = 0;
  for (let iterator of list) {
    if (iterator === searchElement) {
      counter++;
    }
  }
  return (counter);
}
