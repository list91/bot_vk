import vk_api
import random 
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from vk_api import VkApi
from vk_api.upload import VkUpload
import csr
token="..." # В ковычки вставляем токен.
test_list=["hello","..."]
PEER_ID = '...'

def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['owner_id']
    photo_id = response['id']
    access_key = response['access_key']
    return owner_id, photo_id, access_key
def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )
def main():
    vk_session = VkApi(token=token)
    vk = vk_session.get_api()
    upload = VkUpload(vk)

    send_photo(vk, PEER_ID, *upload_photo(upload, 'screen.png'))
# Подключаем токен и longpoll
bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)
# вход в систему
def blasthack(id, text):
    bh.method('messages.send', {'user_id' : id, 'message' : text, 'random_id': 0})
blasthack(PEER_ID, '####################################' )
# Слушаем longpoll(Сообщения)
for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
      # Чтобы не отвечал на самого себя
       if event.to_me:
        # чтобы бот читал все с маленьких букв 
          message = event.text.lower()
          # Получаем id пользователя
          id = event.user_id
          if message == 'ы':
            csr.screen()
            main()
          elif message == 'id':
              blasthack(id, str(id) )

          else:
             blasthack(id, random.choice(test_list))

