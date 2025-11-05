#!/usr/bin/node

function factorial (a) {
  if (a === 0) return 1;
  return a * factorial(a - 1);
}

if (!parseInt(process.argv[2], 10)) {
  const fact = 0;
  console.log(factorial(fact));
} else {
  const fact = parseInt(process.argv[2], 10);
  console.log(factorial(fact));
}
