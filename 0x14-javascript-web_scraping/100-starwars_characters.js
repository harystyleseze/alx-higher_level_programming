#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi.dev/api/films/${movieId}/`;

request.get(url, { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const characters = body.characters;
  characters.forEach((characterUrl) => {
    request.get(characterUrl, { json: true }, (error, response, body) => {
      if (error) {
        console.log(error);
        return;
      }
      console.log(body.name);
    });
  });
});
