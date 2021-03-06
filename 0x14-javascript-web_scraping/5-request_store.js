#!/usr/bin/node
// Gets contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
const url = { url: process.argv[2], method: 'GET' };

request.get(url).on('error', function (err) {
  console.log(err);
}).pipe(fs.createWriteStream(process.argv[3]));
