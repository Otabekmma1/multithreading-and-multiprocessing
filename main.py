import threading
import multiprocessing
from concurrent import futures

import qrcode.main
import requests
import datetime

##---------------- MISOL 1 -------------------------\

# ----------------- multithreading ---------------
# def number_summa(number):
#     summa = 0
#     for num in str(number):
#         summa += int(num)
#     print(f"{number} sonning raqamlari yig'indisi =  {summa}")
#
# def calculate(num):
#     number_summa(num)
#
# numbers = [34, 56, 75, 34, 24, 4534]
#
# if __name__ == '__main__':
#
#     # 1-usul
#     # with futures.ProcessPoolExecutor() as executor:
#     #     executor.map(calculate, numbers)
#
#     # 2-usul
#     threads = []
#     for number in numbers:
#         th = threading.Thread(target=calculate, args=(number,))
#         threads.append(th)
#         th.start()
#
#     for th in threads:
#         th.join()

#-------------- multiprocessing ------------------------

# def number_summa(number):
#     summa = 0
#     for num in str(number):
#         summa += int(num)
#     print(f"{number} sonning raqamlari yig'indisi =  {summa}")
#
# def calculate(num):
#     number_summa(num)
#
# numbers = [34, 56, 75, 34, 24, 4534]
#
# if __name__ == '__main__':
#
#     # 1 - usul
#     # with futures.ProcessPoolExecutor() as executor:
#     #     executor.map(calculate, numbers)
#
#     # 2 - usul
#     proceses = []
#     for number in numbers:
#         pr = multiprocessing.Process(target=calculate, args=(number,))
#         pr.start()
#         proceses.append(pr)
#
#     for pr in proceses:
#         pr.join()


##---------------- MISOL 2 ----------------------------

        #------- multithreading -----------------

# def calculate_secund(secunds):
#     day = secunds // (24 * 3600)
#     secunds %= 24 * 3600
#     hour = secunds // 3600
#     secunds %= 3600
#     minute = secunds // 60
#     secunds %= 60
#     print(f"{int(day)} day, {int(hour)} hour, {int(minute)} minute, {int(secunds)} secund")
#
# sekunds = [234545, 466457, 2342432, 45, 353, 463565]
# if __name__ == '__main__':
#
#     #     # 1 - usul
#     # with futures.ProcessPoolExecutor() as executor:
#     #     executor.map(calculate_secund, sekunds)
#
#     # 2 - usul
#     threads = []
#     for secund in sekunds:
#         th = threading.Thread(target=calculate_secund, args=(secund,))
#         th.start()
#         threads.append(th)
#
#     for th in threads:
#         th.join()

       #----------- multiprocessing ------------------

# def calculate_secund(secunds):
#     day = secunds // (24 * 3600)
#     secunds %= 24 * 3600
#     hour = secunds // 3600
#     secunds %= 3600
#     minute = secunds // 60
#     secunds %= 60
#     print(f"{int(day)} day, {int(hour)} hour, {int(minute)} minute, {int(secunds)} secund")
#
# sekunds = [234545, 466457, 2342432, 45, 353, 463565]
# if __name__ == '__main__':
#
#    #     # 1 - usul
#    # with futures.ProcessPoolExecutor() as executor:
#    #     executor.map(calculate_secund, sekunds)
#
#     2 - usul
#     processes = []
#     for secund in sekunds:
#         pr = multiprocessing.Process(target=calculate_secund, args=(secund,))
#         pr.start()
#         processes.append(pr)
#
#     for pr in processes:
#         pr.join()


#---------------- MISOL 3 -------------------------
#multithreading
# def title_names(names_list: list):
#     title = list(map(lambda name: name.title(), names_list))
#     print(title)
#
# names_list = ['abror', 'ali', 'vali', 'shoxjahon']
#
# if __name__ == '__main__':
#     th = threading.Thread(target=title_names, args=(names_list,))
#     th.start()


#multiprocessing
# def title_names(names_list: list):
#     title = list(map(lambda name: name.title(), names_list))
#     print(title)
#
# names_list = ['abror', 'ali', 'vali', 'shoxjahon']
#
# if __name__ == '__main__':
#     pr = multiprocessing.Process(target=title_names, args=(names_list,))
#     pr.start()

#------------ MISOL 4 --------------------

#multithreading
# def scores_75(scores_list: list):
#     sc = list(filter(lambda score: score > 75, scores_list))
#     print(sc)
#
# scores_list = [55, 65, 76, 99, 87, 45, 87, 54 ,79]
#
# if __name__ == '__main__':
#     th = threading.Thread(target=scores_75, args=(scores_list,))
#     th.start()

# --------multiprocessing
# def scores_75(scores_list: list):
#     sc = list(filter(lambda score: score > 75, scores_list))
#     print(sc)
#
# scores_list = [55, 65, 76, 99, 87, 45, 87, 54 ,79]
#
# if __name__ == '__main__':
#     pr = multiprocessing.Process(target=scores_75, args=(scores_list,))
#     pr.start()


#----------- MISOL 5 --------------------
# multithreading
# def palindrom_words(words_list: list):
#     palindrom = list(filter(lambda word: word.lower() == word.lower()[::-1], words_list))
#     print(f"{words_list} ro'yxatdagi palindrom so'zlar:\n"
#           f"{palindrom}")
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# if __name__ == '__main__':
#     th = threading.Thread(target=palindrom_words, args=(words,))
#     th.start()


