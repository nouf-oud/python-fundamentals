#Python Learning Journey - week 1
#فحص الفئة العمرية ونسبة الخصم
age = 17
if age >= 60:
    discount_status = "كبار السن 30%"
elif age >= 18:
    discount_status = "بالغ السعر كامل "
elif age >= 5:
    discount_status = "طالب خصم 50%"
else:
    discount_status = "طفل تذكرة مجانية"
print(f" الفئة العمرية: {discount_status}")