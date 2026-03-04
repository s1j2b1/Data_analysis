import random
from operator import index
import numpy as np
import pandas as pd
from PIL.ImageOps import expand
from fontTools.ttLib.tables.sbixStrike import sbixGlyphDataOffsetFormatSize

print('csv ____________________________________________')

# ثلاث طرق لقرائة الملف: تجيب الباث تبع الملف
# تسحب الملف كامل داخل بايثون ثم تعمله استدعاء
#  و الفايدة انه لما ترسل لحد ملف البايثون بيكون داخله الملف ما يحتاج يحدد موقعة مرة
# تنسخ بيانات الملف ثم تلصقهن في ملف python.text
# طبعا صيغة "csv" تقدر تقرأ اي نوع من الملفات و تحولها الى "DataFrame"
data= pd.read_csv(r"C:\Users\Lenovo\Desktop\Viewer\JORDAN\Ai\folder\Chocolate_Sales.csv")

print(f"data: \n{data} \n")            # يطبع 5 من الاول و5 من الاخر كنموذج
# يطبع عدد الصفوف الي تريدها من فوق
# اذا بدون رقم اول "5" صفوف
print(f"head(20): \n{data.head(20)} \n")
# يطبع عدد الصفوف الي تريدها من تحت
# اذا بدون رقم اخر "5" صفوف
print(f"tail(20): \n{data.tail(10)} \n")

# ليش"loc" مش"iloc" لان بكل مقارنة يرجع اسم"row" اشان يطبعة فـ"iloc" ما تتعامل مع الاسم
# ليش "&" مش "and" لان "and" تعطي الجواب النهائي "True" او "False"
# اذا القيمة الي بين الاقواس "True" الـ"loc" بتبحث عن اسم "True" ما تحصل
# الـ"&\~\|" تتعامل مع"bet" و ترجع"bet" اشان كذا تعرف ايش المحتوى الي بين الاقواس
# ممكن بدون ما تكتب "loc"
print(f"500 >data[]> 100: \n{
data.loc[(data['Boxes Shipped']<500) & (data['Boxes Shipped']>100)]} \n")

# ترتيب البيانات اعتماد على.. و ممكن على اكثر من عمود
# تصاعدي ا تنازلي "=ascending"
print(f"sort_values : \n{data.sort_values(['Country'], ascending=False)} \n")

print(f"min(): \n{data.min()} \n")   # الاقل من كل عمود و الـ"str" على اول حرف بـ"bet"

print(f"drop(2): \n{data.drop(2)} \n") # يحذف "row" بالاسم
print(f"drop('Country'):\n{data.drop('Country',axis=1)}\n") #يحذف العمود"axis=1"
data.drop(index=1)                  # يحذف "row" باموقع
filt= data[data['Country']== 'UK']  # يرجع اسم "row"
data.drop(index=filt.index)         # يحذف الصفوف التي تحتوي على 'UK'

# كل عنصر في'Country' كم مرة تكرر
print(f"value_counts: \n{data.value_counts('Country')} \n")
print(f"columns: \n{data.columns} \n")
print(f"value_counts: \n{data.value_counts(['Country','Product'])} \n")

# عدد القيم الاكبر و عدد الاصغر
print(f"value_counts: \n{data.value_counts(data['Boxes Shipped']>50)} \n")

# تغيير اسم "row" او "colum"
print(f"rename:\n{data.rename(columns={'Boxes Shipped':'number'}, index={1:'Hi'})}\n")
print(f"data: \n{data} \n")

# استخدم العمود هذا كأسم للصفوف
data.set_index('Country', inplace=True)
print(f"set_index: \n{data} \n")
# يعمل اسماء الصفوف ارقام
data.reset_index(inplace=True)
print(f"reset_index: \n{data} \n")


# اسماء الصفوف الي تحتوي على "India"
print(f"India: \n{data.loc[(data['Country']) == "India"] } \n")
# طريقة ثانية
best_country= ["yemen","UK",'India','oman','Australia']
print(f"isin: \n{data.loc[data['Country'].isin(best_country)]} \n")
print(data.columns)

# تغيير اسماء الاعمدة
data.columns= ['city','name','foods','det','in_many','out_many']
print(f"columns=: \n{data} \n")

# طريقة ثانية
# لازم "inplace=True" و الا ما تنحفظ
data.rename(columns={'city':'city work','name':'man name','foods':'foods name','det':'det out',
                     'in_many':'in come','out_many':'out come'}, inplace=True)

# اذا "False" لازم تنحفظ في متغير كـ"data" جديدة بياناتها من نفس المكان
new_datd= data.rename(columns={'city':'city work','name':'man name','foods':'foods name','det':'det out',
                        'in_many':'in come','out_many':'out come'}, inplace=False)
print(f"new_datd: \n{new_datd} \n")

# تحويل اسماء الاعمدة الى "upper"
data.columns= [i.upper() for i in data.columns]
print(f"upper colum: \n{data} \n")
print(f"columns: \n{data.columns} \n")

# تأكد منهى ما طاعت تصير
data['IN COME']= data['IN COME'].str.replace(r"[$,]",'' ".",regex=True)
# data['IN COME']= data['IN COME'].str.replace(r"[$]","",
#                                              regex=True).replace(r"[,]",".", regex=True).astype(float)
print(f"replace: \n{data} \n")

