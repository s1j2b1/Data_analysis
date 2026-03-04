# ننتبه ان اسم الملف مو نفس اسم المكتبة واحد كبتل

import numpy as np
import pandas as pd   # و ممكن ترسم
import matplotlib.pyplot as plt  # اظهار الرسم

print('Series__________________________________________________')

# ما كثير راح نستخدمها
# الفكرة من "Series" تحط القيم و جنبها موقعها "[]"
# و اخر شي تعطي ":dtype" تبعها
# اذا كلها "int" د"dtype: int"\ اذا وحدة "float" د"dtype: float"\ اذا وحة "str" د"dtype: object"
s = pd.Series([11,22.0,'33',44])
print(f"s: \n{s} \n")

print(f"values: \n{s.values} \n")   # تطبع القيم بشكل "array" و كل قيمة كما هي
print(f"index: \n{s.index} \n")     # القيم تبدي من"index" كم و انتهت الى"index" كم

print(f"describe: \n{s.describe()} \n")
# يعطي ملخص كامل للبيانات
# اذا القيم "number"
# count       عدد القيم
# mean        المتوسط
# std         الانحراف المعياري
# min
# 25%         s تقسيم القيم
# 50%
# 75%
# max
# اذا شي قيم "str"
# count
# unique    ?
# top       ?
# freq      ?
print(f"agg: \n{s.agg(['count'])} \n")
# تحديد البيانات الي تريدها و انتبه في أشياء ما تنفع للـ"str" مثل"max"

print(f"value_counts: \n{s.value_counts()} \n") # كل قيمة و كم مرة تكررت
# طبعا راح نشوف في الطباعة انه "dtype: int64" حتى لو في قيم "str"
# لان هو ما يدخل على القيم و يشوفهن "str" لا هو يشوف القيمة و يشوف كم مرة متكررة في "Series"

s1= pd.Series(['a','b','C',11])
print(f"islower: \n{s1.str.islower()} \n")
# تدخل على "s1" الـ"str" تسأل كل واحد هل هو "lower"


print('series ____________________________________________')

# series
s= pd.Series([1,20.2,3,4])
print(f"s: \n{s} \n")
s= pd.Series([1,20.2,'3',4])
print(f"s: \n{s} \n")
print(f"s[1]: \n{type(s[1])} \n")
print(f"s[2]: \n{type(s[2])} \n")

s= pd.Series([1,20.2,3,4,'A'])
print(f"s: \n{s} \n")

print(f"values: \n{s.values} \n")
print(f"index: \n{s.index} \n")

s1= pd.Series([1,20.2,3,4])
s2= pd.Series(['A','A','a','B','C','x'])
print(f"describe s1: \n{s1.describe()} \n")     # تحليل كامل للبيانات الاكبر الاصغر الخ..
print(f"agg s1: \n{s1.agg(['count','sum','max','sum','mean'])} \n")  # تختار نوع تحليل البيانات

print(f"value_counts s1: \n{s1.value_counts()} \n") # عدد التكرار لكل قيمة
# طبعا راح نشوف في الطباعة انه dtype: int64
# لان هو ما يدخل على القيم و يشوفهن "str" لا هو يشوف القيمة و يشوف كم مرة متكررة في "Series"
print(f"value_counts s2: \n{s2.value_counts()} \n")
print(f"islower(): \n{s2.str.islower()} \n")     # تدخل على "s2" و تعتبر الكل "str" تسأل كل واحد هل هو "lower"


print('projact ____________________________________________')

# مشروع
# قيم عشوائية للطلاب
# اختر الحجم و الابعاد
# حول المصفوفة الى داتا فريم بمكتبة باندا ثم اسماء صفوف و اعمدة
# اطبع الداتا فريم
# طباعة تحليل كامل للبيانات::
# الحصول على ملخص desctibe()
# تفاصيل الاعمدة info()
# اطبع الاعلى \ الاقل \ المتوسط \ عدد القيم لكل عمود على حدة

# عدد الطلاب الذين حصلو على اكبر من 90 اذا اكثر من 5 اطبع is sucess
# انشا رسم بياني ::
# رؤية توزيع الدرجات Histogram
# تحليل القيم المتطرفة box plot


# توليد قيم عشوائية على شكل "array"
student= np.random.uniform(0,100,10).reshape(2,5)
# print(student)
# print(type(student),'\n')

row= ['Math','Python']                            # صفوف
colum= ['Ali','Mohamed','Omar','Nor','Sulaiman']  # اعمدة
# انشاء "DataFrame" الي هي جدول اعتماد على القيم العشوائية من "student"
student_data= pd.DataFrame(student, index=row, columns=colum)

print(f"data_frame: \n{student_data} \n")           # طباعة جدول "DataFrame"
print(f"describe: \n{student_data.describe()} \n")  # تطباعة جميع تفاصيل "DataFrame" الاعلى\ الاقل
print(f"info: \n{student_data.info()} \n")          # للحين ما اعرف ايش تسوي "info"

