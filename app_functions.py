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
        string1 = "Nhớ ăn đủ 3 bữa nhaaaaa!"
        string2 = "Hôm nọ đi ngoài đường thấy một người quen lắm á! Hỏi ra mới biết là mẹ của Meeru luôn.\nĐúng là U MÊ RU mà :>"
        string3 = "Hê lô bạn Nguyễn Thị Uyển Khanh nhaaa"
        string4 = "Này! Tự soi gương kiểm điểm mình đi!\nCó người con gái nào vừa xinh vừa cuti qtqd mà lại còn thông minh như vậy không hả?? (๑˃̵ᴗ˂̵)ﻭ"
        string5 = "Đồ gái alime (/◕ヮ◕)/"
        string6 = "Cin chào Meelim, t là GRimuru đây (ーー;)"
        string7 = "Cô!! Tất cả là tại cô!\nTừ khi gặp cô, không biết từ khi nào tôi đã có thêm quốc tịch khác.\nGiờ tôi đã trở thành người Inazuma"
        string8 = "Khanh muốn gì còn không mau hỏi Trẫm, Trẫm duyệt hết!"
        string9 = "Ahihihohuhhihhuhuo"
        string10 = "Đến chừng nào t chưa nói t ghét miru thì t vẫn ở đây nha"
        string11 = "Nếu mọi thứ có ập đến làm miru áp lực, mệt mỏi thì hãy thử dành thời gian thư giãn cho bản thân xíu nha"
        string12 = "Cười nhiều lên một chút nè"
        string13 = "So whenever you ask me again how i feel\nPlease remember my answer is you\n (Try Again - D.ear, JAEHYUN(Cover:Sam Benwick))"
        string14 = "Hôm nào lại ngồi quán trà Liyue nói chuyện phiếm nha"
        string15 = "Ê tự dưng muốn đàn gheeee. Muốn nghe khumm?"
        string16 = "A B C D E U FUKING PRECIOUSS"
        string17 = "You are special!"
        string18 = "Pepe chào Meeruko nhaa"
        string19 = "Đường đông xe còn Meeru thì Lee Dong-wook (^_^.)"
        string20 = "Nhớ t khum? T thì nhớ áaaa"
        string21 = "Kiếp sau nhớ đi ăn sập cái Việt Nam nhaaa ლ(´ڡ`ლ)"
        string22 = "Cô gái giá băng :))))))))))"
        string23 = "Tự tin lên chút nha"
        string24 = ""
        list_ = [string1, string2, string3, string4, string5, string6, string7, string8, string9, string10, string11, string12, string13, string14, string15, string16, string17, string18, string19, string20, string21, string22, string23]
        return random.choice(list_)