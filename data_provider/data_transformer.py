import pandas as pd
import os

folder_path = r"C:\Users\Steve12\Desktop\datamining\project\LTSF-Linear\LTSF-Linear-main\data" 
file_names = os.listdir(folder_path)


def excel_to_csv(input_file, output_file):
    # 读取 Excel 文件
    data = pd.read_excel(input_file)

    # 将数据保存为 CSV 文件
    data.to_csv(output_file, index=False)

if __name__ == "__main__":
    for file_name in file_names:
        if file_name.endswith('xlsx'):
            input_excel_file = os.path.join(folder_path,file_name)
            name = file_name.split('.')[0]
            csv_name = name + '.csv'
            output_csv_file = os.path.join(folder_path,csv_name)   # 输出的 CSV 文件名
            excel_to_csv(input_excel_file, output_csv_file)