print(f"max(): \n{student_data[:].max()} \n")     # الدرجة الاعلى لكل طالب
print(f"min: \n{student_data[:].min()} \n")     # الدرجة الاقل لكل طالب
print(f"mean: \n{student_data[:].mean()} \n")   # متوسط الدرجات لكل طالب
print(f"count: \n{student_data[:].count()} \n") # الدرجات متقسمة على كم مادة لكل طالب

print(f"columns: \n{student_data.columns} \n")                       # طباعة جميع عناوين الاعمدة

print(f"student_data: \n{student_data} \n")
print(f"sum(): \n{(student_data>50).sum()} \n")   # جمع كم مره حصل على درجة اكبر من50 لكل طالب
student_great= list((student_data>50).sum()) # تخزين القيم في "list"
print(f"student_great: \n{student_great} \n")

# انشانا لست جديد لنضيف القيم بعد التعديل
# لم نعدل على "list" "student_great" مباشرة لانا ما لقينا "المثد" الي تستبدل القيم
student_have90= []

for i in student_great:  # لنعلم كم طالب حصل على اكبر من50
    if i>1:              # اذا طالب حصل اكثر من مرة على50 نحسبلة مرة1
        student_have90.append(1)
        continue
    student_have90.append(i)

print(f"student_have90: \n{student_have90} \n") # طباعة "list" الجديدة بعد التعديل
print("+"*20)
student_have90= sum(student_have90) # نجمع القيم لنعلم كم طالب حصل على درجة اكبر من 50
print(f"student_have90: \n{student_have90} \n")
if student_have90 > 4:              # اذا اكثر من 4 طلاب حصلوا على اكبر من 50
    print(f"{student_have90} is sucess")


print('DataFrame____________________________________________')

# طبعا الـ"array" لازم تتحول الى "pd.DataFrame" أشان نرسمها
s3= np.array([[1,20.2,3,4],[5,7,0,5],[2,33,5,4],[1,5,65,8]])
s3_row= ['A','B','C','D']          # صفوف
s3_colum= ['AA','BB','CC','DD']    # أعمدة
print(f"array: s3 \n{s3} \n")

# تحويل "array" إلى "DataFrame" مع صفوف و أعمدة
s3_data= pd.DataFrame(s3, index=s3_row , columns=s3_colum)
print(f"DataFrame: \n{s3_data} \n")

print(f"columns: \n{s3_data.columns} \n")   # يطبع عناوين الأعمدة و تسما "فيوتشر" "feature"
print(f"s3_data['BB']:\n{s3_data['BB']}\n") # يطبع بيانات العمود مع عناوين الصفوف

print(f"index: \n{s3_data.index} \n")       # يطبع عناوين الصفوف و تسما "إتريشن" "iteration"
print(f"values: \n{s3_data.values} \n")     # تطبع البيانات و على شكل "array" و تسما "اي بوك" "epoch"

print(f"info: \n{s3_data.info()} \n")
# <class 'pandas.core.frame.DataFrame'>     # "DataFrame" انا اتعامل مع
# Index: 4 entries, A to D                  #  "D" الى "A" عندي "4" صف
# Data columns (total 4 columns):           # اربع اعمدة
# نوع القيم \ القيم المتوفرة بكل عمود \ اسماء الاعمدة
#      Column        Non-Null Count          Dtype
# ---  ------        --------------          -----
#  0   AA            4 non-null             float64
#  1   BB            4 non-null             float64
#  2   CC            4 non-null             float64
#  3   DD            4 non-null             float64
#                                           object  حروف و ارقام او حروف فقط
# dtypes: float64(4)                        # كم عمود من كل نوع
# memory usage: 160.0+ bytes                # استهلاك الذاكرة

print(f"describe: \n{s3_data.describe()} \n") # تعطينا ملخص كل عمود الاكبر \ الاصغر الخ..
print(f"min: \n{s3_data.min()} \n")           # اصغر قيمة في كل عمود
print(f"min:['BB']\n{s3_data['BB'].min()}\n") # القيمة الاصغر في العمود "BB"


s3_data.plot(kind='line')
# s3_data.plot(kind='pie')

# في "DataFrame" عادي تنعرض كل رسمة وحدها
plt.show()               # تعرض الرسمة

print('--------------------------------------')


print('DataFrame ____________________________________________')
# بس تأكد منه هل ممكن ننشئ "DataFrame" كذا
# data = pd.DataFrame({
#     'اسم': ['Ali', 'Omar', 'Sara'],
#     'عمر': [20, 25, 22]})
# print(data.size) # تطلع كم العناصل مع  "nan" عدد العناصر الكليّة (صفوف × أعمدة)
# print(data.shape) # data.shape	تعطي tuple: (عدد الصفوف، عدد الأعمدة)

