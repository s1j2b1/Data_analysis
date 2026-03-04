import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


print('________________________________________________الرسم')

# لازم "Series" او "DataFrame"

d= [5,6,8,10]        # ما ممكن نرسمها لان "list" مو موجودة ضمن مكتبة "pandas"
d= pd.Series(d)      # لازم نحولها الى "Series" أشان نقدر نرسمها
# d.plot(kind='line')  # ترسم

# ما ممكن يرسم من "Series" بهذا الشكل الا بطريقة ما يمكم نكتشفها بعدين
# لان بيكون كل موقع من "Series" يساوي "list"
s4= pd.Series([[1,20.2,3,4],[5,7,0,5],[2,33,5,4],[1,5,65,8]])
print(f"s44444: \n{s4} \n")
# s4[0][0].plot(kind='line')
s4[0]= pd.Series
print(f"s44444: \n{s4} \n")

# ممكن يرسم من "Series" بهذا الشكل
# لاكن بعدني ما عرفت ليش يضهرن كلهن في رسمة وحدة اذا "Series" مو "DataFrame"
s5= pd.Series((1,20.2,3,4,5,7,0,5,2,33,5,4,1,5,65,8))

# s5.plot()                   # تمثيل خطي
# s5.plot(kind='line')        # تمثيل خطي
# s5.plot(kind='pie')         # دائرة
# s5.plot(kind='bar')         # أعمدة متفرقة
# s5.plot(kind='hist')        # أعمدة متلاصقة
# s5.plot(kind='box')         # مال تداول

plt.show()               # تعرض الرسمة



print('________________________________________________الرسم')


# "array" توليد قيم عشوائية على شكل 
student= np.random.uniform(0,100,10).reshape(2,5)
# print(student)
# print(type(student),'\n')

row= ['Math','Python']                            # صفوف
colum= ['Ali','Mohamed','Omar','Nor','Sulaiman']  # اعمدة
# انشاء "DataFrame" الي هي جدول اعتماد على القيم العشوائية من "student"
student_data= pd.DataFrame(student, index=row, columns=colum)

# بمكتبة "pandas"
student_data.plot(kind='line')  # رسم بياني لدرجات الطلاب بشكل خطوط
student_data.plot(kind='hist')  # رسم بياني لدرجات الطلاب بشكل خطوط
student_data.plot(kind='box')   # رسم بياني لدرجات الطلاب بشكل خطوط
plt.show()                      # "matplotlib.pyplot" اظهار الرسمات و يجب استخدام مكتبة 


s3= np.array([[1,20.2,3,4],[5,7,0,5],[2,33,5,4],[1,5,65,8]])
s3_row= ['A','B','C','D']
s3_colum= ['AA','BB','CC','DD']
data_s3= pd.DataFrame(s3, index=s3_row , columns=s3_colum)
# data_s3.plot()               # ترسم
# data_s3.plot(kind='line')
# data_s3.plot(kind='pie')
# data_s3.plot(kind='bar')
# data_s3.plot(kind='hist')
# data_s3.plot(kind='box')

plt.show()               # تعرض الرسمة


print('plt+ ____________________________________________')

x= np.array([3,8,1,10])
y= np.array([30,44,60,80])
z= np.array([50,44,60,10])
l= np.array([5,15,6,105])
v= np.array([51,15,60,15])

plt.subplot(3,2,1) # الارقم الاول: عدد الصور \ الثاني: بالطول ام العرض \ الثالث: موقع الصورة
plt.plot(x,y,'-->', linewidth=3)

plt.subplot(3,2,2)
plt.plot(y,z,'--',marker='*',c='g')
plt.subplot(3,2,3)
plt.plot(z,y,'--',marker='1',color='#eab676')    # "image picker" لتحديد درجة اللون من موقع 
plt.subplot(3,2,4)
plt.scatter(l,v,marker='+',color='#eab606',s=200)    # ترسم نقاط فقط"scatter"

# طريقة نرسم 2داتا بلونين مختلين لما تكون بعض البيانات مشتركة
plt.subplot(3,2,5)
plt.bar(z,l, color='r', bottom= v, alpha=0.5 )
plt.bar(v,y, color='purple')

# يكتب تحت بنوع خط "serif" و لون و حجم
plt.xlabel('nam', fontdict={'family':'serif', 'c':'purple', 'size':20})
plt.ylabel('Age')  # يكتب يسار
plt.title('data')  # يكتب فوق

# رسم خطوط الرسم البياني"x" او"y" او بدون يرسم كامل
# ملاحظة يعمل فقط للرسمة الي قبل هذا السطر لازم نعمل لكل رسمة
plt.grid(axis='x', c='b', linewidth='.5', linestyle='--')


plt.show()

print('pie ____________________________________________')

name= ['A','B','C','D']
spise= [0.2,0,0,0.1]
# لاظهار اسماء البيانات"labels" \ المسافات"explode"
plt.pie(x, explode=spise)

plt.legend()  # مربع الوان البيانات
plt.show()






































































