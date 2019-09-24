#!/usr/bin/node
// Converts any number to any base

exports.converter = function (base) {
  function based (number) {
    return number.toString(base);
  }
  return (based);
};
