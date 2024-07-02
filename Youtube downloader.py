from pytube import YouTube

opcao = -1

while opcao != 0:
    opcao = int(input("abaixar video [1] sair [0]\n: "))
    
    if opcao == 1:
        url = input("coloque seu link aqui: ")
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download()
        print("download completo!")
        
    else:
        print("saindo...")
