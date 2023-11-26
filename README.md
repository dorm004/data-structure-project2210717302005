# data-structure-project2210717302005
เป็นโปรแกรม Python ที่ใช้เพื่อจัดการกับพจนานุกรม (dictionary) ของคำศัพท์ โปรแกรมนี้ให้ผู้ใช้ทำการเลือกทำการเพิ่มคำศัพท์, ลบคำศัพท์, แสดงคำศัพท์ทั้งหมด, ค้นหาคำศัพท์, หรือออกจากโปรแกรม ผ่านทาง command-line interface (CLI) ใน console.

นี่คืออธิบายการทำงานของโค้ด:

load_dictionary(): โปรแกรมจะทำการโหลดพจนานุกรมจากไฟล์ 'dictionary.json' (ถ้ามี) โดยใช้ json.load() และจะ return พจนานุกรมนั้นหรือ dictionary ว่างถ้าไม่พบไฟล์.

save_dictionary(dictionary): ฟังก์ชันนี้จะบันทึกพจนานุกรมลงในไฟล์ 'dictionary.json' โดยใช้ json.dump() และ indent=2 เพื่อทำให้ไฟล์ JSON มีการย่อหน่วย.

add_word(dictionary, word, definition): เพิ่มคำศัพท์ลงในพจนานุกรม, จากนั้น save พจนานุกรมใหม่.

delete_word(dictionary, word): ลบคำศัพท์ออกจากพจนานุกรม, จากนั้น save พจนานุกรมใหม่.

display_dictionary(dictionary): แสดงคำศัพท์ทั้งหมดในพจนานุกรม.

search_word(dictionary, word): ค้นหาคำศัพท์และแสดงความหมาย (ถ้ามี).

main(): เป็นฟังก์ชันหลักที่รันโปรแกรม. ใน loop นี้, ผู้ใช้จะถูกให้เลือกรายการที่ต้องการทำ (เพิ่ม, ลบ, แสดง, ค้นหา, หรือออก) โดยผู้ใช้จะใส่หมายเลขที่เป็นเมนูที่ต้องการ และโปรแกรมจะดำเนินการตามที่ผู้ใช้เลือก.

โค้ดนี้ใช้ไฟล์ 'dictionary.json' เพื่อเก็บข้อมูลของพจนานุกรม และทำให้ผู้ใช้สามารถทำกับพจนานุกรมได้ตลอดเวลาที่โปรแกรมทำงาน โดยไม่ต้องเริ่มต้นใหม่ทุกรอบ.
