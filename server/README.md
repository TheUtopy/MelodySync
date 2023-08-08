# API DOCUMENTATION

- [SIGN-UP](#sign-up)
- [LOGIN](#login)
- [CONTACT](#contact)

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

And a session cookie that looks like :

>sessionid: 4cojwlx1izctcaugt0a8kxmnu146jk60

This session cookie have a 2 hours live spawn in the server side (unless the session data is updated). On the client side, the session cookie doesn't have any expiry time. Instead it's deleted when the user close the navigator.

Connection also send a crsftoken, to prevent crsf attacks.

If "stay_connected": true is in the body of the request, then the session cookie will be set to 90 days instead of 2 hours (client and server side).

Else it returns a 401 with :

>{<br>
	"error": "Invalid Credentials"<br>
}

If the data sent is missing either username or password, it return a 400:

>{<br>
	"error": "Missing Credentials"<br>
}


## CONTACT

### POST /api/contact/

Expected format :

>{<br>
	"email": "example@mail.com",<br>
	"message": "Message Content"<br>
}

Should return a 200 with :
>{<br>
	"Success": "Email sent"<br>
}

It also send a fictive email using the EMAIL_BACKEND option of Django.<br>

If the email or message field is empty or if the message field is "Your message goes here.", return a 400 :

>{<br>
	"error": "Email and/or message fields are empty."<br>
}

If the message is more than 500 characters long, return a 400:

>{<br>
	"error": "Message is too long. Must be 500 charracters max."<br>
}

If the email is not valid, return a 400 : 

>{<br>
	"error": "Enter a valid email address."<br>
}
