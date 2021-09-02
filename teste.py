import os
pasta = 'input'
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        txt = (os.path.join(diretorio, arquivo))
        x = txt.replace("/", "\\")

        cmd = "test -o "+x+" "
        cmdwavreplace = cmd.replace("XVAG", "WAV")
        converter = cmdwavreplace+x
        os.system(converter)
        
    

