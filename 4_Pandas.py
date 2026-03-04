import numpy as np
import pandas as pd

# "الداتا" لما تجينا تجينا في ملف "Xl" بصيغةd "csv"
# موقع "colab" هو منصة في "GoogleDrive" للبرمجة تدخل على الاضافات اذا ما موجود
# لتحميل المكتبات في "colab" تكتب "pip install !" لاكن اغلب المكتبات موجودة
# ترتيب تنفيذ الكودات شوي غير الترتيب يعتمد على الي تعمله "Run" اول يعني سيل باي سيل
# صيغة ملف "colab" هي "ipynb"

# ملاحظات للاي بوك و تست و فيتشر

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

print(f"iloc[,],[,]:\n{data.iloc[[0,2],[1,3]]}\n")
print(f"loc['',''],['','']:\n{data.loc[['B','D'],['BB','CC']]}\n")

print(f"iloc[1,3]:\n{data.iloc[1,3]}\n")         # موقع القيمة الي تريدها []
print(f"loc['A','AA']:\n{data.loc['A','CC']}\n") # موقع القيمة الي تريدها []

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
#  feature
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














