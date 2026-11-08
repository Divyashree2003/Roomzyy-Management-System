import { useEffect, useMemo, useState } from "react";
import { BedDouble, CreditCard, IndianRupee, Users, UserCheck } from "lucide-react";
import AppLayout from "../components/AppLayout";
import StatCard from "../components/StatCard";
import { apiRequest, getStoredUser } from "../services/api";

function Dashboard({ user, currentPage, onNavigate, onLogout }) {
  const [searchTerm, setSearchTerm] = useState("");
  const currentUser = getStoredUser() || user;
  const [summary, setSummary] = useState({
    tenants: [],
    rooms: [],
    payments: [],
    visitors: [],
    notifications: [],
  });
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const loadSummary = async () => {
      try {
        const [tenants, rooms, payments, visitors, notificationData] = await Promise.all([
          apiRequest("/tenants"),
          apiRequest("/rooms"),
          apiRequest("/payments"),
          apiRequest("/visitors"),
          apiRequest("/notifications"),
        ]);

        setSummary({
          tenants,
          rooms,
          payments,
          visitors,
          notifications: notificationData.notifications || [],
        });
      } catch (error) {
        console.error(error.message);
      } finally {
        setLoading(false);
      }
    };

    loadSummary();
  }, []);

  const occupiedRooms = summary.rooms.filter((room) => room.status === "Occupied").length;
  const pendingRent = summary.payments
    .filter((payment) => payment.status !== "Paid")
    .reduce((total, payment) => total + Number(payment.amount || 0), 0);
  const insideVisitors = summary.visitors.filter((visitor) => visitor.status === "Inside").length;
  const fullName = currentUser?.fullName || currentUser?.name || currentUser?.full_name || "User";
  const searchQuery = searchTerm.trim().toLowerCase();

  const activities = [
    ...summary.payments.slice(0, 3).map((payment) => ({
      title: `${payment.tenantName} rent ${payment.status}`,
      module: "Payments",
      detail: `Room ${payment.roomNumber} - Rs ${payment.amount}`,
    })),
    ...summary.visitors.slice(0, 3).map((visitor) => ({
      title: `${visitor.visitorName} ${visitor.status}`,
      module: "Visitors",
      detail: `Meeting ${visitor.tenantName}`,
    })),
    ...summary.notifications.slice(0, 3).map((notification) => ({
      title: notification.title,
      module: notification.type,
      detail: notification.message,
    })),
  ].slice(0, 6);

  const filteredActivities = useMemo(() => {
    if (!searchQuery) return activities;

    return activities.filter((activity) =>
      [activity.title, activity.module, activity.detail]
        .join(" ")
        .toLowerCase()
        .includes(searchQuery)
    );
  }, [activities, searchQuery]);

  const searchResults = useMemo(() => {
    if (!searchQuery) return null;

    return {
      tenants: summary.tenants.filter((tenant) =>
        [tenant.tenantName, tenant.roomNumber, tenant.phone, tenant.status]
          .join(" ")
          .toLowerCase()
          .includes(searchQuery)
      ),
      rooms: summary.rooms.filter((room) =>
        [room.roomNumber, room.type, room.status, room.tenantName]
          .join(" ")
          .toLowerCase()
          .includes(searchQuery)
      ),
      payments: summary.payments.filter((payment) =>
        [payment.tenantName, payment.roomNumber, payment.status, String(payment.amount)]
          .join(" ")
          .toLowerCase()
          .includes(searchQuery)
      ),
      visitors: summary.visitors.filter((visitor) =>
        [visitor.visitorName, visitor.tenantName, visitor.status]
          .join(" ")
          .toLowerCase()
          .includes(searchQuery)
      ),
      notifications: summary.notifications.filter((notification) =>
        [notification.title, notification.type, notification.message]
          .join(" ")
          .toLowerCase()
          .includes(searchQuery)
      ),
    };
  }, [searchQuery, summary]);

  return (
    <AppLayout
      user={currentUser}
      currentPage={currentPage}
      onNavigate={onNavigate}
      onLogout={onLogout}
      searchTerm={searchTerm}
      onSearchChange={setSearchTerm}
    >
      <section className="welcome-card">
        <div>
          <p>Admin Dashboard</p>
          <h1>Welcome Back, {fullName} 👋</h1>
          <span>Today&apos;s occupancy, rent, visitor, and alert snapshot.</span>
        </div>
        <button className="btn btn-light" onClick={() => onNavigate("notifications")} type="button">
          View Alerts
        </button>
      </section>

      {searchQuery && (
        <section className="module-panel" style={{ marginBottom: 16 }}>
          <h2>Search Results</h2>
          <p style={{ color: "#5b6b7a", marginBottom: 12 }}>
            Showing matches for “{searchTerm}”.
          </p>
          <div className="table-responsive">
            <table className="table align-middle">
              <thead>
                <tr>
                  <th>Category</th>
                  <th>Matches</th>
                </tr>
              </thead>
              <tbody>
                {Object.entries(searchResults || {}).filter(([, items]) => items.length > 0).length === 0 ? (
                  <tr>
                    <td colSpan="2">No matching records found.</td>
                  </tr>
                ) : Object.entries(searchResults || {}).map(([category, items]) =>
                  items.length > 0 ? (
                    <tr key={category}>
                      <td>{category.charAt(0).toUpperCase() + category.slice(1)}</td>
                      <td>{items.length} record(s)</td>
                    </tr>
                  ) : null
                )}
              </tbody>
            </table>
          </div>
        </section>
      )}

      <section className="stats-grid">
        <StatCard
          label="Total Tenants"
          value={loading ? "..." : summary.tenants.length}
          detail="Active resident records"
          icon={Users}
        />
        <StatCard
          label="Rooms Occupied"
          value={loading ? "..." : `${occupiedRooms}/${summary.rooms.length}`}
          detail="Current occupancy"
          icon={BedDouble}
        />
        <StatCard
          label="Pending Rent"
          value={loading ? "..." : `Rs ${pendingRent}`}
          detail="Payments not marked paid"
          icon={IndianRupee}
        />
        <StatCard
          label="Visitors Inside"
          value={loading ? "..." : insideVisitors}
          detail="Live visitor log"
          icon={UserCheck}
        />
      </section>

      <section className="dashboard-grid">
        <div className="module-panel">
          <h2>Recent Activities</h2>
          <div className="table-responsive">
            <table className="table align-middle">
              <thead>
                <tr>
                  <th>Activity</th>
                  <th>Module</th>
                  <th>Details</th>
                </tr>
              </thead>
              <tbody>
                {filteredActivities.length === 0 ? (
                  <tr>
                    <td colSpan="3">No recent activities yet.</td>
                  </tr>
                ) : (
                  filteredActivities.map((activity, index) => (
                    <tr key={`${activity.title}-${index}`}>
                      <td>{activity.title}</td>
                      <td>{activity.module}</td>
                      <td>{activity.detail}</td>
                    </tr>
                  ))
                )}
              </tbody>
            </table>
          </div>
        </div>

        <div className="module-panel quick-actions">
          <h2>Quick Actions</h2>
          <button className="btn btn-outline-primary" onClick={() => onNavigate("tenants")}>
            <Users size={17} />
            Add Tenant
          </button>
          <button className="btn btn-outline-primary" onClick={() => onNavigate("rooms")}>
            <BedDouble size={17} />
            Add Room
          </button>
          <button className="btn btn-outline-primary" onClick={() => onNavigate("payments")}>
            <CreditCard size={17} />
            Collect Rent
          </button>
        </div>
      </section>
    </AppLayout>
  );
}

export default Dashboard;
