
import win32com.client as win32

# criar a integração com o outlook  
outlook = win32.Dispatch('outlook.application')

# criar um email
email = outlook.CreateItem(0)

try:
    Email_envia = input("DIGITE O EMAIL: ")
    
    tilulo = input("Titulo: ")
    msm = input("Qual é a mesagem? ")
    file = input("Caminho do arquivo:\n(se nao tive arquivo, Presione Enter) ")
        


    email.To = Email_envia
    email.Subject = tilulo
    email.HTMLBody = f"""

        <a>{msm}<a>

    """

    email.Send(file)
except TypeError:
    email.Send()


print("Email Enviado")
