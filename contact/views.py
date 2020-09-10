from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import EmailSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from django.core.mail import EmailMessage
from twilio.rest import Client
from decouple import config
# Create your views here.


@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_sms(request):
    account_sid = config("ACCOUNT_SID")
    auth_token = config("AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            body='Hola Sebas, lo lograste por segunda vez!',
            from_='+14702643943',
            to='+573188524067'
        )
        print(message.sid)
        return Response(status=status.HTTP_200_OK)

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    print(message.sid)


# vista para enviar correos
@api_view(['POST'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def send_email(request):
    # Optiene los datos del formulario
    serializer = EmailSerializer(data=request.data)
    if serializer.is_valid():
        email_destination = request.data['email_destination']
        content = request.data['content']

        # ENVIAMOS EL CORREO
        email = EmailMessage(
            "Colegio Ejemplo - Circular Financiera",  # Asunto del mensaje
            "Remitente: {} \nEmail: <{}> \n\nEscribio: \n\n{} ".format(
                'Colegio Ejemplo', 'colegio@gmail.com', content),  # estructura del mensaje
            "testing.developer.404@gmail.com",  # email de origen
            [str(email_destination)],  # email de destino
            reply_to=[email_destination]
        )
        try:
            email.send()
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)