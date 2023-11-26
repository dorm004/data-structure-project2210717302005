import json

def load_dictionary():
    try:
        with open('dictionary.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def save_dictionary(dictionary):
    with open('dictionary.json', 'w') as file:
        json.dump(dictionary, file, indent=2)

def add_word(dictionary, word, definition):
    dictionary[word] = definition
    save_dictionary(dictionary)
    print(f'เพิ่มคำศัพท์ "{word}" เรียบร้อยแล้ว')

def delete_word(dictionary, word):
    if word in dictionary:
        del dictionary[word]
        save_dictionary(dictionary)
        print(f'ลบคำศัพท์ "{word}" เรียบร้อยแล้ว')
    else:
        print(f'ไม่พบคำศัพท์ "{word}" ในพจนานุกรม')

def display_dictionary(dictionary):
    print('พจนานุกรม:')
    for word, definition in dictionary.items():
        print(f'{word}: {definition}')

def search_word(dictionary, word):
    if word in dictionary:
        print(f'คำศัพท์ "{word}" มีความหมายคือ: {dictionary[word]}')
    else:
        print(f'ไม่พบคำศัพท์ "{word}" ในพจนานุกรม')

def main():
    dictionary = load_dictionary()

    while True:
        print('\nกรุณาเลือกรายการ:')
        print('1. เพิ่มคำศัพท์')
        print('2. ลบคำศัพท์')
        print('3. แสดงคำศัพท์ทั้งหมด')
        print('4. ออกจากโปรแกรม')
        print('5. ค้นหาคำศัพท์')
        choice = input('กรุณาใส่หมายเลขที่ต้องการ: ')

        if choice == '1':
            word = input('กรุณาใส่คำศัพท์: ')
            definition = input('กรุณาใส่ความหมาย: ')
            add_word(dictionary, word, definition)
        elif choice == '2':
            word_to_delete = input('กรุณาใส่คำศัพท์ที่ต้องการลบ: ')
            delete_word(dictionary, word_to_delete)
        elif choice == '3':
            display_dictionary(dictionary)
        elif choice == '4':
            print('ออกจากโปรแกรม')
            break
        elif choice == '5':
            word_to_search = input('กรุณาใส่คำศัพท์ที่ต้องการค้นหา: ')
            search_word(dictionary, word_to_search)

        else:
            print('กรุณาใส่หมายเลขที่ถูกต้อง (1-5)')3

if __name__ == "__main__":
    main()