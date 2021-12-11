#Deploy guide
For correct working service you should setup 3 environment variable:
- CONNECTION_STRING - Required for connection to your mongodb instance
- algorithm - Password encryption algorithm
- secret - Salt for jwt token

You can make it directly and define it in your OS or create .env file in root of the project and define 
its in this file