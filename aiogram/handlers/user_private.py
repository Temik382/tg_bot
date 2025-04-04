from aiogram import  types, Router, F, filters
import sqlite3 as sq
from inline_keyboard import *
from aiogram.filters import CommandStart, Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message, CallbackQuery
from aiogram import  types, Router, F, filters
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from parser_students import group_1,l3,l1,l4,l5, avg2
import database as db
from best_pars import grouped_list1_renamed, grouped_list2_renamed




user_private_router = Router()
lessons = {}

@user_private_router.message(Command('menu'))
async def men(message: types.Message):
    await message.answer('/start - запуск бота\n/table - Расписание по группам')


@user_private_router.message(Command('creator'))
async def i_am(message: types.Message):
    await message.reply('Бот разработан студентом группы ИС-42\nКонтакт--->@artemliange')

class RegisterStates(StatesGroup):
    groups = State()
    num_groups = State()
    pod_groups = State()
    

@user_private_router.message(CommandStart())
async def start_command(message: Message, state: FSMContext):
    await db.create_table()
    await state.set_state(RegisterStates.groups)
    await message.answer("Введите свою группу, например: 'АЭ':")

@user_private_router.message(RegisterStates.groups)
async def process_groups(message: Message, state: FSMContext):
    await state.update_data(groups=message.text)
    await state.set_state(RegisterStates.num_groups)
    await message.answer("Введите номер группы, например: '11':")

@user_private_router.message(RegisterStates.num_groups)
async def process_num_groups(message: Message, state: FSMContext):
    await state.update_data(num_groups=message.text)
    await state.set_state(RegisterStates.pod_groups)
    await message.answer("Введите свою подгруппу, например: '1'")

@user_private_router.message(RegisterStates.pod_groups)
async def process_pod_groups(message: Message, state: FSMContext):
    data = await state.get_data()
    user_id = message.from_user.id
    groups = data['groups']
    num_groups = data['num_groups']
    pod_groups = message.text
    
    existing_user = db.cur.execute("SELECT COUNT(*) FROM users WHERE user_id = ?", (user_id,)).fetchone()[0]
    
    if existing_user > 0:
        await message.answer("Вы уже зарегистрированы.")
        await state.clear()
        return
    
    btn1 = types.InlineKeyboardButton(text='Все верно', callback_data='ok')
    btn2 = types.InlineKeyboardButton(text='Заполнить заново', callback_data='no')
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[[btn1, btn2]])

    await state.update_data(pod_groups=pod_groups)
    await message.answer("Проверьте ваши данные\n\n"
                         f"Название группы - {groups}\n"
                         f"Номер группы - {num_groups}\n"
                         f"Номер подгруппы - {pod_groups}\n\n", reply_markup=keyboard)

@user_private_router.callback_query(RegisterStates.pod_groups)
async def handle_callback(callback: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    user_id = callback.from_user.id
    groups = data['groups']
    num_groups = data['num_groups']
    pod_groups = data['pod_groups']
    
    if callback.data == 'ok':
        await register_user(groups, num_groups, pod_groups, user_id)
        await callback.message.answer("Регистрация прошла успешно.")
        await state.clear()
    elif callback.data == 'no':
        await start_command(callback.message, state)

async def register_user(groups: str, num_groups: str, pod_groups: str, user_id: int):
    try:
        db.cur.execute("INSERT INTO users (groups, num_groups, pod_groups, user_id) VALUES (?, ?, ?, ?)",
                       (groups, num_groups, pod_groups, user_id))
        db.db.commit()
        print(f"Пользователь {user_id} зарегистрирован: группы - {groups}, количество групп - {num_groups}, подгруппы - {pod_groups}")
    except sq.Error as e:
        print(f"Ошибка при регистрации пользователя {user_id}: {e}")
        
        
class Remember(StatesGroup):
    name_group = State()
    name_podgroup = State()

@user_private_router.message(Command('table'))
async def send_keyboard(message: types.Message):
    unique_buttons = set(group[:2] for group in l1)
    if unique_buttons:
        await message.answer('Выберите группу: ', reply_markup=key_group_name())
    

@user_private_router.callback_query(lambda c: c == True) 
async def handle_callback(callback_query: types.CallbackQuery, state: FSMContext):
    button_prefix = callback_query.data
    numbers = [group for group in l1 if group[:2] == button_prefix]

    rows = [numbers[i:i + 5] for i in range(0, len(numbers), 5)]

    keyboard = types.InlineKeyboardMarkup(inline_keyboard=[
        [[types.InlineKeyboardButton(text=num, callback_data=num) for num in row] for row in rows]
    ])
    if button_prefix in set(group[:2] for group in l1):
        await callback_query.message.edit_text('Выберите номер группы: ', reply_markup=keyboard)
    else:
        await callback_query.answer()

         

                    
            
@user_private_router.message()
async def echo(message: types.Message):
    for i in range(len(l1)):
        if message.text == l1[i]:
            lessons['pari1'] = group_1[l3.index(message.text)+1]
            lessons['pari2'] = group_1[l3.index(message.text)+2]
            lessons['pari3'] = group_1[l3.index(message.text)+3]
            lessons['pari4'] = group_1[l3.index(message.text)+4]
            lessons['pari5'] = group_1[l3.index(message.text)+5]
            lessons['pari6'] = group_1[l3.index(message.text)+6]
            lessons['pari7'] = group_1[l3.index(message.text)+7]
            await message.answer(f'Расписание для {l1[i]} на {avg2}:\n\n1 || {lessons.get('pari1')} ||\
                каб. {l5[l3.index(message.text)+1]} || пр. {l4[l3.index(message.text)+1]}\n2 || {lessons.get('pari2')}\
                    || каб. {l5[l3.index(message.text)+2]} || пр. {l4[l3.index(message.text)+2]}\n3 || {lessons.get('pari3')}\
                        || каб. {l5[l3.index(message.text)+3]} || пр. {l4[l3.index(message.text)+3]}\n4 || {lessons.get('pari4')}\
                            || каб. {l5[l3.index(message.text)+4]} || пр. {l4[l3.index(message.text)+4]}\n5 || {lessons.get('pari5')}\
                                || каб. {l5[l3.index(message.text)+5]} || пр. {l4[l3.index(message.text)+5]}\n6 || {lessons.get('pari6')}\
                                    || каб. {l5[l3.index(message.text)+6]} || пр. {l4[l3.index(message.text)+6]}\n7 || {lessons.get('pari7')}\
                                        || каб. {l5[l3.index(message.text)+7]} || пр. {l4[l3.index(message.text)+7]}')





