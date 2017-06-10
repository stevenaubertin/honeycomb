"use strict"

var clone = require('git-clone');

module.exports = function(path) {
    const honeycomb = "https://github.com/stevenaubertin/honeycomb.git";
    clone(honeycomb, path, () =>{
        console.log('Cloning done');
        console.log('Happy Hacking !!!');
    });
};