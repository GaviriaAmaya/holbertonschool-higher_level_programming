#!/usr/bin/node
// Reads and prints the content of a file

const fs = require('fs');
const path = process.argv[2];

fs.readFile(path, 'utf-8', function (error, content) {
  if (error) {
    console.log(error);
    process.exit();
  }

  console.log(content);
}
);
