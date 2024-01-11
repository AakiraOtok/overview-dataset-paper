import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd

# CONSTANTS

# COLOR FOR TEXTS
TITLE_COLOR = '#0F1035'
LABEL_COLOR = '#0F1035'

# COLOR FOR TICK AND EDGE
TICK_COLOR = '#365486'
EDGE_COLOR = '#365486'

# COLOR FOR FIGURE AND AXES
FIGURE_FACECOLOR = '#FFFFFF' 
AXES_FACECOLOR = '#F9F9F9'

# DATA COLOR
LINE_COLOR = '#DCF2F1'


# Configurations
#plt.rcParams['figure.facecolor'] = FIGURE_FACECOLOR
#plt.rcParams['axes.facecolor'] = AXES_FACECOLOR

plt.rcParams['axes.titlecolor'] = TITLE_COLOR
plt.rcParams['axes.labelcolor'] = LABEL_COLOR

plt.rcParams['xtick.color'] = TICK_COLOR
plt.rcParams['ytick.color'] = TICK_COLOR

plt.rcParams['axes.edgecolor'] = EDGE_COLOR 

# Hide left and right border
plt.rcParams['axes.spines.left'] = False 
plt.rcParams['axes.spines.right'] = False 
plt.rcParams['axes.spines.top'] = False 

# Tạo dữ liệu ví dụ
data = {
    'gpu name': [' GPU A', ' GPU B', ' GPU C'],
    'release date': ['2021-01-01', '2022-02-01', '2023-03-01'],
    'number of transistor': [100, 200, 150]
}

# Tạo DataFrame từ dữ liệu
df = pd.DataFrame(data)

# Chuyển định dạng cột release date sang kiểu datetime
df['release date'] = pd.to_datetime(df['release date'])

# Vẽ đồ thị
plt.plot(df['release date'], df['number of transistor'], 'D', markersize=1)

# Định dạng trục x thành ngày tháng
date_format = mdates.DateFormatter('%Y-%m-%d')
plt.gca().xaxis.set_major_formatter(date_format)

# Đặt khoảng cách giữa các nhãn ngày
plt.gcf().autofmt_xdate()
plt.xticks(rotation=45, fontsize=5)  # Thiết lập kích thước của nhãn trục x
plt.yticks(fontsize=5)  # Thiết lập kích thước của nhãn trục 

# Đặt tên cho trục x và trục y
plt.xlabel('Release Date', fontfamily='monospace', fontsize='small', ha='center')
plt.ylabel('Number of Transistors (million)', fontfamily='monospace', fontsize='small', ha='center')

# Đặt tên cho từng điểm trên đồ thị
for i, row in df.iterrows():
    plt.text(row['release date'], row['number of transistor'], row['gpu name'], fontfamily='monospace', fontstyle='oblique', fontsize='xx-small')

# Hiển thị đồ thị
plt.show()
