// src/errors/AppErrorBoundary.tsx
import React, { type ReactNode } from 'react';

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

  componentDidCatch(error: Error, errorInfo: React.ErrorInfo) {
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
          <button
            onClick={() =>
              this.setState({ hasError: false, errorMessage: '' })
            }
          >
            إعادة المحاولة
          </button>
        </main>
      );
    }

    return this.props.children ?? null;
  }
}