data= np.array([[1,2,3,33],[4,5,6,66],[7,8,9,99]])
row= ['A','B','C']
colum= ['one','tow','three','four']
data_frame= pd.DataFrame(data, index=row, columns=colum)  # عرض كجدول
print(f"data_frame: \n{data_frame} \n")

print(f"columns: \n{data_frame.columns} \n")
print(f"data_frame: \n{data_frame['one']} \n")
print(f"index: \n{data_frame.index} \n")
print(f"values: \n{data_frame.values} \n")

print('-------------------------------')
print(f"info: \n{data_frame.info()} \n")
print('-------------------------------')
print(f"describe(): \n{data_frame.describe()} \n")
print('-------------------------------')
print(f"min: \n{data_frame.min()} \n")  # اصغر قيمة من كل صف
print('-------------------------------')
print(f"mean: \n{data_frame['three'].mean} \n")   # 'three' المتوسط للعمود



a = np.array([[1,2,3,4],[4,5,6,3],[8,9,6,2]])
df = pd.DataFrame(a, index=['O','T','Th'], columns= ['C1','C2','C3','C4'])
print( f"df: \n{df} \n")
print( f"columns: \n{df.columns} \n")
print( f"iloc[1]: \n{df.iloc[1]} \n")  #index of row #loc ==> Location i ==> int and index
print( f"loc['O']: \n{df.loc['O']} \n") # name of row
print( f"index: \n{df.index} \n")
print( f"df['C1']: \n{df['C1']} \n")
print( f"iloc[:2]: \n{df.iloc[:2]} \n")
print(  f"iloc [:2,1:]: \n{df.iloc [:2 , 1:]} \n") # [row , coulmn] :
print(    f"loc[['',''],['','']]: \n{df.loc[ ['O','Th'],['C1','C4'] ]} \n")  #[]
print( f"loc['O','C3']: \n{df.loc['O','C3']} \n")
print( f"loc[df['']>3]: \n{df.loc[df['C1'] > 3]} \n")

## print(df[(df['C1']>1) & df['C2']<5])
## print(df[(df['C1']>1) and df['C2']<5])

## print(df[(df['C1']>1) | df['C2']<5])
## print(df[(df['C1']>1) or df['C2']<5])



print('loc\\iloc____________________________________________')

s3= np.array([[1,20.2,3,4],[5,7,0,5],[2,33,5,4],[1,5,65,8]])
s3_row= ['A','B','C','D']          # صفوف
s3_colum= ['AA','BB','CC','DD']    # أعمدة
print(f"array: s3 \n{s3} \n")

data= pd.DataFrame(s3, index=s3_row, columns=s3_colum)
print(f"data: \n{data} \n")

print(f"iloc: \n{data.iloc[1]} \n")  # يطبع البيانات الي بالصف مع عناوين الاعمدة بـ[موقع الصف]
print(f"loc: \n{data.loc["A"]} \n")  # يطبع البيانات الي بالصف مع عناوين الاعمدة بـ[اسم الصف]

print(f"iloc[:]: \n{data.iloc[:20]} \n")    # يطبع البيانات الي بالصف مع عناوين الاعمدة بـ[من:إلى]
print(f"iloc[:,:]:\n{data.iloc[:2, :2]}\n") # iloc[:row, :colum] "colum" و من"row" تحدد كم من

print(f"iloc[[0,2]]:\n{data.iloc[[0,2]]}\n")       # تحدد الـ "row" الي تريدهن بالرقم [[]]
print(f"loc[['B','D']]:\n{data.loc[['B','D']]}\n") # تحدد الـ "row" الي تريدهن بالاسم [[]]

print(f"iloc[1,3]:\n{data.iloc[1,3]}\n")         # موقع القيمة الي تريدها []
print(f"loc['A','AA']:\n{data.loc['A','CC']}\n") # موقع القيمة الي تريدها []

print(f"iloc[,],[,]:\n{data.iloc[[0,2],[1,3]]}\n")
print(f"loc['',''],['','']:\n{data.loc[['B','D'],['BB','CC']]}\n")

print(f"iloc[1]>3:\n{data.iloc[1]>3}\n")  # القيم [1]> 3 "True" و "False"
print(f"iloc[[2]>3]:\n{data.iloc[data[2]>3]}\n") # طباعة"row"الي فيه قيم data[2]>3

# في العمود"CC" القيم>3 اطبع "row" تبعهن
print(f"data['CC']>3:{data.loc[data['CC'] > 3]}\n")
print(f"data['CC']>3:{data.loc[(data['CC']>3) & (data['CC']<60)]}\n")

