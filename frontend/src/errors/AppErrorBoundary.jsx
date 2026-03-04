import React from 'react';

export class AppErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false, errorMessage: '' };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true, errorMessage: error?.message || '' };
  }

  componentDidCatch(error, errorInfo) {
    console.error('App error:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <main style={{ padding: '4rem', textAlign: 'center' }}>
          <h1>صار خطأ غير متوقع</h1>
          {this.state.errorMessage && (
            <p style={{ color: 'red' }}>{this.state.errorMessage}</p>
          )}
          <button onClick={() => this.setState({ hasError: false, errorMessage: '' })}>
            إعادة المحاولة
          </button>
        </main>
      );
    }

    return this.props.children;
  }
}
