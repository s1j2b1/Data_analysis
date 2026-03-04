import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

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
print(f"describe s1: \n{s1.describe()} \n")           # تحليل كامل للبيانات الاكبر الاصغر الخ..
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






