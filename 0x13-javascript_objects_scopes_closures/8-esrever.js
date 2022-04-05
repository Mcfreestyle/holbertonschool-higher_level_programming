#!/usr/bin/node

exports.esrever = function (list) {
  const ar = [];

  while (list.length) ar.push(list.pop());
  return (ar);
};
