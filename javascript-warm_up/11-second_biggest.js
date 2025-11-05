#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  let max = 0;
  let second = 0;

  for (let i = 2; i < process.argv.length; i++) {
    const num = process.argv[i];
    if (num > max) {
      second = max;
      max = num;
    } else if (num > second && num < max) {
      second = num;
    }
  }

  console.log(second);
}
