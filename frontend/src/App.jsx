import { useEffect, useState } from "react";
import { Navigate, Route, Routes, useNavigate } from "react-router-dom";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import TenantManagement from "./pages/TenantManagement";
import RoomManagement from "./pages/RoomManagement";
import PaymentManagement from "./pages/PaymentManagement";
import VisitorManagement from "./pages/VisitorManagement";
import NotificationModule from "./pages/NotificationModule";
import Maintenance from "./pages/Maintenance";
import StaffBroadcastTool from "./pages/StaffBroadcastTool";
import { getStoredUser, logout, setAuthSession } from "./services/api";

function App() {
  const [user, setUser] = useState(() => getStoredUser());
  const navigate = useNavigate();

  useEffect(() => {
    const storedUser = getStoredUser();

    if (storedUser) {
      setUser(storedUser);
    }
  }, []);

  const handleAuthenticated = (payload) => {
    const authenticatedUser = payload?.user || payload || getStoredUser();

    setAuthSession(payload);
    setUser(authenticatedUser);
    navigate("/dashboard", { replace: true });
  };

  const handleRegisterSuccess = () => {
    navigate("/login", {
      replace: true,
      state: { message: "Registration successful. Please login." },
    });
  };

  const handleLogout = () => {
    logout();
    setUser(null);
    navigate("/login", { replace: true });
  };

  const handleNavigate = (page) => {
    navigate(`/${page}`);
  };

  const createPageProps = (currentPage) => ({
    user,
    currentPage,
    onNavigate: handleNavigate,
    onLogout: handleLogout,
  });

  const requireAuth = (element) => (user ? element : <Navigate to="/login" replace />);
  const guestOnly = (element) => (user ? <Navigate to="/dashboard" replace /> : element);

  return (
    <Routes>
      <Route path="/" element={<Navigate to={user ? "/dashboard" : "/login"} replace />} />
      <Route
        path="/login"
        element={guestOnly(
          <Login
            onLoginSuccess={handleAuthenticated}
            onRegister={() => navigate("/register")}
          />
        )}
      />
      <Route
        path="/register"
        element={guestOnly(
          <Register
            onRegisterSuccess={handleRegisterSuccess}
            onSignIn={() => navigate("/login")}
          />
        )}
      />
      <Route
        path="/dashboard"
        element={requireAuth(<Dashboard {...createPageProps("dashboard")} />)}
      />
      <Route
        path="/tenants"
        element={requireAuth(<TenantManagement {...createPageProps("tenants")} />)}
      />
      <Route
        path="/rooms"
        element={requireAuth(<RoomManagement {...createPageProps("rooms")} />)}
      />
      <Route
        path="/payments"
        element={requireAuth(<PaymentManagement {...createPageProps("payments")} />)}
      />
      <Route
        path="/visitors"
        element={requireAuth(<VisitorManagement {...createPageProps("visitors")} />)}
      />
      <Route
        path="/notifications"
        element={requireAuth(<NotificationModule {...createPageProps("notifications")} />)}
      />
      <Route
        path="/maintenance"
        element={requireAuth(<Maintenance {...createPageProps("maintenance")} />)}
      />
      <Route
        path="/broadcasts"
        element={requireAuth(<StaffBroadcastTool {...createPageProps("broadcasts")} />)}
      />
      <Route path="*" element={<Navigate to={user ? "/dashboard" : "/login"} replace />} />
    </Routes>
  );
}

export default App;
