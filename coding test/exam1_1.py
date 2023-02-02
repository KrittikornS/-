number = int(input())

ones = ["", "หนึ่ง", "สอง", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า", "สิบ", "สิบเอ็ด", "สิบสอง", "สิบสาม", "สิบสี่", "สิบห้า", "สิบหก", "สิบเจ็ด", "สิบแปด", "สิบเก้า"]
tenth = ["" ,"" ,"ยี่", "สาม", "สี่", "ห้า", "หก", "เจ็ด", "แปด", "เก้า"]

if number < 20:
    print(ones[number])
if number < 100 and number >= 20:
    if number % 10 == 1:
        print(str(tenth[number // 10]) + "เอ็ด")
    else:
        print(str(tenth[number // 10]) + "สิบ" + str(ones[number % 10]))
if number < 1000 and number >= 100:
    if number% 10 == 1:
        print(str(ones[number // 100]) + "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" +  "เอ็ด")
    else:
        print(str(ones[number // 100]) + "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + str(ones[number % 10]))

if number < 10000 and number >= 1000:
    if number % 10 == 1:
         print(str(ones[number // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + "เอ็ด")
    else:
        print(str(ones[number // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + str(ones[number % 10]))

if number < 100000 and number >= 10000:
    if number % 10 == 1:
         print(str(ones[number // 10000]) + "หมื่น" + str(ones[(number % 10000) // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + "เอ็ด") 
    else:
        print(str(ones[number // 10000]) + "หมื่น" + str(ones[(number % 10000) // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + str(ones[number % 10]))
if number < 1000000 and number >= 100000:
    if number % 10 == 1:
        print(str(ones[number // 100000]) + "แสน" + str(ones[(number % 10000) // 10000]) + "หมื่น" + str(ones[(number % 10000) // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + "เอ็ด")
    else:
        print(str(ones[number // 100000]) + "แสน" + str(ones[(number % 10000) // 10000]) + "หมื่น" + str(ones[(number % 10000) // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + str(ones[number % 10]))
if number < 10000000 and number >= 1000000:
    if number % 10 == 1:
        print(str(ones[number // 1000000]) + "ล้าน" + str(ones[(number % 100000) // 100000]) + "แสน" + str(ones[(number % 10000) // 10000]) + "หมื่น" + str(ones[(number % 10000) // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + "เอ็ด")
    else:
        print(str(ones[number // 1000000]) + "ล้าน" + str(ones[(number % 100000) // 100000]) + "แสน" + str(ones[(number % 10000) // 10000]) + "หมื่น" + str(ones[(number % 10000) // 1000]) + "พัน" + str(ones[(number % 1000) // 100]) +  "ร้อย" + str(tenth[(number % 100) // 10]) + "สิบ" + str(ones[number % 10]))     