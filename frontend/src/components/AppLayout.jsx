import Sidebar from "./Sidebar";
import TopNavbar from "./TopNavbar";

function AppLayout({ user, currentPage, onNavigate, onLogout, searchTerm, onSearchChange, children }) {
  return (
    <div className="app-shell">
      <Sidebar currentPage={currentPage} onNavigate={onNavigate} onLogout={onLogout} />
      <main className="workspace">
        <TopNavbar user={user} onLogout={onLogout} searchTerm={searchTerm} onSearchChange={onSearchChange} />
        {children}
      </main>
    </div>
  );
}

export default AppLayout;
