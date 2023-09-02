from CustomUser.models import CustomUser
from rest_framework.response import Response
from django.contrib.auth.hashers import make_password
from rest_framework.decorators import api_view
import qrcode
import qrcode.image.svg
from django.conf import settings as django_settings
from django_ratelimit.decorators import ratelimit
from django.contrib.auth import authenticate
import smtplib
from email.mime.multipart import MIMEMultipart
import io
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
# Create your views here.

def generate_key(email,password):
    text = f"{email}:{password}"
    generated_hash = make_password(text)
    return generated_hash

def send_qr(receiver,secret):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(secret)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    msg = MIMEMultipart()
    msg['Subject'] = "QR code from the app"
    msg.attach(MIMEText("Please scan this attached QR code into authenticator app to verify your account!"))
    image = MIMEImage(img_bytes.getvalue(), name="qrcode.png")
    msg.attach(image)
    sender_email = django_settings.EMAIL_HOST_USER
    receiver_email = receiver
    password = django_settings.EMAIL_HOST_PASSWORD
    smtp_server = django_settings.EMAIL_HOST
    smtp_port = django_settings.EMAIL_PORT
    sent = False
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, password)

        server.sendmail(sender_email, receiver_email, msg.as_string())
        sent = True
    except Exception as e:
        print(e)
        sent = False
    finally:
        server.quit()
    return sent

def get_qr_svg(secret):
    factory = qrcode.image.svg.SvgPathImage
    img = qrcode.make(secret, image_factory=factory)
    svg_code = img.to_string(encoding='unicode')
    return svg_code

@ratelimit(key='ip', rate='1/m', block=True)
@api_view(['POST'])
def SignupUser(request):
    response = {'error':0, 'message':'', 'data':{}}
    creds = request.data
    try:
        if 'email' in creds and 'password' in creds:    
            email = creds['email']
            password = creds['password']            
            # Generate secret key from email and password
            # Create or get the user
            user,created = CustomUser.objects.get_or_create(email=email)            
            if created:
                user.set_password(password)
                secret = generate_key(email,password)
                user.secret = secret
                user.save()
            # Generate QR code from it                         
            if not user.is_active:
                if user.email_verified:
                    svg_code = get_qr_svg(user.secret)
                    response['message'] = 'Email is already verified'
                    response['data']['verified'] = 1
                    response['data']['secret'] = user.secret
                    response['data']['svg'] = svg_code
                else:                    
                    response['data']['secret'] = user.secret
                    response['data']['verified'] = 0
                    send_qr(email,user.secret)
                    response['message'] = 'QR code sent to the email'   
            else:
                raise Exception("You've already signed up")                
        else:
            raise Exception('Credentials missing')
    except Exception as e:
        response['error']+=1
        response['message']=str(e)
    return Response(response)

@ratelimit(key='ip', rate='1/m', block=True)
@api_view(['POST'])
def LoginUser(request):
    response = {'error':0, 'message':'', 'data':{}}
    creds = request.data
    try:
        if 'email' in creds and 'password' in creds:
            email = creds['email']
            password = creds['password']
            user = authenticate(email=email,password=password)
            if user and user.is_active:
                secret = user.secret
                svg_code = get_qr_svg(secret)
                response['data']['svg'] = svg_code
                response['data']['secret'] = secret
            else:
                raise Exception('User does not exist')
        else:
            raise Exception('Credentials missing')
    except Exception as e:
        response['error'] +=1
        response['message'] = str(e)
    return Response(response)