import React, { useState } from "react";
import {
  ArrowLeft,
  Bell,
  Mail,
  MessageSquare,
  Smartphone,
  Save,
} from "lucide-react";

const preferenceRows = [
  {
    id: "rent",
    title: "Rent reminders",
    description: "Payment due dates, overdue rent, and receipt updates.",
  },
  {
    id: "maintenance",
    title: "Maintenance alerts",
    description: "Work orders, repairs, inspections, and closures.",
  },
  {
    id: "visitor",
    title: "Visitor entries",
    description: "Guest check-ins, gate activity, and approval requests.",
  },
  {
    id: "food",
    title: "Food menu updates",
    description: "Daily menu changes and meal service announcements.",
  },
];

export default function NotificationPreferences({ onBack }) {
  const [quietHours, setQuietHours] = useState(true);

  return (
    <div style={styles.page}>
      <aside style={styles.sidebar}>
        <div>
          <h1 style={styles.brand}>PG Management</h1>
          <p style={styles.subtle}>Notification Center</p>
        </div>

        <button type="button" onClick={onBack} style={styles.backButton}>
          <ArrowLeft size={18} />
          Back
        </button>
      </aside>

      <main style={styles.main}>
        <header style={styles.header}>
          <div>
            <p style={styles.eyebrow}>Settings</p>
            <h2 style={styles.title}>Notification Preferences</h2>
            <p style={styles.description}>
              Choose which alerts are sent to tenants and staff.
            </p>
          </div>

          <button type="button" style={styles.saveButton}>
            <Save size={18} />
            Save Changes
          </button>
        </header>

        <section style={styles.channelGrid}>
          <div style={styles.channelCard}>
            <Bell color="#2563eb" />
            <h3>Push</h3>
            <p>Enabled for urgent and operational alerts.</p>
          </div>

          <div style={styles.channelCard}>
            <Mail color="#16a34a" />
            <h3>Email</h3>
            <p>Enabled for summaries and formal notices.</p>
          </div>

          <div style={styles.channelCard}>
            <MessageSquare color="#dc2626" />
            <h3>SMS</h3>
            <p>Enabled only for high-priority alerts.</p>
          </div>
        </section>

        <section style={styles.panel}>
          <div style={styles.panelHeader}>
            <div>
              <h3>Alert Categories</h3>
              <p>Control the default delivery channels for each alert type.</p>
            </div>
            <Smartphone color="#475569" />
          </div>

          {preferenceRows.map((row) => (
            <div key={row.id} style={styles.row}>
              <div>
                <h4>{row.title}</h4>
                <p>{row.description}</p>
              </div>

              <div style={styles.checks}>
                <label>
                  <input type="checkbox" defaultChecked />
                  Push
                </label>
                <label>
                  <input type="checkbox" defaultChecked />
                  Email
                </label>
                <label>
                  <input type="checkbox" />
                  SMS
                </label>
              </div>
            </div>
          ))}
        </section>

        <section style={styles.panel}>
          <div style={styles.row}>
            <div>
              <h3>Quiet Hours</h3>
              <p>Send non-urgent notifications after 8:00 AM.</p>
            </div>

            <label style={styles.switchLabel}>
              <input
                type="checkbox"
                checked={quietHours}
                onChange={(event) => setQuietHours(event.target.checked)}
              />
              Enabled
            </label>
          </div>
        </section>
      </main>
    </div>
  );
}

const styles = {
  page: {
    minHeight: "100vh",
    display: "flex",
    background: "#f3f4f6",
    color: "#111827",
    textAlign: "left",
  },
  sidebar: {
    width: "260px",
    padding: "28px",
    background: "#0f172a",
    color: "#ffffff",
    display: "flex",
    flexDirection: "column",
    justifyContent: "space-between",
  },
  brand: {
    margin: 0,
    fontSize: "25px",
    fontWeight: 700,
    color: "#ffffff",
  },
  subtle: {
    marginTop: "6px",
    color: "#94a3b8",
    fontSize: "14px",
  },
  backButton: {
    border: 0,
    borderRadius: "10px",
    padding: "12px 14px",
    background: "#1e293b",
    color: "#ffffff",
    display: "inline-flex",
    alignItems: "center",
    gap: "8px",
    cursor: "pointer",
  },
  main: {
    flex: 1,
    padding: "32px",
    overflow: "auto",
  },
  header: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    gap: "20px",
    marginBottom: "24px",
  },
  eyebrow: {
    color: "#2563eb",
    fontSize: "13px",
    fontWeight: 700,
    textTransform: "uppercase",
  },
  title: {
    margin: "6px 0",
    fontSize: "34px",
    fontWeight: 700,
    color: "#111827",
  },
  description: {
    color: "#6b7280",
  },
  saveButton: {
    border: 0,
    borderRadius: "10px",
    padding: "13px 18px",
    background: "#2563eb",
    color: "#ffffff",
    display: "inline-flex",
    alignItems: "center",
    gap: "8px",
    cursor: "pointer",
  },
  channelGrid: {
    display: "grid",
    gridTemplateColumns: "repeat(3, minmax(0, 1fr))",
    gap: "18px",
    marginBottom: "24px",
  },
  channelCard: {
    background: "#ffffff",
    borderRadius: "14px",
    padding: "22px",
    boxShadow: "0 8px 20px rgba(15, 23, 42, 0.08)",
  },
  panel: {
    background: "#ffffff",
    borderRadius: "14px",
    padding: "24px",
    boxShadow: "0 8px 20px rgba(15, 23, 42, 0.08)",
    marginBottom: "24px",
  },
  panelHeader: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    paddingBottom: "18px",
    borderBottom: "1px solid #e5e7eb",
  },
  row: {
    display: "flex",
    justifyContent: "space-between",
    alignItems: "center",
    gap: "20px",
    padding: "18px 0",
    borderBottom: "1px solid #e5e7eb",
  },
  checks: {
    minWidth: "250px",
    display: "flex",
    justifyContent: "flex-end",
    gap: "16px",
    color: "#475569",
    fontSize: "14px",
  },
  switchLabel: {
    display: "inline-flex",
    alignItems: "center",
    gap: "8px",
    color: "#2563eb",
    fontWeight: 700,
  },
};
