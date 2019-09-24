#!/usr/bin/node
// Wedge Antilles? Who's him?

const api = process.argv[2];
const wa = 'https://swapi.co/api/people/18';
const request = require('request');
let counter = 0;

request(api, function (error, response, content) {
  if (error) {
    console.log(error);
    process.exit();
  }

  let json = JSON.parse(content);

  for (let elems in json.results) {
    if (json.results[elems].characters.indexOf(wa) >= 0) {
      counter++;
    }
  }
  console.log(counter);
});
