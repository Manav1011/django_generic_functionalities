# Signup (Email and Password with Additional Required Details)

- Provide a signup form with fields for email, password, and other required details.
- As the user enters their email and password, generate a time-based `secret_key` using these credentials. This key will be used for the websocket endpoint, enabling real-time communication.
- Store this hash in a custom user model within the database for future use.
- Generate a QR code containing this hash, start a websocket server, and prompt the user to enter the OTP.

## Authenticator Workflow

- The user needs to log in to the authenticator app first, using the same credentials they provided on the platform.
- An option will be available to scan the QR code. Scanning the QR code initiates a websocket connection using the `secret_key` from the QR code as a client.
  > Note: The same QR code should only be scannable once. Upon scanning, the `secret_key` is immediately changed, and the QR code is updated on the screen.
  >
- Once the connection is established, a time-based OTP is sent to the client. The authenticator app displays the TOTP.
  - If the user enters the OTP in time and is successfully authenticated:
    - Authenticate the user and create their account.
  - If the OTP is entered incorrectly:
    - Send another TOTP for retry.
  - If the OTP is expired:
    - Send another TOTP to the user.

Upon successful authentication, log the user in without requiring further authentication.

# Login (Email and Password)

- Provide a login form with fields for email and password.
- As the user enters their email and password, retrieve the hash from the database and start a websocket server.
- In the login modal, include a button to show a QR code. This is useful if the app session is lost or the user wants to set up the authenticator on another device.
- When the user opens the authenticator app, it attempts to establish a websocket connection. If the connection fails (due to a changed `secret_key`), the user needs to scan the latest QR code and will be presented with the TOTP.
  - If the user enters the OTP in time and is authenticated:
    - Authenticate the user and log them in.
  - If the OTP is entered incorrectly:
    - Send another TOTP for retry.
  - If the OTP is expired:
    - Send another TOTP to the user.

> Note: One-time backup codes can be generated for situations where the user does not have access to the authenticator app. The user can request these backup codes from the admin.
>
