# API DOCUMENTATION

## SIGN UP

### POST /api/user/

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
- "password": [
		"This password is too short. It must contain at least 8 characters.",
		"This password is too common.",
		"This password is entirely numeric.",
		"The password is too similar to the username.",
		"The password is too similar to the email."
	]

Error 409 :
- "username": [
		"A user with that username already exists."
	],
- "email": [
		"user with this email already exists."
	]


## LOGIN

### POST /api/user/login/

Expected format :

>{<br>
	"username": "test",<br>
	"password": "poisfd45646"<br>
}

It should return a 200 with :

>{<br>
	"status": "login successful"<br>
}

And a session cookie that look like :

sessionid: 4cojwlx1izctcaugt0a8kxmnu146jk60

Else it returns a 400 with :

>{<br>
	"error": "Invalid Credentials"<br>
}
