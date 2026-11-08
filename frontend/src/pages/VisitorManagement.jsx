import { LogOut } from "lucide-react";
import ManagementPage from "../components/ManagementPage";
import { apiRequest } from "../services/api";

const fields = [
  { name: "visitorName", label: "Visitor Name", required: true },
  { name: "tenantName", label: "Tenant Name", required: true },
  { name: "roomNumber", label: "Room Number", required: true },
  { name: "phone", label: "Phone", required: true },
  { name: "purpose", label: "Purpose", required: true },
  {
    name: "status",
    label: "Status",
    type: "select",
    options: ["Inside", "Exited"],
    defaultValue: "Inside",
  },
];

const columns = [
  { key: "visitorName", label: "Visitor" },
  { key: "tenantName", label: "Tenant" },
  { key: "roomNumber", label: "Room" },
  { key: "purpose", label: "Purpose" },
  { key: "status", label: "Status" },
];

function VisitorManagement(props) {
  return (
    <ManagementPage
      {...props}
      title="Visitor Management"
      subtitle="Record visitor entry, exit, and complete visitor history."
      resource="visitors"
      fields={fields}
      columns={columns}
      extraActions={(item, refresh) =>
        item.status === "Inside" ? (
          <button
            className="btn btn-sm btn-outline-primary"
            type="button"
            onClick={async () => {
              await apiRequest(`/visitors/${item._id}/exit`, { method: "PATCH" });
              refresh();
            }}
          >
            <LogOut size={15} />
          </button>
        ) : null
      }
    />
  );
}

export default VisitorManagement;
