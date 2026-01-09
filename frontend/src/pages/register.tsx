const Register = () => {
    return (
        <div>
            <form>
                <h1>انشاء حساب</h1>
                <h3>مرحبا بك في Oda</h3>
                <label htmlFor="username">اسم المستخدم</label>
                <input type="text" id="username" name="username" required />
                <br />
                <label htmlFor="name">الاسم الكامل</label>
                <input type="text" id="name" name="name" required />
                <br />
                <label htmlFor="email">البريد الالكتروني</label>
                <input type="email" id="email" name="email" required />
                <br />
                <label htmlFor="password">كلمة المرور</label>
                <input type="password" id="password" name="password" required />
                <br />
                <label htmlFor="confirmPassword">تأكيد كلمة المرور</label>
                <input type="password" id="confirmPassword" name="confirmPassword" required />
                <br />
                <label htmlFor="dateOfBirth">تاريخ الميلاد</label>
                <input type="date" id="dateOfBirth" name="dateOfBirth" required />
                <br />
                <label htmlFor="gender">الجنس</label>
                <select id="gender" name="gender" required>
                    <option value="male">ذكر</option>
                    <option value="female">أنثى</option>
                    <option value="other">اخرى</option>
                </select>
                <br />
                <label htmlFor="country">البلد</label>
                <select id="country" name="country" required>
                </select>
                <br />
                <label>
                    <input type="checkbox" id="vehicle1" name="vehicle1" value="Bike" />
                    قبول الشروط والاحكام
                </label>
                <br />
                <button type="submit">انشاء حساب</button>
            </form>
        </div>
    );
};

export default Register;
