import { Bell, LogOut, Search } from "lucide-react";

function TopNavbar({ user, onLogout, searchTerm = "", onSearchChange }) {
  const fullName = user?.fullName || user?.name || "User";

  return (
    <header className="top-navbar">
      <div className="search-box">
        <Search size={18} />
        <input
          type="search"
          value={searchTerm}
          onChange={(event) => onSearchChange?.(event.target.value)}
          placeholder="Search tenants, rooms, visitors, payments, notifications"
          aria-label="Search dashboard"
        />
      </div>

      <div className="nav-actions">
        <button className="icon-action" type="button" aria-label="Notifications">
          <Bell size={18} />
        </button>
        <div className="user-chip">
          <span>{fullName.charAt(0).toUpperCase()}</span>
          <div>
            <strong>{fullName}</strong>
            <small>{user?.email || "Logged in"}</small>
          </div>
        </div>
        <button className="icon-action" onClick={onLogout} type="button" aria-label="Logout">
          <LogOut size={18} />
        </button>
      </div>
    </header>
  );
}

export default TopNavbar;
