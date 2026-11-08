import { CheckCircle } from "lucide-react";
import ManagementPage from "../components/ManagementPage";
import { apiRequest } from "../services/api";

const fields = [
  { name: "tenantName", label: "Tenant Name", required: true },
  { name: "roomNumber", label: "Room Number", required: true },
  { name: "category", label: "Category", required: true },
  { name: "description", label: "Complaint", type: "textarea", required: true, full: true },
  {
    name: "status",
    label: "Status",
    type: "select",
    options: ["Open", "In Progress", "Resolved"],
    defaultValue: "Open",
  },
];

const columns = [
  { key: "tenantName", label: "Tenant" },
  { key: "roomNumber", label: "Room" },
  { key: "category", label: "Category" },
  { key: "status", label: "Status" },
];

function Maintenance(props) {
  return (
    <ManagementPage
      {...props}
      title="Maintenance"
      subtitle="Create complaints, track complaint status, and resolve requests."
      resource="maintenance"
      fields={fields}
      columns={columns}
      extraActions={(item, refresh) =>
        item.status !== "Resolved" ? (
          <button
            className="btn btn-sm btn-outline-success"
            type="button"
            onClick={async () => {
              await apiRequest(`/maintenance/${item._id}/resolve`, { method: "PATCH" });
              refresh();
            }}
          >
            <CheckCircle size={15} />
          </button>
        ) : null
      }
    />
  );
}

export default Maintenance;
