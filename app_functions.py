## ==> GUI FILE
from main import *

from gtts import gTTS
from googletrans import Translator
import os
import pafy
import random
from youtube_search import YoutubeSearch
import vlc
import wikipedia
import wolframalpha

class Functions(MainWindow):
    def GetAnswer(query):
        '''Return answer from wikipedia or wolframalpha'''
        if query:
            try:
                # WOLFRAMALPHA
                app_id = 'WTRAQ5-VR7PE9EHYH'
                client = wolframalpha.Client(app_id)

                res = client.query(query)
                answer = ''
                for pod in res.pods:
                    # Need replacing the title list with titles in wolframalpha
                    if pod.title in ["Solution", "Solutions", "Real solution", "Real solutions", "Complex solutions", "Result",
                    "Integer solution", "Numerical solutions"] :
                        answer += pod.title
                        answer += ':\n'
                        for sub in pod.subpods:
                            answer += sub.plaintext
                            answer += '\n'
                if not answer:
                    raise ValueError

            except:
                # WIKIPEDIA
                answer = wikipedia.summary(query, sentences=3)
            return answer
        return None
    
    def GetSound(query):
        '''Return mp3 url'''
        if query:
            try:
                # WOLFRAMALPHA
                app_id = 'WTRAQ5-VR7PE9EHYH'
                client = wolframalpha.Client(app_id)

                res = client.query(query)
                answer = ''
                for pod in res.pods:
                    if pod.title in ["Solution", "Solutions", "Real solution", "Real solutions", "Complex solutions", "Result"] :
                        answer += pod.title
                        answer += ':\n'
                        for sub in pod.subpods:
                            answer += sub.plaintext
                            answer += '\n'

            except:
                # WIKIPEDIA
                answer = wikipedia.summary(query, sentences=3)
            if os.path.exists('gtts_obj.mp3'):
                os.remove('gtts_obj.mp3')
            gtts_obj = gTTS(answer, lang='en')
            gtts_obj.save('gtts_obj.mp3')
            url = QtCore.QUrl.fromLocalFile('gtts_obj.mp3')
            return url
        return None

    def GetYouTubeLink(query):
        '''Return the best Youtube link by keywords'''
        if query:
            search_term = ""
            for word in str(query).split():
                search_term += word + " "
            results = YoutubeSearch(search_term, max_results=10).to_dict()
            url_code = results[0]['id']
            url = "https://www.youtube.com/watch?v=" + url_code  
            return url
        return None  

    def VLCPlay(url):
        '''Stream video online using VLC'''
        global media
        video = pafy.new(url)
        best = video.getbest()
        media = vlc.MediaPlayer(best.url)
        media.video_set_spu(2) 
        media.play()

    def PauseVideo():
        media.pause()

    def StopVideo():
        media.stop()

    def MediaCheck():
        try:
            if media:
                return True
        except:
            return False

    def Translate(query, src, dest):
        '''Return translated text'''
        translator = Translator()
        
        if (src == "auto detect"):
            translations = translator.translate(query.split('\n'), dest=dest)
        else:
            translations = translator.translate(query.split('\n'), src=src, dest=dest)

        origin = ''
        answer = ''
        for translation in translations:
            origin += translation.origin + '\n'
            answer += translation.text + '\n'
        return answer

    def Gift():
        string1 = "Nh??? ??n ????? 3 b???a nhaaaaa!"
        string2 = "H??m n??? ??i ngo??i ???????ng th???y m???t ng?????i quen l???m ??! H???i ra m???i bi???t l?? m??? c???a Meeru lu??n.\n????ng l?? U M?? RU m?? :>"
        string3 = "H?? l?? b???n Nguy???n Th??? Uy???n Khanh nhaaa"
        string4 = "N??y! T??? soi g????ng ki???m ??i???m m??nh ??i!\nC?? ng?????i con g??i n??o v???a xinh v???a cuti qtqd m?? l???i c??n th??ng minh nh?? v???y kh??ng h????? (??????????????)???"
        string5 = "????? g??i alime (/?????????)/"
        string6 = "Cin ch??o Meelim, t l?? GRimuru ????y (??????;)"
        string7 = "C??!! T???t c??? l?? t???i c??!\nT??? khi g???p c??, kh??ng bi???t t??? khi n??o t??i ???? c?? th??m qu???c t???ch kh??c.\nGi??? t??i ???? tr??? th??nh ng?????i Inazuma"
        string8 = "Khanh mu???n g?? c??n kh??ng mau h???i Tr???m, Tr???m duy???t h???t!"
        string9 = "Ahihihohuhhihhuhuo"
        string10 = "?????n ch???ng n??o t ch??a n??i t gh??t miru th?? t v???n ??? ????y nha"
        string11 = "N???u m???i th??? c?? ???p ?????n l??m miru ??p l???c, m???t m???i th?? h??y th??? d??nh th???i gian th?? gi??n cho b???n th??n x??u nha"
        string12 = "C?????i nhi???u l??n m???t ch??t n??"
        string13 = "So whenever you ask me again how i feel\nPlease remember my answer is you\n (Try Again - D.ear, JAEHYUN(Cover:Sam Benwick))"
        string14 = "H??m n??o l???i ng???i qu??n tr?? Liyue n??i chuy???n phi???m nha"
        string15 = "?? t??? d??ng mu???n ????n gheeee. Mu???n nghe khumm?"
        string16 = "A B C D E U FUKING PRECIOUSS"
        string17 = "You are special!"
        string18 = "Pepe ch??o Meeruko nhaa"
        string19 = "???????ng ????ng xe c??n Meeru th?? Lee Dong-wook (^_^.)"
        string20 = "Nh??? t khum? T th?? nh??? ??aaa"
        string21 = "Ki???p sau nh??? ??i ??n s???p c??i Vi???t Nam nhaaa ???(????`???)"
        string22 = "C?? g??i gi?? b??ng :))))))))))"
        string23 = "T??? tin l??n ch??t nha"
        string24 = ""
        list_ = [string1, string2, string3, string4, string5, string6, string7, string8, string9, string10, string11, string12, string13, string14, string15, string16, string17, string18, string19, string20, string21, string22, string23]
        return random.choice(list_)