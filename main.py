# ⁡⁢⁣⁣الخطوة الثانية⁡
# إنشاء الاتصال (𝘊𝘰𝘯𝘯𝘦𝘤𝘵𝘪𝘰𝘯)
conn = sqlite3.connect('school_database.db')

# ⁡⁢⁣⁣الخطوة الثالثة⁡
# إنشاء المؤشر (Cursor)
cursor = conn.cursor()

# ⁡⁢⁣⁣الخطوة الرابعة ⁡
# تنفيذ الاستعلامات(Executing Queries) 
# ⁡⁣⁣⁢إنشاء جدول ⁡
cursor.execute('''
CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER,
    grade INTEGER
)
''')