export const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://127.0.0.1:8000/api/v1';

export const getToken = (): string | null =>
    localStorage.getItem('token') || sessionStorage.getItem('token');

export const getUsername = (): string | null =>
    localStorage.getItem('username') || sessionStorage.getItem('username');

export const getUserId = (): number | null => {
    const id = localStorage.getItem('user_id') || sessionStorage.getItem('user_id');
    return id ? Number(id) : null;
};

export const clearAuth = (): void => {
    localStorage.removeItem('token');
    localStorage.removeItem('username');
    localStorage.removeItem('user_id');
    sessionStorage.removeItem('token');
    sessionStorage.removeItem('username');
    sessionStorage.removeItem('user_id');
};
