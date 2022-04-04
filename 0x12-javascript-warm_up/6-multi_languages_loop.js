#!/usr/bin/node

const languages = ['C is fun', 'Python is cool', 'JavaScript is amazing'];

/* for (let i = 0; i < languages.length; i++) {
  console.log(languages[i]);
} */

/* for (const lan of languages) {
  console.log(lan);
} */

languages.forEach(function (lan) {
  console.log(lan);
});
