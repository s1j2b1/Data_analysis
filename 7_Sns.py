import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

p= sns.load_dataset('penguins')    # هذي داتا"penguins" موجودة داخل مكتبة "sns"
print(f"p: \n{p.head()} \n")
print(f"columns: \n{p.columns} \n")

# الـ"species" تعملهم طبقات
# مع"multiple" ملون:"stack"|مفرغ:"layer"|ملون كامل الشاشة:"fill"|اعمدة متفرقة:'dodge'
# مع"multiple"  |
plt.subplot(2,2,1)
sns.histplot(data=p, x= 'bill_depth_mm', hue= 'species', multiple='stack')

plt.subplot(2,2,2)
sns.kdeplot(data=p, x= 'bill_depth_mm')
plt.subplot(2,2,3)
sns.kdeplot(data=p, x= 'bill_depth_mm', hue= 'species', multiple='layer')

# كل نوع برسمة في نفس الشاشة "species"
sns.displot(data=p, x= 'bill_depth_mm', hue= 'species', col= 'species')
plt.show()

# الرسمة المنقطة
# sns.scatterplot(data=p, x= 'flipper_length_mm',y= 'bill_length_mm', hue= 'species')
# يرسم كل نوع برسمة منقطة في نفس الشاشة "col= sex" بـ"relplot"
sns.relplot(data=p, x= 'flipper_length_mm',y= 'bill_length_mm', hue= 'species', col='sex')
# يرسم كل نوع بشكل "style= species" بـ"relplot"
# sns.relplot(data=p, x= 'flipper_length_mm',y= 'bill_length_mm', hue= 'species', style='species')
#"size= sex" مع تمييز كل نوع بحجم كبير و صغير
sns.relplot(data=p, x= 'flipper_length_mm',y= 'bill_length_mm', hue= 'species', size='sex')

# عدة تحليلات بالرسم في رسمة وحدة
sns.jointplot(data=p, x= 'flipper_length_mm',y= 'bill_length_mm', hue= 'species')
# عدة تحليلات بالرسم في رسمة وحدة كما ماين كرفت"kind= hist"
sns.jointplot(data=p, x= 'flipper_length_mm',y= 'bill_length_mm', hue= 'species', kind= 'hist')

# عدة رسمات في كل رسمة مقارنة مع بيانات مختلفة
sns.pairplot(data=p, hue= 'species')

plt.show()





































