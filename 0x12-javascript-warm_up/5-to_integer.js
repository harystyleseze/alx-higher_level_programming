#!/usr/bin/node
const arg = process.argv[2];
const num = parseInt(arg);

console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);

