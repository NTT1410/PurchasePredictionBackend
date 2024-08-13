# preprocessing.py
import pandas as pd


# Hàm chuẩn hóa cột phân loại
def discrete(col):
    job = {'blue-collar': 0, 'management': 1, 'technician': 2, 'admin.': 3, 'services': 4, 'retired': 5,
           'self-employed': 6, 'entrepreneur': 7, 'unemployed': 8, 'housemaid': 9, 'student': 10}
    marital = {'married': 0, 'single': 1, 'divorced': 2}
    education = {'secondary': 0, 'tertiary': 1, 'primary': 2}
    default = {'no': 0, 'yes': 1}
    housing = {'yes': 0, 'no': 1}
    loan = {'no': 0, 'yes': 1}
    contact = {'cellular': 0, 'telephone': 1}
    if col.name == 'job':
        return col.map(job)
    elif col.name == 'marital':
        return col.map(marital)
    elif col.name == 'education':
        return col.map(education)
    elif col.name == 'default':
        return col.map(default)
    elif col.name == 'housing':
        return col.map(housing)
    elif col.name == 'loan':
        return col.map(loan)
    elif col.name == 'contact':
        return col.map(contact)


# Hàm chuẩn hóa cột tháng
def month_to_int(col):
    mon_dict = {'jan': 1, 'feb': 2, 'mar': 3, 'apr': 4, 'may': 5, 'jun': 6, 'jul': 7, 'aug': 8, 'sep': 9, 'oct': 10,
                'nov': 11, 'dec': 12}
    return col.map(mon_dict)


# Chuyển các cột khác thành số
def convert_to_numeric(df, columns):
    for col in columns:
        if df[col].dtype == 'object':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df


# Hàm tổng hợp tiền xử lý dữ liệu
def preprocess_data(data):
    df = pd.DataFrame([data])

    # Chuẩn hóa các cột phân loại
    df['job'] = discrete(df['job'])
    df['marital'] = discrete(df['marital'])
    df['education'] = discrete(df['education'])
    df['default'] = discrete(df['default'])
    df['housing'] = discrete(df['housing'])
    df['loan'] = discrete(df['loan'])
    df['contact'] = discrete(df['contact'])

    # Chuẩn hóa cột tháng
    df['month'] = month_to_int(df['month'])

    # Chuyển các cột chuỗi khác thành số
    categorical_columns = ['age', 'balance', 'day', 'duration', 'campaign', 'pdays', 'previous']
    df = convert_to_numeric(df, categorical_columns)
    print(df)
    return df
