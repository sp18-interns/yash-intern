# Date 13-July-2022

## First Half

- 🔄 Autoscal Project : In Progress

### Videos

- None

### Assignment

- Worked on sending verification code API adding functions to generate OTP.
- [auth-service](https://github.com/autoscal-SP18/auth-service/tree/AUT-17-api-send-verification-code)

### Doubts

- None

### Links Read

- [Send Email with Django](https://www.sitepoint.com/django-send-email/)

## Second Half

- 🔄 Attended Stand-Up of autoscal
- Attended Knowledge Sharing Session on Kafka

### Videos

- None

### Assignment

- Did mistake of raising PR of Send OTP API without testing it.
- Merged Verify OTP with Send OTP branch as it uses common model.
- [auth-service](https://github.com/autoscal-SP18/auth-service/tree/AUT-17-api-send-verification-code)
- [auth-service](https://github.com/autoscal-SP18/auth-service/tree/AUT-18-api-verify-otp)

### Doubts

- Wasn't able to send otp to email. Having an assertion error issue in Send OTP API. While printing exception, earlier error pointed at smtpauthentication errors. After solving them, had error about incorrect email and password. After solving them, had error about matching query doesn't exist.
  The error still exists, but otp are being sent and recieved.

- ![Alt text](OTP-Email.png?raw="True")

## Links Read

- [Create and Use Signals in Django](<https://www.geeksforgeeks.org/how-to-create-and-use-signals-in-django/#:~:text=There%20are%203%20types%20of,()>)%20this%20signal%20is%20thrown.)
