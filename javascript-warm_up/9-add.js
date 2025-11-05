#!/usr/bin/node

const first = parseInt(process.argv[2], 10);
const second = parseInt(process.argv[3], 10);

function add (a, b) {
  return a + b;
}

console.log(add(first, second));
