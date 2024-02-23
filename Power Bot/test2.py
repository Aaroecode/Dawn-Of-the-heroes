from pyngrok import ngrok
ngrok.set_auth_token("2H2VbF2z7YGuUYC1JNV7MSXHVRh_2zdMs78pytKy9aTAF2Ten")
ssh = ngrok.connect(25565, "tcp")
print(ssh)