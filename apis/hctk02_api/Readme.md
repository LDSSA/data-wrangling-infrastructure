API LDSSA -  Hackthon 2
============================

## Deploy instructions
To deploy, first [install serverless](https://www.serverless.com/framework/docs/getting-started) locally.

The following instructions were testes on a Mac, so I can't promise they'll work in general.

Then run:
```
serverless plugin install -n serverless-python-requirements
```

And finally deploy the app with
```
sls deploy
```