# ما تستخدم"and"استخدم"&"لان"and"تتعامل مع قيمة وحدة على اليمين و وحدة على اليسار
# اما هنا عندنا مجموعة من القيم على الجهتين كـ"Series"
print(data.loc[(data['CC']>3) & (data['CC']<60)]) # ملاحظة جرب خلي كلمة تروو في الداتا هل ايحصلها
# print(data.loc[(data['CC']>3) and (data['CC']<60)])

# اطبع بيانات العمود"BB" فقط القيم فيه متساوية بين "BB""CC"
print(data[data['BB']==data['CC']]['BB'])
print(data[data['BB']>40]['BB'])          # فقط البيانات الي بالعمود"BB" اكبر من40

print('projects____________________________________________')

# مشروع "pandas"
# افتح الملفات 2 و طلع:
# كل عمود ايش البيانات الي فيه
# feature
# كم iteration موجود
# اقرا البيانات بذا الكود data = pd.read_csv("data.csv")  print(data.head())
# ثم اتعامل معها كأنها داتافريم
# طلع الاعلى و الاقل و المتوسط و الانفو و دسكرايب
# استخدم مرتين loc \ iloc


# # للاطلاع على "Xl" بصيغة "csv"
# data1 = pd.read_csv(r"C:\Users\Lenovo\Desktop\viewer\JORDAN\Ai\folder\pixar_films_new.csv"
#                    )  # index_col=5 ,nrows=20 index_col=(0,1,3,5,10,11,12,13,14),
# data2= pd.read_csv(r"C:\Users\Lenovo\Desktop\Viewer\JORDAN\Ai\folder\Chocolate_Sales.csv")
#
# print(f"head():data1 \n{data1.head()} \n")      # عرض الملف بشكل "DataFrame" و ممكن تحدد كم "row"
# print(f"feature:data1 \n{data1.columns} \n")    # عناوين الاعمدة
# print(f"iteration:data1 \n{data1.index} \n")    # عدد "row"
#
# print(f"run_time max:data1 \n{data1['run_\ntime'].max()} \n")    # لقيمة الاعلى في "run_time"
# print(f"run_time min:data1 \n{data1['run_\ntime'].min()} \n")    # لقيمة الادنا في "run_time"
# print(f"run_time mean:data1 \n{data1['run_\ntime'].mean()} \n")  # متوسط القيم في "run_time"
# print(f"run_time info:data1 \n{data1['run_\ntime'].info} \n")    # الي ما منها فائدة "info"
# print(f"run_time describe:data1 \n{data1['run_\ntime'].describe()} \n")  # ملخص القيم في "run_time"
#
# print(f"head():data1 \n{data1.head()} \n")      # عرض الملف بشكل "DataFrame" و ممكن تحدد كم "row"
# print(f"feature:data1 \n{data1.columns} \n")    # عناوين الاعمدة
# print(f"iteration:data1 \n{data1.index} \n")    # عدد "row"
#
# print(f"loc[27]:data1 \n{data1.loc[27]} \n")      # قيم "row" باسم "row"
# print(f"iloc[-1]:data1 \n{data1.iloc[-1]} \n")    # قيم "row" بموقع "row"
# print(f"loc[5,'release_date']:data1\n{data1.loc[5,'release_date']}\n") # قيمة التاريخ لـ"row"
# print(f"loc[[0,1],[1,-1]]:data1 \n{data1.iloc[[0,1],[1,-1]]} \n")      # قيم محددة لاكثر من "row"
# print(data1.tail())
# print("-"*50)
#
# print(f"head():data2 \n{data2.head()} \n")      # عرض الملف بشكل "DataFrame" و ممكن تحدد كم "row"
# print(f"feature:data2 \n{data2.columns} \n")    # عناوين الاعمدة
# print(f"iteration:data2 \n{data2.index} \n")    # عدد "row"
#
# print(f"'Boxes Shipped' max:data2 \n{data2['Boxes Shipped'].max()} \n")    # لقيمة الاعلى في "run_time"
# print(f"'Boxes Shipped' min:data2 \n{data2['Boxes Shipped'].min()} \n")    # لقيمة الادنا في "run_time"
# print(f"'Boxes Shipped' mean:data2 \n{data2['Boxes Shipped'].mean()} \n")  # متوسط القيم في "run_time"
# print(f"'Boxes Shipped' info:data2 \n{data2['Boxes Shipped'].info} \n")    # الي ما منها فائدة "info"
# print(f"'Boxes Shipped' describe:data2 \n{data2['Boxes Shipped'].describe()} \n")  # ملخص القيم في "run_time"
#
# # طباعة"row"الي فيه قيم Boxes Shipped >600
# print(f"data2[]>600: \n{data2.loc[data2['Boxes Shipped']>600]} \n")
# print(f"500 >data2[]> 100: \n{
# data2.loc[(data2['Boxes Shipped']<500) & (data2['Boxes Shipped']>100)]} \n")





