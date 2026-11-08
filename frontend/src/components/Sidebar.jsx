import {
  Bell,
  BedDouble,
  CreditCard,
  LayoutDashboard,
  LogOut,
  Megaphone,
  Users,
  UserCheck,
  Wrench,
} from "lucide-react";

const navItems = [
  { id: "dashboard", label: "Dashboard", icon: LayoutDashboard },
  { id: "tenants", label: "Tenants", icon: Users },
  { id: "rooms", label: "Rooms", icon: BedDouble },
  { id: "payments", label: "Payments", icon: CreditCard },
  { id: "visitors", label: "Visitors", icon: UserCheck },
  { id: "notifications", label: "Notifications", icon: Bell },
  { id: "maintenance", label: "Maintenance", icon: Wrench },
  { id: "broadcasts", label: "Broadcasts", icon: Megaphone },
];

function Sidebar({ currentPage, onNavigate, onLogout }) {
  return (
    <aside className="sidebar">
      <button className="brand" onClick={() => onNavigate("dashboard")} type="button">
        <span>PG</span>
        <strong>PG Manager</strong>
      </button>

      <nav>
        {navItems.map((item) => {
          const Icon = item.icon;
          return (
            <button
              key={item.id}
              className={currentPage === item.id ? "active" : ""}
              onClick={() => onNavigate(item.id)}
              type="button"
            >
              <Icon size={18} />
              {item.label}
            </button>
          );
        })}
      </nav>

      <button className="logout-button" onClick={onLogout} type="button">
        <LogOut size={18} />
        Logout
      </button>
    </aside>
  );
}

export default Sidebar;
