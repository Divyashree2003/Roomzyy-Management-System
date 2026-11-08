import { useEffect, useState } from "react";
import { Bell, CheckCircle, Send, Siren } from "lucide-react";
import AppLayout from "../components/AppLayout";
import { apiRequest } from "../services/api";

const initialForm = {
  title: "",
  message: "",
  type: "Rent Due",
};

function NotificationModule({ user, currentPage, onNavigate, onLogout }) {
  const [form, setForm] = useState(initialForm);
  const [data, setData] = useState({ notifications: [], alerts: [], logs: [] });
  const [status, setStatus] = useState("");

  const loadData = async () => {
    try {
      setData(await apiRequest("/notifications"));
    } catch (error) {
      setStatus(error.message);
    }
  };

  useEffect(() => {
    loadData();
    const timer = window.setInterval(loadData, 5000);
    return () => window.clearInterval(timer);
  }, []);

  const updateField = (event) => {
    const { name, value } = event.target;
    setForm((current) => ({ ...current, [name]: value }));
  };

  const sendNotification = async (event) => {
    event.preventDefault();
    try {
      await apiRequest("/notifications", {
        method: "POST",
        body: JSON.stringify(form),
      });
      setForm(initialForm);
      setStatus("");
      loadData();
    } catch (error) {
      setStatus(error.message);
    }
  };

  const sendAlert = async () => {
    try {
      await apiRequest("/notifications/alerts", {
        method: "POST",
        body: JSON.stringify({
          title: "Emergency Alert",
          message: form.message || "Immediate staff attention required.",
          severity: "Emergency",
        }),
      });
      setStatus("");
      loadData();
    } catch (error) {
      setStatus(error.message);
    }
  };

  const markRead = async (kind, id) => {
    await apiRequest(`/notifications/${kind}/${id}/read`, { method: "PATCH" });
    loadData();
  };

  return (
    <AppLayout user={user} currentPage={currentPage} onNavigate={onNavigate} onLogout={onLogout}>
      <section className="page-heading">
        <div>
          <h1>Notifications</h1>
          <p>Rent reminders, maintenance updates, visitor alerts, and food menu messages.</p>
        </div>
      </section>

      <section className="management-grid">
        <form className="module-panel" onSubmit={sendNotification}>
          <h2>Send Notification</h2>
          <div className="form-grid">
            <label>
              <span>Title</span>
              <input
                className="form-control"
                name="title"
                value={form.title}
                onChange={updateField}
                required
              />
            </label>
            <label>
              <span>Type</span>
              <select
                className="form-select"
                name="type"
                value={form.type}
                onChange={updateField}
              >
                <option>Rent Due</option>
                <option>Maintenance</option>
                <option>Visitor Alert</option>
                <option>Food Menu</option>
                <option>General</option>
              </select>
            </label>
            <label className="full">
              <span>Message</span>
              <textarea
                className="form-control"
                name="message"
                value={form.message}
                onChange={updateField}
                rows="3"
                required
              />
            </label>
          </div>

          {status && <p className="status-message error">{status}</p>}

          <div className="button-row">
            <button className="btn btn-primary" type="submit">
              <Send size={16} />
              Send
            </button>
            <button className="btn btn-outline-danger" type="button" onClick={sendAlert}>
              <Siren size={16} />
              Emergency Alert
            </button>
          </div>
        </form>

        <div className="module-panel">
          <h2>Notification List</h2>
          <div className="notification-list">
            {data.notifications.length === 0 ? (
              <p>No notifications yet.</p>
            ) : (
              data.notifications.map((item) => (
                <article key={item._id} className={item.isRead ? "read" : ""}>
                  <Bell size={18} />
                  <div>
                    <strong>{item.title}</strong>
                    <span>{item.type}</span>
                    <p>{item.message}</p>
                  </div>
                  {!item.isRead && (
                    <button
                      className="btn btn-sm btn-outline-primary"
                      type="button"
                      onClick={() => markRead("notifications", item._id)}
                    >
                      <CheckCircle size={15} />
                    </button>
                  )}
                </article>
              ))
            )}
          </div>
        </div>
      </section>

      <section className="dashboard-grid">
        <div className="module-panel">
          <h2>Alerts</h2>
          <div className="notification-list">
            {data.alerts.length === 0 ? (
              <p>No alerts yet.</p>
            ) : (
              data.alerts.map((item) => (
                <article key={item._id} className={item.isRead ? "read" : "alert-row"}>
                  <Siren size={18} />
                  <div>
                    <strong>{item.title}</strong>
                    <span>{item.severity}</span>
                    <p>{item.message}</p>
                  </div>
                  {!item.isRead && (
                    <button
                      className="btn btn-sm btn-outline-danger"
                      type="button"
                      onClick={() => markRead("alerts", item._id)}
                    >
                      <CheckCircle size={15} />
                    </button>
                  )}
                </article>
              ))
            )}
          </div>
        </div>

        <div className="module-panel">
          <h2>Message Logs</h2>
          <div className="table-responsive">
            <table className="table align-middle">
              <thead>
                <tr>
                  <th>Channel</th>
                  <th>Recipient</th>
                  <th>Status</th>
                </tr>
              </thead>
              <tbody>
                {data.logs.map((log) => (
                  <tr key={log._id}>
                    <td>{log.channel}</td>
                    <td>{log.recipient}</td>
                    <td>{log.status}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </section>
    </AppLayout>
  );
}

export default NotificationModule;
