# API DOCUMENTATION

## SIGN IN

### POST api/user/

Expected JSON :

>{<br>
>	"username": "test",<br>
>	"email": "test@test.com",<br>
>	"password": "1234"<br>
> }

This should return a 201 with :

> {<br>
	"user": {<br>
		"username": "test",<br>
		"email": "test@test.com",<br>
		"password": "pbkdf2_sha256$600000$e9JlmJyL4Mt7Brzf2MAkxm$IRI7Tnbfv4jYQQY1y/vtzmrv/BldE/PgfAYFRWyryjE="<br>
	}
}

Error 400 : 
- "username": [
		"This field may not be blank."
	]
- Same with email and password
- "email": [
		"Enter a valid email address."
	]
- "username": [
		"A user with that username already exists."
	],
- "email": [
		"user with this email already exists."
	]


