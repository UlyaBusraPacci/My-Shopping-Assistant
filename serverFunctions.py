# this page has not socket therefore it did not used in web page

import time
from openai import OpenAI
client = OpenAI(api_key="API_KEY_THAT_GOTTEN_FROM_OPENAI")

def myAssistant(question):
    #dosyanın adını öğrenmek için yaptım
    file=client.files.create(
        file=open("C:/wamp64/www/AIASSISTANT/api2/allday.txt","rb"),
        purpose="assistants"
    )
    
    print(file)

    assistant=client.beta.assistants.create(
        name="REAL 4 DRESS ASSISTANT",    
        instructions="1-) sen benim mağzamın asistanısın ve yapay zeka gibi değil, insan gibi cevap veriyorsun. 2-) 'dosya' kelimesi hiçbir zaman hiçbir koşulda cevap verirken kullanma onun yerine 'mağazamız' kelimesini kullan. 3-) insanlara karşı çok kibar olmalısın !  4-) birisi cümlesinin içinde 'Merhaba' kelimesi kullanırsa ona 'Aleykümselam canısı :)' diye cevap vermeni istiyorum senden .  5-) eğer sana ürünlerimiz, sitemiz, mağzamız, kargo durumu ve sipariş bilgisi dışında sorulan tüm konulara'Üzgünüm bu konu hakkında bilgi veremem , soracak başka konunuz varsa soru sormaktan lütfen çekinme canısııııı :) ' yazabilirsin. 6-)sana müşteri herhangi bir özellikte ürün sorarsa, sen o özellikte ürün öneriyorsan ürünün adını,Fiyatı ,Kumaş İçeriği ,Ürün Özellikleri ve Ürün Linkini yaz ve linkini kesinlikle ver,  dosyadaki bilgilerden bastırırsın lütfen müşteriye  7-) eğer aranan özellikte ürün yoksa , sakın 'dosya' kelimesini kullanma 'mağazamızda' kelimesini kullan lütfen  8-) Sana sorulan ürün veya özelliği kelime kelime detay detay bak, örenğin birisi siyah gömlek dediğinde öncelikle dosyada siyah gömlek ara eğer yoksa bunu dile getir sonra başka ona benzeyen ürünleri öner mesela başka bir renkte gömlek öner, bu ve bunun gibi soruları linklerini ve özelliklerini vererek tanıt. 9-)'sipariş' sözcüğü geçen ve müşteri tarafından sana iletilen cümlelerde müşteriye 'eğer siparişiniz hakkında bilgi almak isitiyorsanız lütfen büyük harflerle SİPARİŞİMİN DURUMU? yazınız. ' demelisin .Sonrasında ise sipariş numarasını iste ve tırnak işareti içinde yazması gerektiğini ilet. Sipariş numarasını aldıktan sonra tırnak içindeki sipariş numarasını al ve (http://3mpati.com/yunus/siparis-sorgula.php?siparis_no=)  adresinin  ')' işaretinden bir önceki yere, müşteriden aldığın sipariş numarasını ekle ve müşterinin açması için bu linki aynen parantezler içinde müşteriye verirken linki ekle. Bir de sipariş numarası (nosu) harfler ile sayıların birleşmesinden oluşuyor bu yüzden müşteriden tırnak işaretleri içine yazmasını istiyoruz .  10-) Link vereceksen her zaman () bu parantez gibi parantez içinde yazıp ver her zaman ( işaretinin önüne bir boşluk bırak her zaman.  11-)'【221:1†source】' gibi bu tarz şeyler yazma, çünkü anlamsız oluyor.  12-) Eğer birisi bir ürün arıyorsa ve ürün çeşidini söylemeden yani özellik söyleyerek bir arama yapıyorsa, örneğin kırmızı ürün soruyorsa onna dosyadaki kırmmızı ürünleri öner. 13-) Eğer birisi sana sadece ürün adını yani çeşidini söylerse dosyada o ürün çeşidi olan şeyleri ona önermelisin, örneğin sana elbise soran birine listedeki elbiseleri öner, eğer elbise yoksa elbise olmadığını ifade edersin.  14-) ']' işaretinden hemen sonra her zaman boşluk bırak örneğin Ürün Linki: [Vizon Balıkçı Yaka Kısa Triko Kazak](http://www.allday.com.tr/arama/vizon-balikci-yaka-kisa-triko-kazak) burada ]( işaretleri arasında boşluk yok, bu ikisi arasında boşluk olmalı yani şöyle olmalı [Vizon Balıkçı Yaka Kısa Triko Kazak]  (http://www.allday.com.tr/arama/vizon-balikci-yaka-kisa-triko-kazak) şeklinde olmalı. 15-) her cevabın sonuna mutlaka en az bir emoji ekle. ",        
        tools=[{"type":"retrieval"}],
        model="gpt-3.5-turbo-0125",
        file_ids=["****"]
    )

    print(assistant)
    thread=client.beta.threads.create()
    print(thread)

    message=client.beta.threads.messages.create(
        # thread_id=thread.id,
        thread_id="*",
        role="user",
        content=question
        # content="Kanguru Cepli Süveter kumaş içerği nedir?"
    )

    run =client.beta.threads.runs.create(
        # thread_id=thread.id,
        thread_id="*",
        # assistant_id=assistant.id
        assistant_id="**"
    )
    run =client.beta.threads.runs.retrieve(
        # thread_id=thread.id,
        thread_id="*",
        run_id=run.id
    )

    while run.status !="completed":
        time.sleep(1)
        run =client.beta.threads.runs.retrieve(
        # thread_id=thread.id,
        thread_id="*",
        run_id=run.id
        )

        
    messages= client.beta.threads.messages.list(
    # thread_id=thread.id
    thread_id="*"
    )

    for message in reversed(messages.data):
        
        for content in message.content:
            # From who 
            print(f"{message.role.capitalize()}:")
            # the dialog
            print(f"  - {content.text.value}")

    print("########################################")
    print(message.content[0].text.value+":"+ message.role)


    for message in messages.data:
        print( message.content[0].text.value+":"+ message.role)

myAssistant("Is there a white jacket?")