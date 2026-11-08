import { useState } from "react";
import { Lock, Mail, Phone, User } from "lucide-react";
import { authApi } from "../services/api";
import "./Login.css";

const initialForm = {
  fullName: "",
  email: "",
  mobile: "",
  password: "",
  confirmPassword: "",
};

const isValidEmail = (email) => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);

function Register({ onRegisterSuccess, onSignIn }) {
  const [form, setForm] = useState(initialForm);
  const [status, setStatus] = useState({ type: "", message: "" });
  const [loading, setLoading] = useState(false);

  const updateField = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!form.fullName.trim()) {
      setStatus({ type: "error", message: "Full Name is required." });
      return;
    }

    if (!isValidEmail(form.email.trim())) {
      setStatus({ type: "error", message: "Enter a valid email address." });
      return;
    }

    if (!form.mobile.trim()) {
      setStatus({ type: "error", message: "Mobile Number is required." });
      return;
    }

    if (form.password.length < 6) {
      setStatus({ type: "error", message: "Password must be at least 6 characters." });
      return;
    }

    if (form.password !== form.confirmPassword) {
      setStatus({ type: "error", message: "Passwords do not match." });
      return;
    }

    setLoading(true);
    setStatus({ type: "", message: "" });

    try {
      await authApi.register({
        fullName: form.fullName.trim(),
        email: form.email.trim().toLowerCase(),
        mobile: form.mobile.trim(),
        password: form.password,
      });
      setStatus({
        type: "success",
        message: "Registration successful. Redirecting to login...",
      });
      setForm(initialForm);
      setTimeout(() => {
        onRegisterSuccess();
      }, 1200);
    } catch (error) {
      setStatus({ type: "error", message: error.message });
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
          <h1>Create the admin account for your PG.</h1>
          <p>Your full name is saved in MongoDB and shown automatically after login.</p>
        </div>
      </section>

      <section className="auth-panel">
        <form className="auth-card" onSubmit={handleSubmit}>
          <div>
            <h2>Register</h2>
            <p>Enter owner or manager details.</p>
          </div>

          <label>
            <span>Full Name</span>
            <div className="auth-input">
              <User size={18} />
              <input
                name="fullName"
                value={form.fullName}
                onChange={updateField}
                placeholder="Divyashree"
                autoComplete="name"
                required
              />
            </div>
          </label>

          <label>
            <span>Email</span>
            <div className="auth-input">
              <Mail size={18} />
              <input
                type="email"
                name="email"
                value={form.email}
                onChange={updateField}
                placeholder="divya@pg.com"
                autoComplete="email"
                required
              />
            </div>
          </label>

          <label>
            <span>Mobile</span>
            <div className="auth-input">
              <Phone size={18} />
              <input
                name="mobile"
                value={form.mobile}
                onChange={updateField}
                placeholder="9876543210"
                autoComplete="tel"
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
                placeholder="Create password"
                autoComplete="new-password"
                minLength="6"
                required
              />
            </div>
          </label>

          <label>
            <span>Confirm Password</span>
            <div className="auth-input">
              <Lock size={18} />
              <input
                type="password"
                name="confirmPassword"
                value={form.confirmPassword}
                onChange={updateField}
                placeholder="Confirm password"
                autoComplete="new-password"
                minLength="6"
                required
              />
            </div>
          </label>

          {status.message && (
            <p className={`status-message ${status.type}`}>{status.message}</p>
          )}

          <button className="btn btn-primary auth-submit" type="submit" disabled={loading}>
            {loading ? "Creating account..." : "Register"}
          </button>

          <p className="auth-switch">
            Already registered?{" "}
            <button type="button" onClick={onSignIn}>
              Login here
            </button>
          </p>
        </form>
      </section>
    </main>
  );
}

export default Register;
