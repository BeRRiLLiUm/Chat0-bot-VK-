import datetime
from vkbottle.bot import Bot, Message
from vkbottle import Keyboard, KeyboardButtonColor, Text, OpenLink
import os 
import logging
import datetime 
import csv
import io

token = '-'

logger = logging.getLogger('logger')


group_id = '281865'


bot_token = token
bot_group_id = group_id
vk = Bot(bot_token, bot_group_id)



@vk.on.private_message(text='photo')
async def photo(message: Message):
    await message.answer('Вот твоя фотка ' , attachment='photo-281865_457242085')
    chat_id = message.chat.id
    dtn = datetime.datetime.now()
    botlogfile = open('TestBot.log', 'a')
    print(dtn.strftime("%d-%m-%Y %H:%M ") + str(chat_id), "Поступление в РЭУ", file=botlogfile)
    botlogfile.close()

@vk.on.private_message(text='video')
async def video(message: Message):
    await message.answer('Вот твое видео ', attachment='video-281865_456239235')

@vk.on.private_message(text=['Начать', 'Ку', 'Привет','start','/mm', 'menu', 'меню','start','/start'])
@vk.on.private_message(payload={'cmd': 'menu'})
async def menu(message: Message):
    await message.answer(
        message = 'РЭУ-Пермь приветствует вас!\n\nНапишите в сообщение один из пунктов, и мы с удовольствием ответим на ваши вопросы!',
        keyboard = (
            #Keyboard(inline = True)
            #            .add(OpenLink('https://vk.com/rea_perm', 'l'))
            # one_time - True - одноразовая клавиатура, False - постоянная клавиатура
            # inline - True - клавиатура прикрепляется к сообщению(РАССМОТРИМ), False - клавиаутра в стандартном положении
            # .add - добавить кнопку
            # .row - отступ
            # Цвета: POSITIVE - зеленый, SECONDARY - БЛЕДНО БЕЛЫЙ
            # PRIMARY - СИНИЙ, NEGATIVE - КРАСНЫЙ стильбелый с синим назад!!!!!!!

            Keyboard(one_time = False, inline = False)
            .add(Text('Поступление'), color=KeyboardButtonColor.SECONDARY)
            .row()
            .add(Text('Обучение'))
            .row()
            .add(Text('Допобразование'))
            .row()
            .add(Text('Экспертиза'))
            .row()
            .add(Text('Вопрос'))
            )
    )

@vk.on.private_message(text='Поступление')
@vk.on.private_message(payload={'cmd': 'first'})
async def bot(message: Message):
    await message.answer(
        message = 'Напишите в сообщение один из пунктов, и мы с удовольствием ответим на ваши вопросы!',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Бакалавриат'))
            .row()
            .add(Text('ЕГЭ'))
            .row()
            .add(Text('СПО'))
            .row()
            .add(Text('Магистратура'))
            .row()
            .add(Text('Контакты'))
            .row()
            .add(Text('Правила приема'))
            .row()
            .add(Text('Сроки приема'))
            .row()
            .add(Text('Назад', payload={'cmd': 'menu'}), color=KeyboardButtonColor.PRIMARY)
            )
    )

@vk.on.private_message(text='Обучение')
@vk.on.private_message(payload={'cmd': 'second'})
async def bot(message: Message):
    await message.answer(
        message = 'Напишите в сообщение один из пунктов, и мы с удовольствием ответим на ваши вопросы!',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Деканаты'))
            .row()
            .add(Text('Бухгалтерия'))
            .row()
            .add(Text('Назад', payload={'cmd': 'menu'}), color=KeyboardButtonColor.PRIMARY)
            )
        )
        
    
@vk.on.private_message(text='Допобразование')
@vk.on.private_message(payload={'cmd': 'third'})
async def bot(message: Message):
    await message.answer(
        message = 'Центр доп.образования \n\n(https://www.rea.ru/ru/org/branches/perm/Pages/centr-dopolnitelnogo-professional-nogo-obrazovanija.aspx)',)

@vk.on.private_message(text='Экспертиза')
@vk.on.private_message(payload={'cmd': 'fourth'})
async def bot(message: Message):
    await message.answer(
        message = 'Лаборатория товарных экспертиз (досудебная и судебная экспертиза товаров)\n\n Подробнее (https://www.rea.ru/ru/org/branches/perm/Pages/nauchno-issledovatelskaya-laoratoriya-tovarnykh-ekspertiz.aspx)')

@vk.on.private_message(text='Вопрос')
@vk.on.private_message(payload={'cmd': 'fifth'})
async def bot(message: Message):
    await message.answer(
        message = 'Задайте свой вопрос и вам обязательно ответят!')

