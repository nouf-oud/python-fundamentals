
# حساب مكافأة الاداء
hours = 12
evaluation = "Excellent"
if hours >= 10 and evaluation == "Excellent":
    bonus="مستحق للمكافأةالكاملة(1000)"
elif hours >= 10:
    bonus="مستحق لنصف المكافأة(500)"
else:
    bonus="غير مستحق للمكافأة"
print(f"نتيجة المكافأة: {bonus}")