#multiprocessing
# def palindrom_words(words_list: list):
#     palindrom = list(filter(lambda word: word.lower() == word.lower()[::-1], words_list))
#     print(f"{words_list} ro'yxatdagi palindrom so'zlar:\n"
#           f"{palindrom}")
# words = ['Anna', 'Alexey', 'Alla', 'Kazak', 'Dom']
# if __name__ == '__main__':
#     pr = multiprocessing.Process(target=palindrom_words, args=(words,))
#     pr.start()




#------------------- MISOL 6 -------------------
#multithreading

# API_KEY = 'b01e7608c07f15c54ff9d9b64d478705'
# def weather(city):
#     req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric").json()
#     temp = req['main']['temp']
#     city = req['name']
#     description = req['weather'][0]['main']
#     wind = req['wind']['speed']
#     humidity = req['main']['humidity']
#     utc = 10800
#     sunrise = datetime.datetime.fromtimestamp(req['sys']['sunrise'] + req['timezone'] - utc).strftime('%H:%M:%S')
#     sunset = datetime.datetime.fromtimestamp(req['sys']['sunset'] + req['timezone'] - utc).strftime('%H:%M:%S')
#
#     info = (f"-------------- {city} --------------\n"
#         f"🔹Hozirgi ob-havo ma'lumoti\n"
#             f"🌡️Temperatura: {temp} C°\n"
#             f"️️☁️Namlik: {humidity}%\n"
#             f"🌪️Shamol: {wind}\n"
#             f"🌤️Quyosh chiqishi: {sunrise}\n"
#             f"🌥️Quyosh botishi: {sunset}\n"
#             f"⏱️Sana: {datetime.datetime.today().strftime('%Y/%d/%m')}    Vaqt: {datetime.datetime.today().strftime('%H:%M:%S')}\n"
#             f"{'-'*40}")
#
#     print(info)
#
# if __name__ == '__main__':
#     city_list = ['Uzbekistan',"Amerika", 'Russia', 'New York', 'Korea']
#     threads = []
#     for city in city_list:
#         th = threading.Thread(target=weather, args=(city,))
#         threads.append(th)
#         th.start()
#
#     for th in threads:
#         th.join()


#multiprocessing
# API_KEY = 'b01e7608c07f15c54ff9d9b64d478705'
# def weather(city):
#     req = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric").json()
#     temp = req['main']['temp']
#     city = req['name']
#     wind = req['wind']['speed']
#     humidity = req['main']['humidity']
#     utc = 10800
#     sunrise = datetime.datetime.fromtimestamp(req['sys']['sunrise'] + req['timezone'] - utc).strftime('%H:%M:%S')
#     sunset = datetime.datetime.fromtimestamp(req['sys']['sunset'] + req['timezone'] - utc).strftime('%H:%M:%S')
#
#     info = (f"-------------- {city} --------------\n"
#         f"🔹Hozirgi ob-havo ma'lumoti\n"
#             f"🌡️Temperatura: {temp} C°\n"
#             f"️️☁️Namlik: {humidity}%\n"
#             f"🌪️Shamol: {wind}\n"
#             f"🌤️Quyosh chiqishi: {sunrise}\n"
#             f"🌥️Quyosh botishi: {sunset}\n"
#             f"⏱️Sana: {datetime.datetime.today().strftime('%Y/%d/%m')}    Vaqt: {datetime.datetime.today().strftime('%H:%M:%S')}\n"
#             f"{'-'*40}")
#
#     print(info)
#
# if __name__ == '__main__':
#     city_list = ['Uzbekistan',"Amerika", 'Russia', 'New York', 'Korea']
#     processes = []
#     for city in city_list:
#         pr = multiprocessing.Process(target=weather, args=(city,))
#         processes.append(pr)
#         pr.start()
#
#     for pr in processes:
#         pr.join()




#-------------- MISOL 7 -------------------
#multithreading
# import qrcode
# def qr_code(url, filename):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=10,
#         border = 4,
#     )
#     qr.add_data(url)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color = 'black', back_color='white')
#     img.save(filename)
#
# urls = [
#     'https://github.com',
#     'https://youtube.com',
#     'https://google.com',
#     'https://yandex.ru',
# ]
# if __name__ == '__main__':
#     threads = []
#     for url in urls:
#         filename = f"{urls.index(url)}.png"
#         th = threading.Thread(target=qr_code, args=(url, filename))
#         th.start()
#         threads.append(th)
#
#     for th in threads:
#         th.join()


#multiprocessing
# import qrcode
# def qr_code(url, filename):
#     qr = qrcode.QRCode(
#         version=1,
#         error_correction=qrcode.constants.ERROR_CORRECT_H,
#         box_size=10,
#         border = 4,
#     )
#     qr.add_data(url)
#     qr.make(fit=True)
#
#     img = qr.make_image(fill_color = 'black', back_color='white')
#     img.save(filename)
#
# urls = [
#     'https://github.com',
#     'https://youtube.com',
#     'https://google.com',
#     'https://yandex.ru',
# ]
# if __name__ == '__main__':
#     processes = []
#     for url in urls:
#         filename = f"{urls.index(url)}.png"
#         pr = multiprocessing.Process(target=qr_code, args=(url, filename))
#         pr.start()
#         processes.append(pr)
#
#     for pr in processes:
#         pr.join()