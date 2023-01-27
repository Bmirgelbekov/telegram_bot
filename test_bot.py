import csv
import json
import requests
import telebot
from telebot import types
from bs4 import BeautifulSoup
from bs4.element import ResultSet, Tag

""" 
1) Get html url
2) Get cards from html
3) To parse cards
4) Write down to the file
"""



token = '5870199630:AAEE5EmWgI3Z4tCBZeHCB3ZPKqOTuVIMWzY'

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message: types.Message):
    bot.send_message(message.chat.id, 'Минутку, загружаем самые актуальные новости☺️...')



    URL = 'https://kaktus.media/'

    def get_link_to_all_news(url: str):
        html_of_main_page = requests.get(url=url).text
        soup = BeautifulSoup(html_of_main_page, 'lxml')
        html_link = soup.find('a', class_='Main--all_news-link').get('href')
        return html_link


    def get_html(html_link: str):
        html = requests.get(url= html_link)
        return html.text


    def get_all_news_from_kaktus(html: str) -> ResultSet:
        soup = BeautifulSoup(html, 'lxml')
        all_news = soup.find_all('div', class_='Tag--article')
        return all_news



    def parse_news(all_news: ResultSet[Tag]) -> list[dict]:
        result = []
        for news in all_news:
            title = news.find('div', class_= 'ArticleItem--data ArticleItem--data--withImage').find('a', class_='ArticleItem--name').text.strip()
            image_link = news.find('a', class_= 'ArticleItem--image').find('img').get('src')
            news_link = news.find('a', class_='ArticleItem--name').get('href')

            def description_of_one_news(news_link):
                one_news_page = get_html(news_link)
                soup_of_one = BeautifulSoup(one_news_page, 'lxml')
                descript = soup_of_one.find('div', class_= 'BbCode').find('p').text
                return descript
            description = description_of_one_news(news_link)


            obj = {
                'title': title,
                'image': image_link,
                'news_link': news_link,
                'description': description
            }

            result.append(obj)
        return result


    # def write_to_json(result: list) -> str:
    #     with open('news_from_kaktus.json', 'w') as file1:
    #         res = json.dump(result, file1, ensure_ascii=False, indent=4)



    def main():
        html_link = get_link_to_all_news(URL)
        html = get_html(html_link)
        all_news = get_all_news_from_kaktus(html)
        result = parse_news(all_news)
        
        return result



    if __name__ == '__main__':
        data = main()




    j = 0
    call_back_nums = 1
    inline_keyboard = types.InlineKeyboardMarkup()

    for news in data:
        if j < 20:
            inline_button = types.InlineKeyboardButton(news['title'], callback_data=f'{call_back_nums}')
            inline_keyboard.add(inline_button)            
            j += 1
            call_back_nums += 1
            
    bot.send_message(message.chat.id, 'Новости за сегодня!', reply_markup=inline_keyboard)

    


    

    @bot.callback_query_handler(func=lambda callback: callback.data == '1')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[0]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[0]['title']}</b>\n\n{data[0]['description']}\n{data[0]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '2')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[1]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[1]['title']}</b>\n\n{data[1]['description']}\n{data[1]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '3')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[2]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[2]['title']}</b>\n\n{data[2]['description']}\n{data[2]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '4')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[3]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[3]['title']}</b>\n\n{data[3]['description']}\n{data[3]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '5')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[4]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[4]['title']}</b>\n\n{data[4]['description']}\n{data[4]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '6')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[5]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[5]['title']}</b>\n\n{data[5]['description']}\n{data[5]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '7')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[6]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[6]['title']}</b>\n\n{data[6]['description']}\n{data[6]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '8')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[7]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[7]['title']}</b>\n\n{data[7]['description']}\n{data[7]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '9')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[8]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[8]['title']}</b>\n\n{data[8]['description']}\n{data[8]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '10')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[9]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[9]['title']}</b>\n\n{data[9]['description']}\n{data[9]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '11')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[10]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[10]['title']}</b>\n\n{data[10]['description']}\n{data[10]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '12')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[11]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[11]['title']}</b>\n\n{data[11]['description']}\n{data[11]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '13')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[12]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[12]['title']}</b>\n\n{data[12]['description']}\n{data[12]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '14')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[13]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[13]['title']}</b>\n\n{data[13]['description']}\n{data[13]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '15')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[14]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[14]['title']}</b>\n\n{data[14]['description']}\n{data[14]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '16')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[15]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[15]['title']}</b>\n\n{data[15]['description']}\n{data[15]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '17')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[16]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[16]['title']}</b>\n\n{data[16]['description']}\n{data[16]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '18')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[17]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[17]['title']}</b>\n\n{data[17]['description']}\n{data[17]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '19')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[18]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[18]['title']}</b>\n\n{data[18]['description']}\n{data[18]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            

    @bot.callback_query_handler(func=lambda callback: callback.data == '20')
    def answer(callback: types.CallbackQuery):
        inline_keyboard = types.InlineKeyboardMarkup()
        inline_button = types.InlineKeyboardButton("Остановить!", callback_data='stop')
        inline_button2 = types.InlineKeyboardButton("Подробнее", url=data[19]['news_link'])
        inline_keyboard.add(inline_button2, inline_button)
        bot.send_message(callback.message.chat.id, f"<b>{data[19]['title']}</b>\n\n{data[19]['description']}\n{data[19]['image']}", parse_mode='html', reply_markup=inline_keyboard)
        
        @bot.callback_query_handler(func=lambda callback: callback.data == 'stop')
        def stop_command(message):
            bot.send_message(callback.message.chat.id, 'Досвидания!')
            bot.stop_polling()
            




bot.polling()









