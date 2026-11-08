const API_URL = import.meta.env.VITE_API_URL || "http://localhost:5000/api";
const AUTH_TOKEN_KEY = "token";
const AUTH_USER_KEY = "user";
const LEGACY_TOKEN_KEY = "pg_token";
const LEGACY_USER_KEY = "pg_user";

const safeJsonParse = (value) => {
  if (!value) return null;

  try {
    return JSON.parse(value);
  } catch {
    return null;
  }
};

export const setAuthSession = (payload) => {
  if (!payload) return;

  const token = payload.token || payload.accessToken || null;
  const user = payload.user || payload;

  if (token) {
    localStorage.setItem(AUTH_TOKEN_KEY, token);
    localStorage.setItem(LEGACY_TOKEN_KEY, token);
  }

  if (user && typeof user === "object") {
    localStorage.setItem(AUTH_USER_KEY, JSON.stringify(user));
    localStorage.setItem(LEGACY_USER_KEY, JSON.stringify(user));
  }
};

export const getStoredUser = () => {
  const storedUser = safeJsonParse(localStorage.getItem(AUTH_USER_KEY))
    || safeJsonParse(localStorage.getItem(LEGACY_USER_KEY));

  return storedUser || null;
};

export const logout = () => {
  localStorage.removeItem(AUTH_TOKEN_KEY);
  localStorage.removeItem(AUTH_USER_KEY);
  localStorage.removeItem(LEGACY_TOKEN_KEY);
  localStorage.removeItem(LEGACY_USER_KEY);
};

const requestJson = async (path, options = {}) => {
  const response = await fetch(`${API_URL}${path}`, {
    method: options.method || "GET",
    headers: {
      "Content-Type": "application/json",
      ...(options.headers || {}),
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.message || "Request failed");
  }

  return data;
};

export const getToken = () => localStorage.getItem(AUTH_TOKEN_KEY) || localStorage.getItem(LEGACY_TOKEN_KEY);

export const apiRequest = async (path, options = {}) => {
  const token = getToken();

  const response = await fetch(`${API_URL}${path}`, {
    method: options.method || "GET",
    headers: {
      "Content-Type": "application/json",
      ...(token ? { Authorization: `Bearer ${token}` } : {}),
      ...(options.headers || {}),
    },
    body: options.body ? JSON.stringify(options.body) : undefined,
  });

  const data = await response.json().catch(() => ({}));

  if (!response.ok) {
    throw new Error(data.message || "Request failed");
  }

  return data;
};

export const resourceApi = (resource) => ({
  list: () => apiRequest(`/${resource}`),
  create: (payload) => apiRequest(`/${resource}`, { method: "POST", body: payload }),
  update: (id, payload) => apiRequest(`/${resource}/${id}`, { method: "PUT", body: payload }),
  remove: (id) => apiRequest(`/${resource}/${id}`, { method: "DELETE" }),
});

export const authApi = {
  register: (credentials) =>
    requestJson("/auth/register", {
      method: "POST",
      body: credentials,
    }),
  login: (credentials) =>
    requestJson("/auth/login", {
      method: "POST",
      body: credentials,
    }),
};