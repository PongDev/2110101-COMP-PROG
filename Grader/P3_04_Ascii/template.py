filename = input().strip()
cmd = input().strip()

# ตรวจความถูกต้องของ cmd ถ้าผิดก็แสดงข้อความ Invalid command 
# แล้วใช้คำสั่ง exit(0) เพื่อจบโปรแกรมได้เลย

#???  
  

# อ่านแต่ละบรรทัดในแฟ้มมาเพื่อหาความกว้างของช่องว่างทางขอบซ้ายและขอบขวา
fn = open(filename)
left_margin = 99999         # ให้ช่องว่างทางขอบซ้ายมีค่ามาก ๆ ไว้ก่อน
right_margin = ???
for line in fn:
    line = line.strip()
    # นับจำนวนจุดใน line เริ่มจากขอบซ้ายไปทางขวา หยุดนับเมื่อพบตัวที่ไม่ใช่จุด เก็บในตัวแปร left
    # เช่น ถ้า line = "....|...|.." จะได้ left มีค่า 4
    for left in range(len(line)):
      #???

    if left < left_margin: left_margin = left
    
    # ทำในทำนองเดียวกัน เพื่อหาค่า right_margin
    #???


fn.close()

if cmd != 'STRIP_ALL':
    # LSTRIP, RSTRIP  หรือ STRIP
    # เปิดแฟ้มใหม่เพื่ออ่านข้อมูลอีกรอบ  รอบนี้ อ่านแต่ละบรรทัดมา เพื่อตัดจุดที่ขอบซ้ายและ/หรือขอบขวา ตามคำสั่งแสดง แล้วก็แสดงเลย

    fn = open(filename)

    #???  จัดการกรณี LSTRIP, RSTRIP และ STRIP

    fn.close()

else:    
    # STRIP_ALL 

    fn = open(filename)
    
    #???  ตรงนี้ซับซ้อน ค่อยทำทีหลัง (มี testcases แค่ประมาณ  20% ของทั้งหมด)

    fn.close()