@vk.on.private_message(text='Бакалавриат')
async def bot(message: Message):
    await message.answer(
        message = 'Специальности бакалавриата:\n',
        keyboard = (
            Keyboard(inline = True)
            .add(OpenLink('https://rea.perm.ru/?page_id=2162', 'Экономика'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=2152', 'Менеджмент'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=2155', 'Товароведение'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=2159', 'Торговое дело'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=2164', 'Прикладная информатика'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=2157', 'Технология продукции и орг. общ. пит.'))

            ))

@vk.on.private_message(text='ЕГЭ')
async def bot(message: Message):
    await message.answer( 'Картинки 15,17,18')
    await message.answer('фотка пример', attachment='photo-281865_457242085')
    
@vk.on.private_message(text='СПО')
async def bot(message: Message):
    await message.answer(
        message = 'Специальности СПО\n\nПОДРОБНЕЕ (https://rea.perm.ru/?page_id=757)',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Экономика и бухгалтерский учет'))
            .row()
            .add(Text('Страховое дело'))
            .row()
            .add(Text('Товароведение и эксп-за кач-ва тов.'))
            .row()
            .add(Text('Банковское дело'))
            .row()
            .add(Text('Поварское и кондитерское дело'))
            .row()
            .add(Text('Информационные сис. и программирование'))
            .row()
            .add(Text('Назад', payload={'cmd': 'first'}), color=KeyboardButtonColor.PRIMARY)
            ))

@vk.on.private_message(text='Магистратура')
async def bot(message: Message):
    await message.answer(
        message = 'Специальности магистратуры\n\nПОДРОБНЕЕ (https://rea.perm.ru/?page_id=755)',
        keyboard = (
            Keyboard(one_time = False, inline = False)
            .add(Text('Экономика'))
            .row()
            .add(Text('Менеджмент'))
            .row()
            .add(Text('Торговое дело'))
            .row()
            .add(Text('Назад', payload={'cmd': 'first'}), color=KeyboardButtonColor.PRIMARY)
            ))

@vk.on.private_message(text='Контакты')
async def bot(message: Message):
    await message.answer(
        message = '614070, г. Пермь, бульвар Гагарина, 57\n\nтелефоны: 263-26-75, 8-912-88-44-050\n\n perm.pk@rea.ru')

@vk.on.private_message(text='Правила приема')
async def bot(message: Message):
    await message.answer(
        message = 'info: ',
        keyboard = (
            Keyboard(inline = True)
            .add(OpenLink('https://rea.perm.ru/?page_id=759', 'Высшее образование'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=761', 'СПО'))
        ))
        

@vk.on.private_message(text='Сроки приема')
async def bot(message: Message):
    await message.answer(
        message = 'info: ',
        keyboard = (
            Keyboard(inline = True)
            .add(OpenLink('https://rea.perm.ru/?page_id=1', 'Высшее образование'))
            .row()
            .add(OpenLink('https://rea.perm.ru/?page_id=1', 'СПО'))
        ))

@vk.on.private_message(text='Деканаты')
async def bot(message: Message):
    await message.answer(
        message = '(справки, вопросы по обучению, переводам и прочее) ',
        keyboard = (
            Keyboard(inline = True)
            .add(OpenLink('https://www.rea.ru/ru/org/branches/perm/sveden/struct/Pages/uff/contacts.aspx', 'Учетно-финансовый факультет'))
            .row()
            .add(OpenLink('https://www.rea.ru/ru/org/branches/perm/sveden/struct/Pages/menegment/contacts.aspx', 'Факультет Менеджмента'))
            .row()
            .add(OpenLink('https://www.rea.ru/ru/org/branches/perm/sveden/struct/Pages/teh_tto/contacts.aspx', 'Торгово-технологическое отделение'))
            .row()
            .add(OpenLink('https://www.rea.ru/ru/org/branches/perm/sveden/struct/Pages/teh_ikt/contacts.aspx', 'Отделение ИКТ'))
            ))

@vk.on.private_message(text='Бухгалтерия')
async def bot(message: Message):
    await message.answer(
        message = '(оплата обучения, материальная помощь, прочее) ',
        keyboard = (
            Keyboard(inline = True)
            .add(OpenLink('https://www.rea.ru/ru/org/branches/perm/Pages/%D0%A1%D0%BE%D1%82%D1%80%D1%83%D0%B4%D0%BD%D0%B8%D0%BA%D0%B8-%D0%B1%D1%83%D1%85%D0%B3%D0%B0%D0%BB%D1%82%D0%B5%D1%80%D0%B8%D0%B8.aspx', 'Контакты'))
            ))

@vk.on.private_message()
async def main(message):
    await message.answer('Я не знаю, что ответить на это =(')


vk.run_forever()
