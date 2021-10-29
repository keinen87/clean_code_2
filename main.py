from replit import audio
import os



azbukaMorze = {'а': '.-','б': '-...','в': '.--', 'г': '--.',
               'д': '-..','е': '.','ж': '...-','з': '--..',
               'и': '..','й': '.---','к': '-.-','л': '.-..',
               'м': '--','н': '-.','о': '---','п': '.--.',
               'р': '.-.','с': '...','т': '-','у': '..-',
               'ф': '..-.','х': '....','ц': '-.-.','ч': '---.',
               'ш': '----','щ': '--.-','ъ': '.--.-.','ы': '-.--',
               'ь': '-..-','э': '..-..','ю': '..--','я': '.-.-',
               '1': '.----','0': '-----','2': '..---','3': '...--',
               '4': '....-','5': '.....','6': '-....','7': '--...',
               '8': '---..','9': '----.',',': '--..--','.': '.-.-.-',
               '?': '..--..',';': '-.-.-.',':': '---...',"'": '.----.',
               '-': '-....-','/': '-..-.','(': '-.--.-',')': '-.--.-',
               ' ': '|','_': '..--.-'
               }

soobchenie=os.getenv('komanda', default = 'По-умолчанию')
soobchenie=soobchenie.lower()
x=soobchenie[0]
xx=soobchenie[1]
xxx=soobchenie[2]
probel1=soobchenie[3]
y=soobchenie[4]
yy=soobchenie[5]
yyy=soobchenie[6]
probel2=soobchenie[7]
z=soobchenie[8]
zz=soobchenie[9]
zzz=soobchenie[10]
morz=azbukaMorze[x]+azbukaMorze[xx]+azbukaMorze[xxx]+azbukaMorze[probel1]+azbukaMorze[y]+azbukaMorze[yy]+azbukaMorze[yyy]+azbukaMorze[probel2]+azbukaMorze[z]+azbukaMorze[zz]+azbukaMorze[zzz]        
adres='http://195.161.68.58'
import requests
from alive_progress import alive_bar
import time
def svyazatsya_s_robotom( adres ):
    otvet=requests.get( adres )
    soobshchenie = 'Проверка связи с роботом...' 
    print(soobshchenie)
    with alive_bar( len( soobshchenie ),bar = 'brackets',spinner = 'radioactive' ) as bar:
         for _ in range( len( soobshchenie ) ):
              time.sleep(0.06)
              bar( )

        
    if otvet.status_code==200:
        print( 'Связь с роботом установлена!' ) 
    else:
        print( 'Нет связи с роботом' )    
    print( )
svyazatsya_s_robotom(adres)
def igrat_muzyku( soundfile, delay = 0.3 ):
    audio.play_file( soundfile)
    time.sleep(delay)
def proigrat_muzyku_Morze( morz ):
    print( )
    with alive_bar( len(morz),bar = 'brackets',spinner = 'dots_waves2' ) as bar:
        if   morz[ 0 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 0 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 0 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 1 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 1 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 1 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 2 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 2 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 2 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 3 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 3 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 3 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 4]  == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 4 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 4 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 5 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 5 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 5 ] == '|':
             time.sleep(0.9)
        bar( )  
        if   morz[ 6 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 6 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 6 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 7 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 7 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 7 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 8 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 8 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 8 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 9 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 9 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 9 ] == '|':
             time.sleep(0.9)
        bar( )   
        if   morz[ 10 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 10 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 10 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 11 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 11 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 11 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 12 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 12 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 12 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 13 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 13 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 13 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 14 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 14 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 14 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 15 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 15 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 15 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 16 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 16 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 16 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 17 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 17 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 17 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 18 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 18 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 18 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 19 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 19 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 19 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 20 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 20 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 20 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 21 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 21 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 21 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 22 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 22 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 22 ] == '|':
             time.sleep(0.9)
        bar( )
        if   morz[ 23 ] == '.':
             igrat_muzyku('dot.wav')
        elif morz[ 23 ] == '-':
             igrat_muzyku('dash.wav')
        elif morz[ 23 ] == '|':
             time.sleep(0.9)
        bar( )
    print()
def otpravka_soobshcheniya_robotu(adres, soobshchenie):
    print('Отправка сообщения роботу...')
    otvet = requests.post(adres,soobshchenie.encode('utf-8'))
    if otvet.status_code == 200:
        print('Команда принята.');time.sleep(1);print('Бегу к вам!')
    elif otvet.status_code == 501:
        print('Команда принята. Продолжаю выполнять прежнюю инструкцию.')
    else:
        print('Команда не принята. Не понял вас!')      