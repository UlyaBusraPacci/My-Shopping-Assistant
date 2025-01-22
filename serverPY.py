from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from openai import OpenAI
import time

# flask uygulaması oluşturmak içinmiş
app = Flask(__name__)
# socket bağlantısı yapıyoruz, CORS hata vermesin diye bunu kullanıyoruz
socketio = SocketIO(app, cors_allowed_origins="*")


# yazılan adresine gelen istekler için index sayfasını döndürmüş
@app.route('/')

# HTML içeriği oluşturup, içeriği istemciye göndermek içinmiş
def index():
    # flask te içerik oluşturma fonk.
    return render_template('index.html')

# gelen question ı dinleyen fonsiyondan almak için dinleyen fonsiyon bu
@socketio.on('question')

# data denilen istemciden gelen veri yani question oluyor
def handle_question(data):
    # gelen soruyu alıyor ve question değerine atıyoruz
    question = data.get('question', '')
    # sonra bu soruyu assistant a yönlendirmek için yaptığım fonksiyona atıyoruz
    # ve cevabı döndürdüğü için geri dönüşü alıyoruz
    assistant_response = myAssistant(question)
    # bu da HTML sayfasında script tag inin içinde yazdığımız 'answer' socket.on a gidiyor
    # aslında veriyi buradan gönderiyoruz
    emit('answer', {'assistant_response': assistant_response})


# bunu biliyorsun zaten
def myAssistant(question):
    api_key = "API_KEY"
    client = OpenAI(api_key=api_key)
    
    # thread=client.beta.threads.create()
    # print(thread)
    
    #  json ile açılan 
    message = client.beta.threads.messages.create(
        # thread_id=thread.id,
        thread_id="*",
        role="user",
        content=question
    )
    run = client.beta.threads.runs.create(
        # thread_id=thread.id,
        thread_id="*",
        assistant_id="**"
    )
    run = client.beta.threads.runs.retrieve(
        # thread_id=thread.id,
        thread_id="*",
        run_id=run.id
    )
    while run.status != "completed":
        time.sleep(1)
        run = client.beta.threads.runs.retrieve(
            # thread_id=thread.id,
            thread_id="*",
            run_id=run.id
        )
    messages = client.beta.threads.messages.list(
        # thread_id=thread.id,
        thread_id="*"
    )
    assistant_response = ""
    for message in reversed(messages.data):
        for content in reversed(message.content):
            assistant_response = f"{message.role.capitalize()}: {content.text.value}\n"
            break
    print(assistant_response)
    return assistant_response

# myAssistant("turuncu ne var?")


if __name__ == '__main__':
    print("python kısmı")
    
    # burada da socket.io yu 4000 port üzerinden çalıştırıyoruz
    socketio.run(app, port=4000)

