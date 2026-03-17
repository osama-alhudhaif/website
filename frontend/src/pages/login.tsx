import { Link } from "react-router-dom";

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
                <div style={{ marginTop: "10px" }}>
                    <Link to="/register">انشاء حساب</Link>
                </div>
            </form>
        </div>
    );
}

export default login;