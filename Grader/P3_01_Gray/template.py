n = int(input())
k = int(input())
???
# บรรทัดแรกแสดงต ำแหน่งจ ำนวน k ช่วง เช่น ให้n = 5, k = 11 จะแสดง
# 1-----2-----3-----4-----5-----6-----7-----8-----9-----10----11---
out = ''
for i in range(1,k+1):
    # ให้m มีค่ำ n+1 ถ้ำเป็น k-1 ช่วงแรก
    # ให้m มีค่ำ n ถ้ำเป็นช่วงสุดท้ำย
    ???
    out += str(i) + '-'*m
print(out)
# เริ่มหำ Gray codes และแสดงตำมข้อก ำหนด
???