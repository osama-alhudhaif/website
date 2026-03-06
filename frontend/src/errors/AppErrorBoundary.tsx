import React, { type ReactNode, type ErrorInfo } from 'react';

interface AppErrorBoundaryProps {
  children?: ReactNode;
}

interface AppErrorBoundaryState {
  hasError: boolean;
  errorMessage: string;
}

export default class AppErrorBoundary extends React.Component<
  AppErrorBoundaryProps,
  AppErrorBoundaryState
> {
  constructor(props: AppErrorBoundaryProps) {
    super(props);
    this.state = { hasError: false, errorMessage: '' };
  }

  static getDerivedStateFromError(error: Error): AppErrorBoundaryState {
    return { hasError: true, errorMessage: error?.message || '' };
  }

  // هنا يتم "صيد" الخطأ وإرساله إليك
  async componentDidCatch(error: Error, errorInfo: ErrorInfo) {
    console.error('App error:', error, errorInfo);

    try {
      // إرسال تقرير الخطأ إلى الباك إند (Django)
      await fetch('/api/errors/report/', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          error_name: error.name,
          message: error.message,
          stack: errorInfo.componentStack, // يعطيك مكان الخطأ بالضبط في شجرة المكونات
          url: window.location.href,
          timestamp: new Date().toISOString(),
        }),
      });
      console.log('تم إرسال تقرير الخطأ تلقائياً للمطور.');
    } catch (sendError) {
      console.error('فشل إرسال تقرير الخطأ:', sendError);
    }
  }

  // دالة محاولة الإصلاح التلقائي (عن طريق تحديث الصفحة أو مسح التخزين المؤقت)
  handleReset = () => {
    // يمكنك إضافة منطق هنا لمسح LocalStorage إذا شككت أنه سبب الخطأ
    this.setState({ hasError: false, errorMessage: '' });
    window.location.reload(); // إعادة تحميل الصفحة كحل أولي "تلقائي"
  };

  render() {
    if (this.state.hasError) {
      return (
        <main style={{ padding: '4rem', textAlign: 'center', direction: 'rtl' }}>
          <h1 style={{ fontSize: '2rem', marginBottom: '1rem' }}>عذراً، حدث خطأ غير متوقع</h1>
          <p style={{ color: '#666', marginBottom: '2rem' }}>
            تم إرسال تفاصيل المشكلة لفريق التطوير للعمل على حلها.
          </p>
          
          {this.state.errorMessage && (
            <div style={{ 
              background: '#fff5f5', 
              padding: '1rem', 
              borderRadius: '8px', 
              border: '1px solid #feb2b2',
              display: 'inline-block',
              marginBottom: '2rem'
            }}>
              <code style={{ color: '#c53030' }}>{this.state.errorMessage}</code>
            </div>
          )}
          <br />
          <button
            onClick={this.handleReset}
            style={{
              padding: '0.8rem 2rem',
              backgroundColor: '#3182ce',
              color: 'white',
              border: 'none',
              borderRadius: '5px',
              cursor: 'pointer',
              fontSize: '1rem'
            }}
          >
            تحديث الصفحة والمحاولة مرة أخرى
          </button>
        </main>
      );
    }

    return this.props.children ?? null;
  }
}