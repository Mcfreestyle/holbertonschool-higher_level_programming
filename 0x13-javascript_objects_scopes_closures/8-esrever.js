#!/usr/bin/node

exports.esrever = function (list) {
  let size = list.length;
  const ar = [];

  while (size--) ar.push(list[size]);
  return (ar);
};
