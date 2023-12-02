# ProgramPython03 - โปรแกรมคำนวณเงินโบนัสให้กับพนักงานบริษัท

nameEmployee = str(input("ชื่อพนักงาน >>> "))

sales = float(input("ยอดขาย >>> "))

yearOfService = float(input("อายุงานของพนักงาน >>> "))

if yearOfService == 1 :
    print(f"คุณ {nameEmployee} ยอดขายของคุณเท่ากับ {sales} บาท อายุงานของคุณ {nameEmployee} เท่ากับ {yearOfService} ปี มีสิทธิ์ได้รับโบนัส")

elif yearOfService < 5 :
    bonus1 = 3 / 100 * sales
    print(f"คุณ {nameEmployee} ยอดขายของคุณเท่ากับ {sales} บาท อายุงานของคุณ {nameEmployee} เท่ากับ {yearOfService} ปี ได้รับโบนัส 3% เท่ากับ {bonus1} บาท")

elif yearOfService > 5 :
    bonus2 = 5 / 100 * sales
    print(f"คุณ {nameEmployee} ยอดขายของคุณเท่ากับ {sales} บาท อายุงานของคุณ {nameEmployee} เท่ากับ {yearOfService} ปี ได้รับโบนัส 5% เท่ากับ {bonus2} บาท")

else :
    print(f"ข้อมูลของ {nameEmployee} ผิดพลาด")
