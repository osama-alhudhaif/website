import React, { useState } from 'react';
import axios from 'axios';
import { API_BASE_URL } from '../config/api';

const Register = () => {
    // الحالة الابتدائية بأسماء الحقول المطابقة لـ Django تماماً
    const [formData, setFormData] = useState({
        username: '',
        email: '',
        password: '',
        password_confirm: '', // مطابقة لما طلبه Django سابقاً
        date_of_birth: '',   // مطابقة لاسم الحقل في قاعدة بياناتك
        gender: '',          // موجود في قاعدة بياناتك
        country: '',         // موجود في قاعدة بياناتك
        role: ''             // استخدمنا role بدلاً من accountType
    });

    const [message, setMessage] = useState('');
    const [error, setError] = useState('');

    const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
        setFormData({ ...formData, [e.target.name]: e.target.value });
    };

    const handleSubmit = async (e: React.FormEvent) => {
        e.preventDefault();
        setMessage('');
        setError('');
        
        if (formData.password !== formData.password_confirm) {
            setError("كلمات المرور غير متطابقة!");
            return;
        }

        try {
            // الرابط الكامل الذي تأكدنا من عمله في الباك-إند
            await axios.post(`${API_BASE_URL}/accounts/register/`, formData);
            setMessage("تم إنشاء حسابك في Oda بنجاح! جرب تسجيل الدخول الآن.");
            // الإصدار 12: إزالة console.log الذي قد يعرض بيانات المستخدم (الاسم، البريد، إلخ)
        } catch (err: any) {
            // الإصدار 12: إزالة console.error الذي قد يعرض بيانات حساسة من استجابة الخادم
            // عرض تفاصيل الخطأ بدقة (مثل: اسم المستخدم موجود مسبقاً)
            const errorMsg = err.response?.data 
                ? JSON.stringify(err.response.data) 
                : "خطأ في الاتصال بالسيرفر";
            setError("فشل التسجيل: " + errorMsg);
        }
    };

    return (
        <div style={{ padding: '40px', maxWidth: '500px', margin: '0 auto', textAlign: 'right', direction: 'rtl' }}>
            <h1>إنشاء حساب جديد</h1>
            <p>مرحباً بك في منصة Oda للترجمة الأدبية</p>

            {message && <div style={{ color: 'green', marginBottom: '15px' }}>{message}</div>}
            {error && <div style={{ color: 'red', marginBottom: '15px' }}>{error}</div>}

            <form onSubmit={handleSubmit}>
                <label>اسم المستخدم</label><br/>
                <input type="text" name="username" onChange={handleChange} required style={inputStyle} /><br/>

                <label>البريد الإلكتروني</label><br/>
                <input type="email" name="email" onChange={handleChange} required style={inputStyle} /><br/>

                <label>كلمة المرور</label><br/>
                <input type="password" name="password" onChange={handleChange} required style={inputStyle} /><br/>

                <label>تأكيد كلمة المرور</label><br/>
                <input type="password" name="password_confirm" onChange={handleChange} required style={inputStyle} /><br/>

                <label>تاريخ الميلاد</label><br/>
                <input type="date" name="date_of_birth" onChange={handleChange} required style={inputStyle} /><br/>

                <label>الجنس</label><br/>
                <select name="gender" onChange={handleChange} required style={inputStyle}>
                    <option value="">اختر</option>
                    <option value="male">ذكر</option>
                    <option value="female">أنثى</option>
                    <option value="other">آخر</option>
                </select><br/>

                <select name="role" onChange={handleChange} required style={inputStyle}>
                    <option value="">اختر</option>
                    <option value="WRITER">كاتب (مؤلف)</option>
                    <option value="READER">قارئ</option>
                </select>

                <label>البلد</label><br/>
                <input type="text" name="country" placeholder="مثلاً: Saudi Arabia" onChange={handleChange} required style={inputStyle} /><br/><br/>

                <button type="submit" style={buttonStyle}>إنشاء الحساب</button>
            </form>
        </div>
    );
};

// تنسيق بسيط وسريع
const inputStyle = {
    width: '100%',
    padding: '10px',
    margin: '8px 0',
    borderRadius: '5px',
    border: '1px solid #ccc'
};

const buttonStyle = {
    width: '100%',
    padding: '12px',
    backgroundColor: '#007bff',
    color: 'white',
    border: 'none',
    borderRadius: '5px',
    cursor: 'pointer',
    fontSize: '16px'
};

export default Register;