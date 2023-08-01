import seaborn as sns
import matplotlib.pyplot as plt

# data
x = [50, 75, 100, 125, 150, 175, 200]
x_yolo3 = [74, 100, 123]
y_yolo3 = [33.0, 31.0, 28.0]

x_yolo4 = [66, 83, 95, 124]
y_yolo4 = [43.5, 42.5, 41.7, 38.2]

x_yolo5 = [113, 182, 376, 602]
y_yolo5 = [49.0, 45.4, 37.4, 28.0]

x_yolo6 = [98, 113, 179, 358, 449, 802]
y_yolo6 = [52.5, 51.7, 49.5, 43.5, 40.3, 35.9]

x_yolo7 = [110, 424, 787]
y_yolo7 = [51.2, 37.4, 33.3]

# color
color3 = "#038355" # 孔雀绿
color4 = "#ffc34e" # 向日黄
color5 = "#9370DB"
color6 = "#3CB371"
color7 = "#FF6347"

# 设置字体
font = {'family' : 'Arial',
        'size'   : 12}
plt.rc('font', **font)
# 绘图
sns.set_style("whitegrid") # 设置背景样式
sns.lineplot(x=x_yolo3, y=y_yolo3, color=color3, linewidth=2.0, marker="o", markersize=8, markeredgecolor="white", markeredgewidth=1.5, label='Yolo3')
sns.lineplot(x=x_yolo4, y=y_yolo4, color=color4, linewidth=2.0, marker="s", markersize=8, markeredgecolor="white", markeredgewidth=1.5, label='Yolo4')
sns.lineplot(x=x_yolo5, y=y_yolo5, color=color5, linewidth=2.0, marker="p", markersize=8, markeredgecolor="white", markeredgewidth=1.5, label='Yolo5')
sns.lineplot(x=x_yolo6, y=y_yolo6, color=color6, linewidth=2.0, marker="h", markersize=8, markeredgecolor="white", markeredgewidth=1.5, label='Yolo6')
sns.lineplot(x=x_yolo7, y=y_yolo7, color=color7, linewidth=2.0, marker="d", markersize=8, markeredgecolor="white", markeredgewidth=1.5, label='Yolo7')
#sns.lineplot(x=x_yolo4, y=y_yolo4, color=color4, linewidth=2.0, marker="s", markersize=8, markeredgecolor="white", markeredgewidth=1.5, label='Yolo4')

# 添加标题和标签
plt.title("Performance Comparison of Yolo Object Detection Models", fontweight='bold', fontsize=12)
plt.xlabel("FPS (Yolo3-4 tested on Tesla V100, Yolo5-7 tested on Tesla T4), BS=1 ", fontsize=10)
plt.ylabel("BBox AP(%)", fontsize=10)
# 添加图例
plt.legend(loc='upper left', frameon=True, fontsize=10)

# 设置刻度字体和范围
plt.xticks(fontsize=10)
plt.yticks(fontsize=10)
plt.xlim(50, 850)
plt.ylim(25, 70)

# 设置坐标轴样式
for spine in plt.gca().spines.values():
    spine.set_edgecolor("#CCCCCC")
    spine.set_linewidth(1.5)
plt.savefig('lineplot.png', dpi=300, bbox_inches='tight')
# 显示图像
plt.show()
