# ما هي هذه المكتبة
import numpy as np

print('Math____________________________________________')

#
print('sin(90)',np.sin(90),'\n')

#
print(f"sin(90*np.pi/180): \n{np.sin(90*np.pi/180)} \n")

#
print(f"cos(60): \n{np.cos(60)} \n")

#
print(f"tan(90): \n{np.tan(90)} \n")

#للاكبر
print(f"ceil(4.2): \n{np.ceil(4.2)} \n")

# المتوسط
print(f"mean(): \n{np.mean([3,45,14,5])} \n")

# "الاكبر" اول كنا نناديها بالمكتبة الحين عملوهن فنكشن في بايثون
print(f"max(): \n{max([3,45,14,5])} \n")

# "للتقريب" اول كنا نناديها بالمكتبة الحين عملوهن فنكشن في بايثون
print(f"round(10.8): \n{round(10.8)} \n")

print(f"floor(2.8 ): \n{np.floor(2.8 )} \n")  # تشيل بعد الفاصل

x= [1,15,4,9,2,24,7,55,1,23]
# يخربط مواقع القيم
print(f"x: \n{x} ")
np.random.shuffle(x)
print(f"random.shuffle(x): \n{x} \n")

y= np.random.choice(x)              # تختار قيمة بشكل عشوائي
print(f"y: \n{y} \n")

print('array____________________________________________')

# "array" الى "list" تحويل 
test_array= (3,45,14,5)
print(f"test_array: \n{test_array}")
print(np.array(test_array),'\n')

# انشاء "array" طبعا اذا تحتوي على "str" راح يتحول محتواها كامل "str"
a= np.array((5,9,2))
s= np.array([2,5,9,'a'])
print(f"a: \n{a} \n")
print(f"s: \n{s} \n")

# قيم من "0" الى "100" قسمهن على "5" في "array"
print(f"linspace(): \n{np.linspace(0,100,5)} \n")

# range(i,i+3)=> تبدي من 0الى2 \ for i in [2,4,6]=> [{(2,4,6)}]اول مرة2 بعدين4 بعين6 وعادي"i"
R= np.array((range(i,i+3) for i in [2, 4, 6]))    #صار مشكلة ما شغال ما اعرف ايش هي##
print(f"R: \n{R} \n")

# طريقة ثانية يعبي "array" بقيم تبدي"2" تنتهي"21"
# بدون تحديد "reshape" بتكون في "row" واحد
print(f"arange(): \n{np.arange(2,22).reshape(4,5)} \n")

# 2=الصفوف \ 3=الاعمدة "empty" بتطلع "array" شبه فاضية يعني القيم ما تعتبرهن
a1= np.empty((2,3))
print(f"empty: a1 \n{a1} \n")

print('random ____________________________________________')

# 7 ارقام عشوائية بين.. في اري
# reshape(6,2) تحدد كم صف و عمود لاكن لازم ناتج ظرب= size
a2= np.random.uniform(1,10,12).reshape(6,2)
print(f"random.uniform: a2 \n{a2} \n")

# يعبي بقيم > 1 في اري
a3= np.random.random((2,3))
print(f"random.random: a3 \n{a3} \n")

# يعبي قيم عشوائية سالب و موجب \ اذا(0,1,10) بين -1و+1
# 10 قيم\ 1 هو مركز البياتات \
# إذا زودت scale (مثلا خليه 10 بدل 2)، بتصير القيم منتشرة أكثر.
# وإذا قللته (مثلا 0.5)، بتكون مكدسة حول المتوسط بقوة
# مثلا عندي بيانات اشخاص بس الطول ما متوفر عندي
# فراح امل في الكود انه مثلا المتوسط 150 سم
# و مقدار الانحراف 20 سم و عدد القيم على حسب عدد الاشخاص الي عندي
# مثلا 50 فالقيم الي راح تكون اغلبها قريبة من 150
# بعدها نسبة اقل لاعداد الى 130 و170 حوالي 68%
# عدد قليل بيطلع بعيد شوي (مثلا 110 أو 190)، لكن نادر
# والنسبة الأقل تطلع قيم بعيدة جدًا (100 أو 200) وهذه نادرة مرة
# باقي القيم النادرة جدً ممكن تكون
# أصغر من 110 أو أكبر من 190، لكنها قليلة جدًا حوالي 5% أو أقل
# النسب (68%، 95%، 99.7%) كـ قواعد عامة للتوزيع الطبيعي
a4= np.random.normal(loc=150, scale=20, size=50)
print(f"random.normal: a4 \n{a4} \n")

# الناتج int و اري 4 بكل واحد9
# a5= np.random.randint(0,30,36).reshape(6,6)  # الطريقتين نفس الشي
a5= np.random.randint(1,20,(4,9))
print(f"random.randint: a5 \n{a5} ")
print(f"shape: {a5.shape} ") # عدد الصفوف و الاعمدة
print(f"size: {a5.size} \n") # عدد القيم

# تحويل a5 الى كل عنصر وحده بصف
# هذي"array" تسمى "vector" وما يفرق كم صف
# تستخدم للتطبيقات الفيزيائية
a5= a5.reshape(36,1)
print(f"reshape: a5 \n{a5} \n")


# اذا نريد نجمع مع "array" و ما تتغير القيم نعمل "array" معباية كلها "0"
print(f"full(0): \n{np.full((4,8),0)} \n")
# اذا نريد نظرب في "array" و ما تتغير القيم نعمل "array" معباية كلها "1"
print(f"full(1): \n{np.full((4,8),1)} \n")

# طريقة ثانية لإنشاء "array"بـ"0""1"
print(f"zeros(): \n{np.zeros((4,8))} \n")
print(f"ones(): \n{np.ones((4,8))} \n")

"""
# مشروع array

# array random with size and shape
# print with min max mean
# reshape array
# print size and shape

# import numpy as np

# انشاء array بقيم عشوائية بين 1 و 15 ب4 صفوف و 5 أعمدة
student_mark= np.random.uniform(1,15,20).reshape(4,5)
print(f"student_mark: \n{student_mark} \n")

print(f"Max student mark: {np.max(student_mark)}")
print(f"Min student mark: {np.min(student_mark)}")
print(f"Mean student mark: {np.mean(student_mark)}")
print()

# تحويل array من 4صفوف و 5 اعمدة الى 10صفوف و 2 اعمدة
student_mark= student_mark.reshape(10,2)
print(f"student_mark: \n{student_mark} \n")

# توظيح array عبارة عن كم صف و عمود
print(f"Shape student mark array: {np.shape(student_mark)}")
# توظيح عدد عناصر array
print(f"Size student mark array: {np.size(student_mark)}")
print()
"""
print('array+____________________________________________')

array1= np.random.randint(0,20,(4,4))
# ترتب قيم كل "colum" من الاصغر اما إذا "axis=1" ترتب قيم كل "row" من الاصغر
array2= np.sort(array1, axis=0)
print(f"array1: \n{array1}\n")
print(f"array2: \n{array2}\n")

a= np.array([[1,3,6],[1,9,3]])
b= np.array([[9,3,6],[1,5,9]])
# مطلوب مننى بس نعرف ان ممكن نعمل +-*/إلخ...
print(a+2)
print(a*-2)
print(a*b)
print(a/b)

# تعطينا "الانفيرس" تبع الداتا
# يعني كل "colum" يصير "row" و العكس للـ"array"
# دور الداتا لليمين مع تثبيت قيمة اليسار فوق
e1= np.eye((3))  # Identefie array
print(f"e1: \n{e1}\n")












