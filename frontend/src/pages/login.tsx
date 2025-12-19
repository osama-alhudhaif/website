const login = () => {
    return (
        <div>
            <h1>تسجيل الدخول</h1>
            <form>
                <label htmlFor="username">اسم المستخدم</label>
                <input type="text" id="username" name="username" required />
                <br />
                <label htmlFor="password">كلمة المرور</label>
                <input type="password" id="password" name="password" required />
                <br />
                <button type="submit">تسجيل الدخول</button>
                <link href="./pages/register">انشاء حساب</link>
            </form>
        </div>
    );
}

export default login;