# تغيير قيم صف
new_datd.loc[2]= ['A','B','C','D',50,2]
new_datd.loc[3,'city_work']= 'oman'        # اذا اسم العمود مو موجود بيعمل عمود جديد و الباقي "NaN"
print(f"new_datd change: \n{new_datd} \n")

print('merge ____________________________________________')

new_datd.rename(columns={'city work':'CITY WORK'}, inplace=True)
merge_data= pd.merge(data,new_datd)        # ملاحظة لازم على الاقل اسم عمود واحد متشابه
print(f"merge: \n{merge_data} \n")

print(data.columns)
# جمع قيم عمودين
print(f"data[]+data[]: \n{data['CITY WORK']+ data['MAN NAME']} \n")

# و ممكن تخليه يظيفة في عمود جديد
data['join']= data['CITY WORK'] + data['MAN NAME']
print(f"data['join']: \n{data} \n")
print(data.columns)

# بدون .str، وش يصير؟
# ❌ ما يشتغل لأنه "split" تشتغل بس على قيمة وحدةstring مو على سلسلة من القيم في عمود كامل
# إذا ما كتبته "expand=True" يعطيك قائمة في نفس العمود

# اذا موجودات قيم غير "str" حولها
# data['CITY WORK'] = data['CITY WORK'].astype(str)
# معنى"str." يا"pandas" طبق دالة "split" على كل صف في هذا العمود
# معنى "expand=True" مفرز في عمودين مختلفات
data['CITY WORK'].str.split('_', expand=True)# لم تزبط معنا لازم نظيف عمودين اشان يقسم فيهم
print(f"split: \n{data} \n")
# data[['A','B']] =data['join'].str.split('_', expand=True)     # لم تزبط معنا
# print(f"split[['A','B']]: \n{data} \n")

# طبق مثد "len" او اي مثد على هذا العمود أو اي..
print(f"apply(len): \n{data['CITY WORK'].apply(len)} \n")
# ليش استخدمنا"lambda" لان"apply" ما تقدر تتعامل مع المثد الي تجي مع اقواس مثل"()upper"
print(f"apply(upper()): \n{data['CITY WORK'].apply(lambda x: x.upper())} \n")

print(f"data: \n{data} \n")

# تطبيق مثد "len" على البيانات كامل
# print(f"applymap(len): \n{data.applymap(str.lower)} \n")      # لم تزبط معنا

# يفصل بين الكلمات يتعامل مع "str" فقط
# للفصل في عمودين مختلفين "expand=True" اذا "False" او اذا ما موجودة يفصل في "list"
print(f"split(): \n{data['CITY WORK'].str.split('s',expand=False)} \n")
print(f"data: \n{data} \n")

print('grob ____________________________________________')

d= np.random.uniform(1,10,15).reshape(5,3)
print(f"d: \n{d} \n")
data1_row= ['A','B','C','D','E']
data1_col= ['AA','BB','CC']
data1= pd.DataFrame(d, index=data1_row, columns=data1_col)
print(f"data1: \n{data1} \n")

# يعطينا القيمة الي تقع بالمنتصف بعد ما يرتبهن
# و ممكن للبيانات كامل
# اذا من ضمن البيانات"str" هو فقط يشوف الارقام
print(f"['BB'] median(): \n{data1['BB'].median()} \n")
print(f"median(): \n{data1.median()} \n") # المنتصف لكل عمود

# يجيب الـ"mean" للعمود"AA" من كل "row""CC" قيمة متشابهة
print(f"groupby(): \n{data1.groupby('CC')['AA'].mean()} \n")

print(f"data1: \n{data1} \n")
# print(f"applymap(): \n{data1.applymap(mean())} \n")           # لم تزبط معنا


# نعمل داتا غير متفرة "None" او "np.nan"
name= pd.Series(('2','4',np.nan,5,5))
Age= pd.Series(('name','Age',3,None,3))

# لاظافة أعمدة إلى الداتا
# "DataFrame" "array" "Series" لازم الاعمدة الي تظيفهن يكونن معرفات
data1 = pd.concat([name,Age], axis='columns', sort=False)
data1.columns= ['AA','BB']
data1.index= ['a','b','c','d','e']
print(f"data1: \n{data1} \n")

# تجمع كامل البيانات الغير متوفرة لكل عمود
print(f"isnull: \n{data1.isnull().sum()} \n")

# حذف السطر الي فيه قيمة غير متوفرة
print(f"dropna: \n{data1.dropna()} \n")

print(f"data1: \n{data1} \n")
# حذف الصف فقط الي كل قيمة غير متوفرة
# ممكن تعدل الخيارات طبعا
print(f"dropna(axis,how): \n{data1.dropna(axis='index', how='all')} \n")

# حذف الصف الي فيه بالعمود"AA" بيانات غير متوفرة
print(f"dropna(axis,how,subset): \n{
data1.dropna(axis='index', how='any', subset=['AA'])} \n")


print(f"fillna(0): \n{data1.fillna(0)} \n")  # يغير القيم الغير متوفرة برقم
# يختار من القيم و يعبي القيم الغير متوفرة
print(f"choice(): \n{data1.fillna(random.choice(['D',22]))} \n")

# ملاحظة لازم كل قيم العمود ارقام
print(f"astype(float): \n{data1['AA'].astype(float).mean()} \n")




















































