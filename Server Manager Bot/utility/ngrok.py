from pyngrok import ngrok, conf
import dotenv, os
dotenv.load_dotenv()
token = os.getenv("NGROK_TOKEN")
ngrok.set_auth_token(token)
def run():
    ssh = ngrok.connect(25565, "tcp", )
    ngrok_process = ngrok.get_ngrok_process()
    return(ssh)
    try:
        ngrok_process.proc.wait()
    except:
        ngrok.kill()

run()