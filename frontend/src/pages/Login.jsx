import { useState } from "react";
import { Lock, Mail } from "lucide-react";
import { useLocation } from "react-router-dom";
import { authApi, setAuthSession } from "../services/api";
import "./Login.css";

function Login({ onLoginSuccess, onRegister }) {
  const location = useLocation();
  const [form, setForm] = useState({ email: "", password: "" });
  const [status, setStatus] = useState(location.state?.message || "");
  const [statusType, setStatusType] = useState(location.state?.message ? "success" : "error");
  const [loading, setLoading] = useState(false);

  const updateField = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!form.email.trim()) {
      setStatus("Email is required.");
      setStatusType("error");
      return;
    }

    if (!form.password) {
      setStatus("Password is required.");
      setStatusType("error");
      return;
    }

    setLoading(true);
    setStatus("");
    setStatusType("error");

    try {
      const data = await authApi.login(form);
      setAuthSession(data);
      onLoginSuccess(data);
    } catch (error) {
      setStatus(error.message || "Login failed. Check your email and password.");
      setStatusType("error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="auth-page">
      <section className="auth-visual">
        <div className="auth-brand">
          <span>PG</span>
          <strong>PG Management System</strong>
        </div>
        <div className="auth-copy">
          <h1>Run your PG from one focused dashboard.</h1>
          <p>Tenants, rooms, rent, visitors, maintenance, and alerts in one place.</p>
        </div>
      </section>

      <section className="auth-panel">
        <form className="auth-card" onSubmit={handleSubmit}>
          <div>
            <h2>Login</h2>
            <p>Use your registered email and password.</p>
          </div>

          <label>
            <span>Email</span>
            <div className="auth-input">
              <Mail size={18} />
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={updateField}
                placeholder="admin@pg.com"
                autoComplete="email"
                required
              />
            </div>
          </label>

          <label>
            <span>Password</span>
            <div className="auth-input">
              <Lock size={18} />
              <input
                type="password"
                name="password"
                value={form.password}
                onChange={updateField}
                placeholder="Enter password"
                autoComplete="current-password"
                required
              />
            </div>
          </label>

          {status && <p className={`status-message ${statusType}`}>{status}</p>}

          <button className="btn btn-primary auth-submit" type="submit" disabled={loading}>
            {loading ? "Logging in..." : "Login"}
          </button>

          <p className="auth-switch">
            New user?{" "}
            <button type="button" onClick={onRegister}>
              Register here
            </button>
          </p>
        </form>
      </section>
    </main>
  );
}

export default Login;
