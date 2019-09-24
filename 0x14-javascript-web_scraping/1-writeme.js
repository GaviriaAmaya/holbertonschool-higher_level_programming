#!/usr/bin/node
// Write text on a file

const fs = require('fs');
const path = process.argv[2];
const content = process.argv[3];

fs.writeFile(path, content, 'utf-8', function (error, data) {
  if (error) {
    console.log(error);
    process.exit();
  }
});
