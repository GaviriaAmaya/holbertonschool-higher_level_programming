#!/usr/bin/node
// Prints a list in reverse

exports.esrever = function (list) {
  let reverse = [];
  for (let lengther = (list.length) - 1; lengther >= 0; lengther--) {
    reverse.push(list[lengther]);
  }
  return reverse;
};
