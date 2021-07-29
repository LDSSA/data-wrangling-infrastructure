# data-wrangling-infrastructure

## Hosting

### APIs

The APIs are currently hosted on heroku on
* https://ldsa-learning-api.herokuapp.com/random
* https://ldsa-pokemon-api.herokuapp.com/pokemon/all

Deploy with
```bash
heroku create ldsa-pokemon-api
heroku git:remote ldsa-pokemon-api
heroku stack:set container
git subtree push --prefix apis/pokemon_api heroku main
```

### Websites

The websites are static and hosted on s3
* https://s02-infrastructure.s3.eu-west-1.amazonaws.com/ldsa-bork/index.html
* https://s02-infrastructure.s3.eu-west-1.amazonaws.com/ldsa_imdb/index.html
