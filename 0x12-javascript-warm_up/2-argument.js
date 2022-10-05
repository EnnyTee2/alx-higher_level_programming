#!/usr/bin/node

const argv_length = process.argv.length;
if (argv_length === 2) {
  console.log('No argument');
} else if (argv_length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
