#!/usr/bin/node

exports.converter = function (base) {
  return function (num) {
    if (typeof num !== 'undefined' && !isNaN(num)) {
      return (num.toString(base));
    }
  };
};
