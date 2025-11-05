#!/usr/bin/node

function addMeMaybe (number, theFunction) {
  const newnum = number + 1;
  return theFunction(newnum);
}

exports.addMeMaybe = addMeMaybe;
